import datetime
import pandas
from utils.display_dataset_info import display_dataset_info


def normalize_dataset_row(row):
    index = 0
    row.steps[6]["duration"] = 0
    for step in row.steps:
        if index == 0:
            row[step["stepId"]] = datetime.datetime(year=row.year, day=row.day, month=row.month + 1).timestamp()
        else:
            if step["duration"] is None:
                row[step["stepId"]] = None
            else:
                if row[row.steps[index - 1]["stepId"]] is None:
                    row[step["stepId"]] = None
                else:
                    previous_date = datetime.datetime.fromtimestamp(row[row.steps[index - 1]["stepId"]])
                    new_date = previous_date + datetime.timedelta(
                        days=step["duration"])
                    row[step["stepId"]] = new_date.timestamp()
        index += 1
    return row


def normalize_dataset(path="./data/raw.json", output_path="./data/raw-normalized.json"):
    # "./data/raw.json"
    # "./data/raw-normalized.json"
    original_ds = pandas.read_json(path)

    display_dataset_info(dataset=original_ds, dataset_name="Original Dataset")

    normalized_ds = original_ds.apply(normalize_dataset_row, axis="columns")
    normalized_ds = normalized_ds.drop('month', axis="columns")
    normalized_ds = normalized_ds.drop('year', axis="columns")
    normalized_ds = normalized_ds.drop('day', axis="columns")
    normalized_ds = normalized_ds.drop('steps', axis="columns")

    display_dataset_info(dataset=normalized_ds, dataset_name="Normalized Dataset")

    normalized_ds.to_json(output_path, orient='records')
    return pandas.read_json(output_path)
