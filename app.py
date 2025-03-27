from flask import Flask, request, render_template
import joblib

# Load the model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('sentiment_tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['text']
    input_vectorized = vectorizer.transform([input_text])
    prediction = model.predict(input_vectorized)
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    return render_template('index.html', prediction_text=f'Sentiment: {sentiment}')

if __name__ == '__main__':
    app.run(debug=True)