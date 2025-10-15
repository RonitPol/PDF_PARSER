# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from parsers.hdfc_parser import HDFCParser
from parsers.icici_parser import ICICIParser
from parsers.sbi_parser import SBIParser
from parsers.axis_parser import AxisParser
from parsers.citi_parser import CitiParser

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_bank(text):
    """Detect bank from statement text"""
    text = text.lower()
    if 'hdfc' in text or 'hdfc bank' in text:
        return 'hdfc'
    elif 'icici' in text or 'icici bank' in text:
        return 'icici'
    elif 'state bank' in text or 'sbi card' in text:
        return 'sbi'
    elif 'axis' in text or 'axis bank' in text:
        return 'axis'
    elif 'citi' in text or 'citibank' in text:
        return 'citi'
    else:
        return 'unknown'

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Detect bank and parse
            with open(filepath, 'rb') as f:
                import pdfplumber
                text = ""
                with pdfplumber.open(f) as pdf:
                    for page in pdf.pages:
                        text += page.extract_text() or ""
            
            bank = detect_bank(text)
            
            # Parse based on detected bank
            if bank == 'hdfc':
                parser = HDFCParser(filepath)
            elif bank == 'icici':
                parser = ICICIParser(filepath)
            elif bank == 'sbi':
                parser = SBIParser(filepath)
            elif bank == 'axis':
                parser = AxisParser(filepath)
            elif bank == 'citi':
                parser = CitiParser(filepath)
            else:
                return jsonify({'error': 'Unsupported bank statement'}), 400
            
            result = parser.parse()
            result['detected_bank'] = bank.capitalize()
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify(result)
            
        except Exception as e:
            # Clean up on error
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': f'Parsing failed: {str(e)}'}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/supported-banks', methods=['GET'])
def supported_banks():
    banks = [
        {'name': 'HDFC Bank', 'code': 'hdfc'},
        {'name': 'ICICI Bank', 'code': 'icici'},
        {'name': 'SBI Card', 'code': 'sbi'},
        {'name': 'Axis Bank', 'code': 'axis'},
        {'name': 'Citibank', 'code': 'citi'}
    ]
    return jsonify(banks)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Credit Card Parser API is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)