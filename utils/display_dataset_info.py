from config import SHOW_LOGS

class bcolors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def display_dataset_info(dataset, dataset_name="Dataset"):
    if not SHOW_LOGS:
        return
    print("****************************************************************")
    print(f"Dataset {bcolors.OK_GREEN}<{dataset_name}>{bcolors.ENDC} Information:")
    print("****************************************************************")
    dataset.info()
    print("****************************************************************")
    print("First few rows:")
    print(dataset.head())
    print("****************************************************************")
