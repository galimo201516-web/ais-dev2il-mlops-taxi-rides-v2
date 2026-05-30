import pandas as pd
import os
import time

df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')

print("CSV types:")
print(df_csv.dtypes)

print("\nParquet types:")
df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq.dtypes)

csv_size = os.path.getsize('example-data/2025-01-01.taxi-rides.csv')
pq_size = os.path.getsize('example-data/2025-01-01.taxi-rides.parquet')

print("\nFile sizes:")
print(f"CSV: {csv_size / 1024:.2f} KB")
print(f"Parquet: {pq_size / 1024:.2f} KB")

t = time.time()
pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print("\nLoad times:")
print(f"CSV: {csv_time:.3f} seconds")
print(f"Parquet: {pq_time:.3f} seconds")