from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def line_chart():
    # Generate some random data for the line chart
    data = [random.randint(1, 100) for _ in range(10)]
    labels = [f"Point {i+1}" for i in range(len(data))]
    return render_template("line_chart.html", labels=labels, data=data)

if __name__ == "__main__":
    app.run(debug=True)