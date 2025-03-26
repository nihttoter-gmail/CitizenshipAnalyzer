import pandas as pd
import matplotlib

from utils.normalize_dataset import normalize_dataset

original_ds = pd.read_json("./data/raw.json")
normalized_ds = original_ds.apply(normalize_dataset, axis="columns")
normalized_ds = normalized_ds.drop('month', axis="columns")
normalized_ds = normalized_ds.drop('year', axis="columns")
normalized_ds = normalized_ds.drop('day', axis="columns")
normalized_ds = normalized_ds.drop('steps', axis="columns")

normalized_ds.to_json('./data/raw-normalized.json', orient='records')


print(normalized_ds.head(1))
