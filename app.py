from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    heart_rate = int(request.form['heart_rate'])
    oxygen = int(request.form['oxygen_level'])
    temperature = float(request.form['temperature'])
    age = int(request.form['age'])

    # Emergency detection logic
    if heart_rate > 120 or oxygen < 90 or temperature > 38:
        prediction_text = "🚨 Emergency Detected!"
    else:
        prediction_text = "✅ Normal Condition"

    # Render HTML with prediction_text
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)