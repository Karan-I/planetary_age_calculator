from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_planetary_ages(age):
    return {
        "Mercury": round(age * (365 / 88), 2),
        "Venus": round(age * (365 / 225), 2),
        "Mars": round(age * (365 / 687), 2),
        "Jupiter": round(age / 11.86, 2),
        "Saturn": round(age / 29.46, 2),
        "Uranus": round(age / 84.01, 2),
        "Neptune": round(age / 164.8, 2),
        "Pluto": round(age / 248, 2),
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        birth_year = 2025 - age
        planetary_ages = calculate_planetary_ages(age)
        return render_template("index.html", name=name, age=age, birth_year=birth_year, planetary_ages=planetary_ages)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
