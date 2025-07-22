import pandas as pd
import pickle
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset from URL
url = "https://raw.githubusercontent.com/upflairs-pvt-ltd/3rd_july_datascience/master/farmer_guider/farmer.csv"
df = pd.read_csv(url)

# Features and target
X = df.drop('label', axis=1)
y = df['label']

# Train-test split (not strictly needed here)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

# Flask app
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[i]) for i in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    prediction = model.predict([features])[0]
    return render_template('index.html', prediction_text=f'Recommended Crop: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)
