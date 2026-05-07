import pandas as pd
import dask.dataframe as dd
import time
import os
import gzip
import shutil

results = []

# -----------------------
# 1) Pandas Chunks
# -----------------------
start = time.time()

chunksize = 100000
rows = 0

for chunk in pd.read_csv("big_dataset.csv", chunksize=chunksize):
    rows += len(chunk)

end = time.time()

results.append({
    "method": "Pandas Chunks",
    "rows": rows,
    "time_seconds": end - start,
    "file_size_MB": os.path.getsize("big_dataset.csv") / (1024*1024)
})

# -----------------------
# 2) Dask
# -----------------------
start = time.time()

df = dd.read_csv("big_dataset.csv")
rows = df.shape[0].compute()

end = time.time()

results.append({
    "method": "Dask",
    "rows": rows,
    "time_seconds": end - start,
    "file_size_MB": os.path.getsize("big_dataset.csv") / (1024*1024)
})

# -----------------------
# 3) Compression
# -----------------------
with open("big_dataset.csv", "rb") as f_in:
    with gzip.open("big_dataset.csv.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

start = time.time()

df = pd.read_csv("big_dataset.csv.gz", compression="gzip")
rows = len(df)

end = time.time()

results.append({
    "method": "Compression (gzip)",
    "rows": rows,
    "time_seconds": end - start,
    "file_size_MB": os.path.getsize("big_dataset.csv.gz") / (1024*1024)
})

# -----------------------
# Save comparison
# -----------------------
results_df = pd.DataFrame(results)
results_df.to_csv("comparison_results.csv", sep=";", index=False, encoding="utf-8")

print(results_df)
print("Comparison saved to comparison_results.csv")