import pandas as pd
import matplotlib

from utils.normalize_dataset import normalize_dataset

normalized_dataset = normalize_dataset(path="./data/raw.json", output_path="./data/raw-normalized.json")

print(normalized_dataset.head(1))
