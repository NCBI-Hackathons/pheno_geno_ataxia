import pandas as pd
import numpy as np
import os

data = None  # Global score file in pandas dataframe


def get_tables():
    """
    input raw data from csv files, do preprocessing - rename columns shorter, drop any
    NA data from table.
    Note: We can disscuss if we need to drop NA or impute them
    """
    global data
    filename = "resources/residue_table.csv"
    data = pd.read_csv(filename)
    all_columns = list(data.columns)
    data.rename(
        columns={
            all_columns[0]: "hgnc_gene",
            all_columns[1]: "score_wo_prcnt",
            all_columns[2]: "score_prcnt",
        },
        inplace=True,
    )
    data.dropna(inplace=True)


def user_input_from_gui(min_score, head_dir, max_score="NO"):
    """
    The interface of user request from GUI of our web app. The request handler
    should call this method to filter and write data into server's current
    working directory. file format: min.csv, if there is no max or min-max.to_csv
    otherwise. The function does not return any value.
    Note: a) We can retrun a json object if we want to show this data in view
    b) currently get_tables is called each time a user request. It can be tuned
    to improve performance for large number of user request handle

    """
    get_tables()
    global data
    cwd = os.getcwd()
    os.chdir(head_dir)
    if max_score == "NO":
        data_ = data[data["score_wo_prcnt"] >= min_score]
        fname = str(round(min_score, 2)) + ".tsv"
        data_.to_csv(fname, index=False, sep="\t")
    elif isinstance(max_score, int) or isinstance(max_score, float):
        data_ = data[
            (data["score_wo_prcnt"] >= min_score)
            & (data["score_wo_prcnt"] <= max_score)
        ]
        fname = str(round(min_score, 2)) + "-" + str(round(max_score, 2)) + ".tsv"
        data_.to_csv(fname, index=False, sep="\t")


# user_input_from_gui(1)
