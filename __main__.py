import dropbox
from glob import glob
import os
from dotenv import load_dotenv


def run():
    load_dotenv()

    dbx = dropbox.Dropbox(os.getenv("dbx_token"))
    origin_path = os.getenv("origin_path")
    destination = os.getenv("destination")

    latest_file = glob(os.path.join(origin_path, "*.sql"))[-1]

    dbx_files = [file.name for file in dbx.files_list_folder(
        '/db_backup').entries]
    if os.path.basename(latest_file) not in dbx_files:
        print("ENVIA ARQUIVO PRO DROPBOX")
        with open(latest_file, "rb") as f:
            content = f.read()
            dbx.files_upload(content, os.path.join(
                destination, os.path.basename(latest_file)))


if __name__ == '__main__':
    run()
