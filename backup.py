import argparse
from datetime import datetime
import os
import logging
import pathlib
import shutil
import tarfile
import yadisk


def download_folder(folder, path_to_save, timeout, retry):
    logging.info(f"start download folder {folder}")
    if not (y.exists(folder)):
        logging.error(f"Folder {folder} not exists in Y.disk")
        return
    pathlib.Path(f"{path_to_save}/{folder}").mkdir(parents=True, exist_ok=True)
    for file_ in y.listdir(folder):
        if file_.type == "dir":
            download_folder(
                f"{folder}/{file_.name}", f"{path_to_save}/{file_.name}", timeout, retry
            )
        if file_.type == "file":
            logging.info(f"    start download file {file_.path}")
            y.download(
                file_.path,
                f"{path_to_save}/{folder}/{file_.name}",
                timeout=timeout,
                n_retries=retry,
            )
    logging.info(f"Success download folder {folder}")


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token", help="token yandex disk", default=os.environ.get("TOKEN")
    )
    parser.add_argument(
        "--dirs",
        help="download from folder with pattern",
        default=["Backup"],
        nargs="+",
    )
    parser.add_argument(
        "--no-archive", action="store_true", help="no archive folder after download"
    )
    parser.add_argument("-l", "--log", action="store", default=None)
    parser.add_argument(
        "--timeout",
        action="store",
        default=10,
        type=int,
        help="timeout in seconds for all. Defaults to 10 seconds.",
    )
    parser.add_argument(
        "--retry",
        action="store",
        default=3,
        type=int,
        help="retry connection. Defaults to 3 attempts",
    )
    parser.add_argument(
        "--path-to-download",
        help="path when create folder with date and download all files",
        default=os.path.dirname(__file__),
    )
    return parser.parse_args()


def archive_folder(path_to_archive, folder_to_archive):
    with tarfile.open(path_to_archive, "w:bz2") as f:
        f.add(folder_to_archive)
    shutil.rmtree(folder_to_archive)
    logging.info(f"archive {path_to_archive} save")


if __name__ == "__main__":
    args = parsing_arguments()
    logging.basicConfig(
        filename=args.log,
        level=logging.INFO,
        format="[%(asctime)s] %(levelname).1s %(message)s",
        datefmt="%Y.%m.%d %H:%M:%S",
    )
    logging.info(
        f"""
        Run back with params:
          timeout: {args.timeout}
          retry connection: {args.retry}
          dirs: {args.dirs}
          download to: {args.path_to_download}
        """
    )
    if not args.token:
        logging.exception("Token not set")
        raise ValueError("Token not set")
    y = yadisk.YaDisk(token=args.token)
    date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M")
    path_to_download = os.path.join(args.path_to_download, date)
    for folder in args.dirs:
        download_folder(
            folder, f"{path_to_download}/{folder}", args.timeout, args.retry
        )
    if not args.no_archive:
        archive_folder(f"{date}.tar.bz2", path_to_download)
    logging.info("Success")

