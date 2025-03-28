def display_dataset_info(dataset, dataset_name="Dataset"):
    print("****************************************************************")
    print("Dataset <{dataset_name}> Information:".format(dataset_name=dataset_name))
    dataset.info()
    print("****************************************************************")
    print("First few rows:")
    print(dataset.head())
    print("****************************************************************")
