import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data
df = pd.read_csv(r'C:\Users\Asus\OneDrive\Desktop\Data Science 16\insurance.pred\insurance.csv')

# Encode categorical variables
le_sex = LabelEncoder()
le_smoker = LabelEncoder()
le_region = LabelEncoder()

df['sex'] = le_sex.fit_transform(df['sex'])
df['smoker'] = le_smoker.fit_transform(df['smoker'])
df['region'] = le_region.fit_transform(df['region'])

# Features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save label encoders and model
pickle.dump((model, le_sex, le_smoker, le_region), open('model.pkl', 'wb'))

# Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    sex = le_sex.transform([request.form['sex']])[0]
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = le_smoker.transform([request.form['smoker']])[0]
    region = le_region.transform([request.form['region']])[0]

    input_data = [[age, sex, bmi, children, smoker, region]]
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Predicted Insurance Charge: ₹{prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
