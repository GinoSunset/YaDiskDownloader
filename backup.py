import argparse
from datetime import datetime
import os
import logging
import pathlib
import yadisk


def download_folder(folder, path_to_save):
    logging.error(f"start download folder {folder}")
    if not (y.exists(folder)):
        logging.error(f"Folder {folder} not exists")
        return
    pathlib.Path(f"{date}/{folder}").mkdir(parents=True, exist_ok=True)
    for file_ in y.listdir(folder):
        if file_.type == "dir":
            download_folder(f"{folder}/{file_.name}", f"{path_to_save}/{file_.name}")
        if file_.type == "file":
            logging.error(f"    start download file {file_.path}")
            y.download(file_.path, f"{date}/{folder}/{file_.name}")
    logging.error(f"Success download folder {folder}")


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
        download_folder(folder, f"{date}/{folder}")

