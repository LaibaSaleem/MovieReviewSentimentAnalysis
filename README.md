# Movie Review Sentiment Analysis
A Flask-based web application that performs sentiment analysis on text reviews using Natural Language Processing (NLP).

## Features
- Preprocesses text data (removes punctuation, stopwords, and converts to lowercase)
- Uses TF-IDF Vectorization for text representation
- Implements Logistic Regression for sentiment classification
- Simple web interface to input text and get predictions

## Technologies Used
- **Python**
- **Flask** (for the web interface)
- **Scikit-learn** (for ML model training)
- **NLTK** (for text preprocessing)
- **Joblib** (for model persistence)
- **Jupyter Notebook** (for experimentation)
- **GitHub** (for version control)

## Installation & Setup
### Clone the Repository
```sh
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

### Install dependencies
```sh
pip install -r requirements.txt
```  

### Run the app
```sh
python app.py
```
The web app will be available at http://127.0.0.1:5000/.
