from flask import Flask, render_template, request
import functions as func

app = Flask(__name__)


@app.route("/convert", methods=["GET", "POST"])
def isleap():
    if request.method == "GET":
        return render_template("ivesta.html")
    elif request.method == "POST":
        skaicius = str(request.form["skaicius"])
        if skaicius.isdigit():
            skaicius = func.arabic_to_roman(int(skaicius))
        else:
            skaicius = func.roman_to_arabic(skaicius)
        return render_template("atsakymas.html", skaicius=str(skaicius))


if __name__ == "__main__":
    app.run(debug=True)
