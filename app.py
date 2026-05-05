from flask import Flask, render_template, request

app = Flask(__name__)


def summarize(text):
    sentences = text.split('.')
    summary = '.'.join(sentences[:2])  
    return summary.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    summary = summarize(text)
    word_count = len(text.split())
    return render_template('result.html', summary=summary, word_count=word_count)

if __name__ == "__main__":
    app.run(debug=True)