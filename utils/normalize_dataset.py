import datetime


def normalize_dataset(row):
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
    print(row)
    return row
