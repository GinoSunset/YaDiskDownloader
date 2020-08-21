import argparse
from datetime import datetime
import os
import logging
import pathlib
import yadisk


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token", help="token yandex disk", default=os.environ.get("TOKEN")
    )
    parser.add_argument(
        "--dirs",
        help="download from folder with pattern",
        default=["Каталоги", "Каталоги 2"],
        nargs="+",
    )
    args = parser.parse_args()
    if not args.token:
        logging.exception("Token not set")
        raise ValueError("Token not set")
    y = yadisk.YaDisk(token=args.token)
    date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
    for folder in args.dirs:
        pathlib.Path(f"{date}/{folder}").mkdir(parents=True, exist_ok=True)
        if not (y.exists(folder)):
            logging.error(f"Folder {folder} not exists")
            continue
        for file_ in y.listdir(folder):
            # TODO: look directory
            # TODO: make repository
            y.download(folder, f"{date}/{folder}")

