
import pandas as pd


def read_csv(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe.to_string(index=False)


def read_excel(file_path):
    dataframe = pd.read_excel(file_path)
    return dataframe.to_string(index=False)


def extract_spreadsheet(file_path):
    extension = str(file_path).split(".")[-1].lower()

    if extension == "csv":
        return read_csv(file_path)

    elif extension == "xlsx":
        return read_excel(file_path)

    else:
        raise ValueError("Unsupported spreadsheet format.")