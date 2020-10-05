Script to copy folder from Yandex.disk
---------
Download files from yandex disk. Use for backup. 

Requirements
--------
* yadisk

How to run
-----------
1. Reg app and create debug token for apps in ya.disk ( https://yandex.ru/dev/oauth/doc/dg/tasks/get-oauth-token-docpage/ ) 
1. run script with params `--token <TOKEN>` or create ENVIRON `TOKEN=<TOKEN>`
1. List the directory to download (backup) after the flag `--dirs` otherwise will try to download the default directory 

Flags
--------
|Param|Decription|Default|
|-----|---------|-------|
| `--token`| token to connect ya.disk. For create lookup ( https://yandex.ru/dev/oauth/doc/dg/tasks/get-oauth-token-docpage/) | `None`
|`--dirs`  | folder to download (backup) | `backup`
|`--no-archive` | flag for canceling archiving after downloading | `False`
|`-l` `--logs`| Path to save log file. | `None`
|`--timeout`| timeout in seconds for all. Defaults to 10 seconds.|10
|`--retry`| retry connection. Defaults to 3 attempts |3
|`--path-to-download`| | locate file (`__file__`)


Example
------------
Download file from folder `Catalog` and `Catalog 2` 
```
python backup.py --token My_secret_token --dirs Catalog Catalog2
```

Cron example:
-------
for backup every month
```bash
BASE_DIR=/opt/backup-ya-disk/YaDiskDownloader/backup
LANG=ru_RU.UTF-8

0 0 1 *  * source /opt/backup-ya-disk/YaDiskDownloader/venv/bin/activate ; python3 /opt/backup-ya-disk/YaDiskDownloader/backup.py --token SECRET_TOKEN_FROM_YANDEX --dirs "catalog"  "catalog 2" --path-to-download {$BASE_DIR}  --timeout 101```

