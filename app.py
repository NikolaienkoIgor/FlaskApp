from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'), delimiter = ";", encoding="utf8")
        fileName = request.files.get('file').filename
        labels = df['label'].tolist()
        values = df['value'].tolist()
        return render_template('index.html', labels=labels, values=values, fileName = fileName)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/")
# def home():
#     data = [
#         ("01-01-2020", 1597),
#         ("02-01-2020", 1456),
#         ]
#     labels = [row[0] for row in data]
#     values = [row[1] for row in data]    
#     return render_template("graph.html", labels=labels, values=values)