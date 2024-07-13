from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from convert import convert_csv_to_json
import pandas as pd
import io

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/convert_file', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        if file.content_length > app.config['MAX_CONTENT_LENGTH']:
            return jsonify({'error': 'File size exceeds limit'}), 400
        
        try:
            df = pd.read_csv(file)
            return convert_csv_to_json(df)
        except Exception as e:
            return jsonify({'error': f'Failed to read CSV: {str(e)}'}), 400
    else:
        return jsonify({'error': 'Invalid file format'}), 400
     
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