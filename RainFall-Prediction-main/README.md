# Rainfall Prediction System for Indian Agriculture

A machine learning application that predicts rainfall patterns to support agricultural decision-making in India.

## Project Overview

This system consists of:
- **Jupyter Notebook** (Rainfall_prediction.ipynb) - Data analysis, visualization, and model training
- **Flask Web Application** (app.py) - User interface for predictions
- **HTML Templates** - Interactive web forms and result pages
- **Trained Models** - Serialized ML models and preprocessing artifacts

## Project Structure

```
.
├── data/                    # Dataset folder (place your CSV file here)
├── templates/               # HTML templates for Flask
├── static/                  # Static files (CSS, images)
├── Rainfall_prediction.ipynb  # Jupyter notebook for model development
├── app.py                   # Flask web application
├── requirements.txt         # Python dependencies
├── Rainfall.pkl            # Trained model (generated)
├── scale.pkl               # Feature scaler (generated)
├── encoder.pkl             # Label encoder (generated)
└── imputer.pkl             # Missing value imputer (generated)
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Dataset

Place your rainfall dataset CSV file in the `data/` folder.

### 3. Run Jupyter Notebook

```bash
jupyter notebook Rainfall_prediction.ipynb
```

Execute all cells to:
- Load and analyze the dataset
- Perform exploratory data analysis
- Train multiple ML models
- Generate pickle files for production

### 4. Start Flask Application

```bash
python app.py
```

Access the web interface at `http://localhost:5000`

## Usage

1. Open the web application in your browser
2. Enter location and meteorological parameters
3. Submit the form to receive rainfall prediction
4. View recommendations based on the prediction

## Models Trained

- Random Forest Classifier
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

The best-performing model is automatically selected and saved for production use.

## Requirements

- Python 3.x
- Anaconda Navigator (recommended)
- See requirements.txt for complete package list
