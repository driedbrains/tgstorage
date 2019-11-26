# Personal Telegram cloud

upload files to a personal Telegram cloud from cli.

# Usage:

- get from [https://my.telegram.org/](https://my.telegram.org/) ```api_id``` and ```api_hash```.
- copy secret.py.template to secret.py and edit.

after: 

```bash
git clone https://github.com/driedbrains/tgstorage.git
virtualenv -p python3 tgstorage
cd tgstorage
source bin/activate
pip install -r requirements.txt
python upload.py -u testpic.jpg
```
