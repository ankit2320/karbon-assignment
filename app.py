from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            data = json.load(file)
            results = probe_model_5l_profit(data)
            return redirect(url_for('show_results', results=json.dumps(results)))
    return render_template('upload.html')

@app.route('/results', methods=['GET'])
def show_results():
    results = json.loads(request.args.get('results'))
    return render_template('results.html', results=results)

if __name__ == '__main__':
     app.run(debug=True)
