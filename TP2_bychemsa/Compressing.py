import gzip
import shutil

with open("big_dataset.csv", "rb") as f_in:
    with gzip.open("big_dataset.csv.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)