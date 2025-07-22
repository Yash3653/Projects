from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])  # in kg
    height_feet = float(request.form['height'])  # in feet
    height_m = height_feet * 0.3048  # convert feet to meters

    bmi = weight / (height_m ** 2)

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return render_template("result.html", bmi=round(bmi, 2), category=category)

if __name__ == '__main__':
    app.run(debug=True)