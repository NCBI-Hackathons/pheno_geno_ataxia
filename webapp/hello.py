from flask import Flask, render_template, request
from user_query import user_input_from_gui
from extract_data_from_sqlite import sqlite_to_tsv

app = Flask(__name__)
import os, os.path
import threading
import errno
import sqlite3
import csv


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
        sqlName = result.get("dataFile") + ".sqlite"
        sqlite_to_tsv(sqlName,"cravat.tsv")
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
