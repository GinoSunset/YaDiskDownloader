Script to copy folder from Yandex.disk
---------

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


Example
------------
Download file from folder `Catalog` and `Catalog 2` 
```
python backup.py --token My_secret_token --dirs Catalog Catalog2
```