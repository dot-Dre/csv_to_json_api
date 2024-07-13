from flask import Flask, request, jsonify
from convert import convert_csv_to_json
import pandas as pd
import io

app = Flask(__name__)

@app.route('/convert_file', methods=['POST'])
def convert_file():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    try:
        df = pd.read_csv(file)
        return convert_csv_to_json(df)
    except Exception as e:
        return jsonify({'error': f'Failed to read CSV: {str(e)}'}), 400
    
@app.route('/convert_data', methods=['POST'])
def convert_data():
    data = request.data.decode('utf-8')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        df = pd.read_csv(io.StringIO(data))
        return convert_csv_to_json(df)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)