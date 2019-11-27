# Personal Telegram cloud

upload files to a personal Telegram cloud from CLI.

### Usage:

- get from [https://my.telegram.org/](https://my.telegram.org/) ```api_id``` and ```api_hash```.
- copy secret.py.template to secret.py and edit.


```bash
git clone https://github.com/driedbrains/tgstorage.git
virtualenv -p python3 tgstorage
cd tgstorage
source bin/activate
pip install -r requirements.txt
python upload.py -u testpic.jpg
```
```bash
$ python upload.py --help
usage: upload.py [-h] [-u [filename [filename ...]]] [-l [N]]

Upload file to your Telegram storage

optional arguments:
  -h, --help            show this help message and exit
  -u [filename [filename ...]], --upload [filename [filename ...]]
                        upload file to storage
  -l [N], --list [N]    list last messages (default: 10)

```
