import pandas as pd
import matplotlib.pyplot as pyplot
import datetime

from utils.normalize_dataset import normalize_dataset

normalized_dataset = normalize_dataset(path="./data/raw.json", output_path="./data/raw-normalized.json")

submit_set = normalized_dataset["ApplicationSubmitted"].map(
    lambda date: datetime.datetime.fromtimestamp(date))
pyplot.hist(submit_set)
pyplot.show()

print(normalized_dataset.head(1))
