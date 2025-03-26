import datetime
import pandas


def normalize_dataset_row(row):
    # row["ApplicationSubmitted"] = datetime.date(year=row.year, day=row.day, month=row.month + 1)
    index = 0
    row.steps[6]["duration"] = 0
    for step in row.steps:
        if index == 0:
            row[step["stepId"]] = datetime.date(year=row.year, day=row.day, month=row.month + 1)
        else:
            if step["duration"] is None:
                row[step["stepId"]] = None
            else:
                if row[row.steps[index - 1]["stepId"]] is None:
                    row[step["stepId"]] = None
                else:
                    row[step["stepId"]] = row[row.steps[index - 1]["stepId"]] + datetime.timedelta(
                        days=step["duration"])
        index += 1
    return row


def normalize_dataset(path="./data/raw.json", output_path="./data/raw-normalized.json"):
    # "./data/raw.json"
    # "./data/raw-normalized.json"
    original_ds = pandas.read_json(path)
    normalized_ds = original_ds.apply(normalize_dataset_row, axis="columns")
    normalized_ds = normalized_ds.drop('month', axis="columns")
    normalized_ds = normalized_ds.drop('year', axis="columns")
    normalized_ds = normalized_ds.drop('day', axis="columns")
    normalized_ds = normalized_ds.drop('steps', axis="columns")
    normalized_ds.to_json(output_path, orient='records')
    return pandas.read_json(output_path)
