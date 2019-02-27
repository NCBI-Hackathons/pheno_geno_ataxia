from flask import Flask, render_template, request
from user_query import user_input_from_gui
from extract_data_from_sqlite import sqlite_to_tsv

app = Flask(__name__)
import os, os.path
import threading
import errno
import sqlite3
import csv
import pandas as pd


@app.route("/")
def input():
    return render_template("input.html")


@app.route("/result", methods=["POST", "GET"])
def analysis():
    if request.method == "POST":
        result = request.form
        threads = []
        threads.append(
            threading.Thread(
                target=cravat, args=(result.get("dataFile"), result.get("familyID"))
            )
        )
        if result.get("maxVal") is not None:
            threads.append(
                threading.Thread(
                    target=bari,
                    args=(
                        result.get("minVal"),
                        result.get("familyID"),
                        result.get("maxVal"),
                    ),
                )
            )
        else:
            threads.append(
                threading.Thread(
                    target=bari, args=(result.get("minVal"), result.get("familyID"))
                )
            )
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        if result.get("maxVal") is None:
          min_score = float(result.get("minVal"))
          varianceFile = str(round(result.get("minVal"), 2)) + ".tsv"
        else:
          min_score = float(result.get("minVal"))
          max_score = float(result.get("maxVal"))
          varianceFile = str(round(min_score, 2)) + "-" + str(round(max_score, 2)) + ".tsv"

        sqlName = result.get("dataFile") + ".sqlite"
        sqlite_to_tsv(sqlName,"cravat.tsv")
        df = pd.DataFrame.from_csv("cravat.tsv", sep='\t')
        print(df.get_row(0))
        df1 = pd.DataFrame.from_csv(varianceFile, sep='\t')
        result = pd.merge(df, df1, how='outer', on=[1,"hgnc_gene"])
        result.to_csv("FINAL.tsv", sep='\t')
        return render_template(
            "ran.html", program="All", familyID=result.get("familyID")
        )



def cravat(file_name, familyID):
    os.system("cravat " + file_name + " -t text -d " + familyID)


def anovar():
    result = request.form
    command = (
        "cravat " + result.get("dataFile") + " -t text -d " + result.get("familyID")
    )
    os.system(command)
    return render_template(
        "ran.html", program="Anovar", familyID=result.get("familyID")
    )


def bari(minVal, upperDir, maxVal="NO"):
    try:
        os.makedirs(upperDir)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(upperDir):
            pass
        else:
            raise
    user_input_from_gui(float(minVal), upperDir, float(maxVal))


if __name__ == "__main__":
    app.run(debug=True)
