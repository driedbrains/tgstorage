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
parser.add_argument('-u', '--upload',
                    help='upload file to storage',
                    metavar='filename',
                    action='store',
                    dest='args_file'
)
args = parser.parse_args()
if (len(sys.argv) == 1):
    print(parser.print_help())
    print('Missing required argument')
    sys.exit()

filename = args.args_file

if (os.path.exists(filename) == False):
    print('File "{}" not exist'.format(filename))
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
    file = await client.upload_file(filename)
    res = await client.send_file(entity,
                           file,
                           force_document = True)
    # print(res)


with client:
    client.loop.run_until_complete(main())
