import pandas as pd

df = pd.read_csv("archive_dataset.csv")


del df["pl_orbeccen"]


print(df.shape)

df.to_csv("merge_dataset1.csv")