from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

# Global variables for loaded models
model = None
scaler = None
encoders = None
imputers = None

def load_artifacts():
    """Load all pickle artifacts"""
    global model, scaler, encoders, imputers
    
    try:
        # Load trained model
        with open('Rainfall.pkl', 'rb') as f:
            model = pickle.load(f)
        
        # Load scaler
        with open('scale.pkl', 'rb') as f:
            scaler = pickle.load(f)
        
        # Load encoders
        with open('encoder.pkl', 'rb') as f:
            encoders = pickle.load(f)
        
        # Load imputers
        with open('imputer.pkl', 'rb') as f:
            imputers = pickle.load(f)
        
        print("All artifacts loaded successfully!")
        return True
    
    except FileNotFoundError as e:
        print(f"Error: Missing pickle file - {e}")
        print("Please run the Jupyter notebook first to generate model artifacts.")
        return False
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        return False

@app.route('/')
def index():
    """Render home page with input form"""
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error rendering page: {str(e)}", 500

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction request"""
    try:
        # Load artifacts if not already loaded
        if model is None:
            if not load_artifacts():
                return "Error: Model artifacts not found. Please run Jupyter notebook first.", 500
        
        # Extract form data and create DataFrame with exact column order from training
        # The model expects these 21 features in this exact order
        input_data = pd.DataFrame({
            'Location': [request.form.get('Location')],
            'MinTemp': [float(request.form.get('MinTemp'))],
            'MaxTemp': [float(request.form.get('MaxTemp'))],
            'Rainfall': [float(request.form.get('Rainfall'))],
            'Evaporation': [float(request.form.get('Evaporation'))],
            'Sunshine': [float(request.form.get('Sunshine'))],
            'WindGustDir': [request.form.get('WindGustDir')],
            'WindGustSpeed': [float(request.form.get('WindGustSpeed'))],
            'WindDir9am': [request.form.get('WindDir9am')],
            'WindDir3pm': [request.form.get('WindDir3pm')],
            'WindSpeed9am': [float(request.form.get('WindSpeed9am'))],
            'WindSpeed3pm': [float(request.form.get('WindSpeed3pm'))],
            'Humidity9am': [float(request.form.get('Humidity9am'))],
            'Humidity3pm': [float(request.form.get('Humidity3pm'))],
            'Pressure9am': [float(request.form.get('Pressure9am'))],
            'Pressure3pm': [float(request.form.get('Pressure3pm'))],
            'Cloud9am': [float(request.form.get('Cloud9am'))],
            'Cloud3pm': [float(request.form.get('Cloud3pm'))],
            'Temp9am': [float(request.form.get('Temp9am'))],
            'Temp3pm': [float(request.form.get('Temp3pm'))],
            'RainToday': [request.form.get('RainToday')]
        })
        
        # Preprocessing pipeline (must match training exactly):
        # 1. Encode categorical features
        categorical_cols = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']
        
        if encoders and 'features' in encoders:
            for col in categorical_cols:
                if col in encoders['features']:
                    try:
                        input_data[col] = encoders['features'][col].transform(input_data[col])
                    except ValueError as e:
                        # Handle unseen categories - use mode/most common value
                        print(f"Warning: Unseen category '{input_data[col].values[0]}' in {col}")
                        # Get the first class from the encoder as fallback
                        input_data[col] = 0
        
        # 2. Ensure column order matches training (critical for sklearn models)
        expected_columns = ['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 
                          'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 
                          'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 
                          'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 
                          'Cloud3pm', 'Temp9am', 'Temp3pm', 'RainToday']
        input_data = input_data[expected_columns]
        
        # 3. Scale features (scaler expects all numerical values after encoding)
        if scaler:
            input_scaled = scaler.transform(input_data)
        else:
            input_scaled = input_data.values
        
        # 4. Make prediction
        prediction = model.predict(input_scaled)[0]
        
        print(f"Prediction: {prediction}")
        
        # Render result page based on prediction
        if prediction == 1:
            return render_template('chance.html')
        else:
            return render_template('noChance.html')
    
    except ValueError as e:
        return f"Error: Invalid input values - {str(e)}", 400
    except KeyError as e:
        return f"Error: Missing required field - {str(e)}", 400
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error during prediction: {str(e)}", 500

if __name__ == '__main__':
    # Check if model artifacts exist
    required_files = ['Rainfall.pkl', 'scale.pkl', 'encoder.pkl', 'imputer.pkl']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("Warning: Missing model artifacts:")
        for f in missing_files:
            print(f"  - {f}")
        print("\nPlease run the Jupyter notebook (Rainfall_prediction.ipynb) first to generate these files.")
    else:
        load_artifacts()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
