from flask import Flask, render_template, request

app = Flask(__name__)
import os
import threading


@app.route("/")
def input():
    return render_template("input.html")


@app.route("/result", methods=["POST", "GET"])
def analysis():
    if request.method == "POST":
        result = request.form
        threads = []
        threads.append(
            threading.Thread(cravat(result.get("dataFile"), result.get("familyID")))
        )
        for t in threads:
            t.start()
        for t in threads:
            t.join()
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


if __name__ == "__main__":
    app.run(debug=True)
