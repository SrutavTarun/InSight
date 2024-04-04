import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, origins=["http://localhost:5173/python/function1"])
CORS(app, origins=["http://localhost:5173/python/function2"])
CORS(app, origins=["http://localhost:5173/python/function3"])

# @app.route('/members')
# def members():
#   return {"members": ["member1", "member2", "member3"]}

@app.route('/python/function1', methods=['POST','GET'])
def handle_function1():
    uploaded_file = request.files['file']

    if uploaded_file:
        file_path = 'D:\Srutav\Programs\Projects\InSight\images\\tumour.png'  # Construct file path
        try:
            uploaded_file.save(file_path)  # Save the file
            return jsonify({'message': 'File uploaded successfully!'}), 201  # Return success message
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return error message if saving fails
    else:
        return jsonify({'error': 'No file uploaded'}), 400  # Handle missing file


@app.route('/python/function2', methods=['POST','GET'])
def handle_function2():
    uploaded_file = request.files['file']

    if uploaded_file:
        file_path = 'D:\Srutav\Programs\Projects\InSight\images\\pneumonia.png'  # Construct file path
        try:
            uploaded_file.save(file_path)  # Save the file
            return jsonify({'message': 'File uploaded successfully!'}), 201  # Return success message
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return error message if saving fails
    else:
        return jsonify({'error': 'No file uploaded'}), 400  # Handle missing file

@app.route('/python/function3', methods=['POST','GET'])
def handle_function3():
    uploaded_file = request.files['file']

    if uploaded_file:
        file_path = 'D:\Srutav\Programs\Projects\InSight\images\\alzheimers.png'  # Construct file path
        try:
            uploaded_file.save(file_path)  # Save the file
            return jsonify({'message': 'File uploaded successfully!'}), 201  # Return success message
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return error message if saving fails
    else:
        return jsonify({'error': 'No file uploaded'}), 400  # Handle missing file

if __name__ == '__main__':
  app.run()