# InSight: Medical Imaging Analysis System

InSight is a comprehensive medical imaging analysis system designed to analyze chest X-rays, MRI images for tumor detection, and dementia prediction. It employs various deep learning models to accurately diagnose medical conditions and generate detailed medical reports.

## Features

- **Dementia Prediction**: Utilizes a self-trained model to predict dementia severity levels (no dementia, very mild, mild, moderate).
- **Chest X-ray Analysis**: Utilizes a DenseNet model from the `torchxrayvision` library to classify 14 different lung diseases accurately.
- **Tumor Detection**: Employs YOLOv3-tiny for brain tumor detection in MRI images.
- **Medical Report Generation**: Generates detailed medical reports based on the analysis results.
- **API Integration with Gemini AI**: Connects with Gemini AI through API for report generation from analysis result and provide with cross-checking suggestions 
  for radiologist.
-**Report Lab**:ReportLab dynamically generates detailed medical reports based on the analysis results obtained

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/InSight.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    npm install  #using React.js for frontend
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Access the application at [http://localhost:5000](http://localhost:5000).

3. Upload medical images for analysis and view the generated medical reports.

## API Usage

- **Endpoint**: `/api/analyze`
- **Method**: POST
- **Request Body**: JSON object containing the medical image data.
- **Response**: JSON object containing the analysis results and medical report.

Example request:

```json
{
  "image": "base64_encoded_image_data"
}
```

## Contributing
Contributions are welcome! Please read the contribution guidelines before making any changes.

## License
This project is licensed under the MIT License.

## Acknowledgements

- [torchxrayvision](https://github.com/mlmed/torchxrayvision)
- [YOLOv3-tiny](https://github.com/AlexeyAB/darknet)
- [Gemini AI](https://gemini.google.com/app/)
- [ReportLab](https://www.reportlab.com/)

