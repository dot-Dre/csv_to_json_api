from flask import Flask, request, jsonify
import pandas as pd
from convert import convert_csv_to_json

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    try:
        df = pd.read_csv(file)
        return convert_csv_to_json(df)
    except Exception as e:
        return jsonify({'error': f'Failed to read CSV: {str(e)}'}), 400
    
if __name__ == "__main__":
    app.run(debug=True)