from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from convert import convert_csv_to_json
import pandas as pd
import io

app = Flask(__name__)

# Configuration for file upload and data processing
ALLOWED_EXTENSIONS = {'csv'}  # Allowed file extensions
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum allowed file size (16MB)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH  # Set maximum content length for requests

# Function to check if file extension is allowed
def allowed_file(filename):
    """
    Check if the given filename has an allowed file extension.
    
    Args:
        filename (str): Name of the file to check.
        
    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/convert_file', methods=['POST'])
def convert_file():
    """
    Endpoint to handle CSV file upload and convert it to JSON.

    Accepts a POST request with a file upload containing CSV data.
    Reads the CSV file into a pandas DataFrame and converts it to JSON using
    a custom conversion function (convert_csv_to_json).

    Returns:
        JSON response containing converted data if successful, otherwise an error message.
    """
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
    """
    Endpoint to handle CSV data string and convert it to JSON.

    Accepts a POST request with CSV data as a string in the request body.
    Reads the CSV data into a pandas DataFrame using io.StringIO and converts
    it to JSON using a custom conversion function (convert_csv_to_json).

    Returns:
        JSON response containing converted data if successful, otherwise an error message.
    """
    data = request.data.decode('utf-8')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if len(data) > app.config['MAX_CONTENT_LENGTH']:
        return jsonify({'error': 'Data size exceeds limit'}), 400
    
    try:
        df = pd.read_csv(io.StringIO(data))
        return convert_csv_to_json(df)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
