from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Placeholder for prediction logic
    user_input = request.form['user_score']
    predicted_colleges = []  # Replace with ML model output
    return render_template('results.html', colleges=predicted_colleges)

if __name__ == '__main__':
    app.run(debug=True)
