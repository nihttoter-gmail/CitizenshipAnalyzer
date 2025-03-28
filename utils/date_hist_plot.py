import matplotlib.pyplot as pyplot
import matplotlib.patches as patches
from utils.display_dataset_info import display_dataset_info


def date_hist_plot(dates_set, chart_title="Date Histogram", xlabel="Date", ylabel="Count"):
    # Информация о датасете
    display_dataset_info(dataset=dates_set, dataset_name="Histogram chart dataset")

    # Готовим бины
    bins_start = dates_set.min().replace(day=1)
    if dates_set.max().month == 12:
        bins_end = dates_set.max().replace(day=1, month=1, year=dates_set.max().year + 1)
    else:
        bins_end = dates_set.max().replace(day=1, month=dates_set.max().month + 1)

    bins = [bins_start]
    while bins[-1] != bins_end:
        is_last_month = bins[-1].month == 12
        if is_last_month:
            new_bin = bins[-1].replace(month=1, year=(bins[-1].year + 1))
        else:
            new_bin = bins[-1].replace(month=(bins[-1].month + 1))

        bins.append(new_bin)

    # Рисуем график
    legend = "Количество записей: {size}".format(size=str(dates_set.size))

    figure, axes = pyplot.subplots()
    axes.hist(dates_set, bins=bins, label=legend)

    axes.set_label(chart_title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_title(chart_title)
    axes.legend(loc="upper right", fontsize="medium")
    axes.set_yticks(range(1, 15))
    # axes.set_xticks(bins)
    pyplot.show()
