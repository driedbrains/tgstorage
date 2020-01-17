from telethon.tl.types import MessageMediaDocument,MessageMediaPhoto
import pprint
from telethon import TelegramClient, connection
from secret import *
import socks
import argparse
import os
import sys

# it's contained in the imported secret.py
# api_id = secret.api_id
# api_hash = secret.api_hash

parser = argparse.ArgumentParser(description = 'Upload file to your Telegram storage')
parser.add_argument('-u',
                    '--upload',
                    help = 'upload file to storage',
                    metavar = 'filename',
                    action = 'store',
                    nargs = argparse.REMAINDER,
                    dest = 'args_file'
)
parser.add_argument('-l',
                    '--list',
                    help = 'list last messages (default: 10)',
                    metavar='N',
                    const = '10',
                    nargs = '?',
                    type=int,
                    action = 'store',
                    dest = 'args_list_count'
)
args = parser.parse_args()

if (len(sys.argv) == 1):
    print(parser.print_help())
    print('Missing required argument')
    sys.exit()


if (args.args_file is not None):
    filename = args.args_file

    for i in filename:
        if (os.path.exists(i) == False):
            print('File "{}" not exist'.format(i))
            sys.exit()


proxy_ip = '127.0.0.1'
proxy_port = 9050
proxy = (proxy_ip, proxy_port)
entity = 'me'

client = TelegramClient('tgstorage',
                        api_id,
                        api_hash,
                        proxy=(socks.SOCKS5,
                               proxy_ip,
                               proxy_port))

async def main():
    if(args.args_file is not None):
        await upload(entity, filename)

    if(args.args_list_count):
        await listMessages(entity, args.args_list_count)

async def upload(entity, file_list):
    # file = await client.upload_file(filename)
    for f in filename:
        res = await client.send_file(entity,
                                     f,
                                     force_document = True)
    # print(res)


async def listMessages(entity, limit):
    async for message in client.iter_messages(entity,
                                              reverse = False,
                                              limit = limit):
        if isinstance(message.media, MessageMediaDocument):
            media = message.document
            print( media )
            print("------------------------------------")


with client:
    client.loop.run_until_complete(main())
