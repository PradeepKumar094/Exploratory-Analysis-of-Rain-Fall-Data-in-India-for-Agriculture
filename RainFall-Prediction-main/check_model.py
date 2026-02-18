import pickle
import pandas as pd

# Check what's in the encoder file
try:
    with open('encoder.pkl', 'rb') as f:
        encoders = pickle.load(f)
    print("Encoder structure:")
    print(f"Keys: {encoders.keys()}")
    if 'features' in encoders:
        print(f"Feature encoders: {list(encoders['features'].keys())}")
except Exception as e:
    print(f"Error loading encoder: {e}")

# Check scaler
try:
    with open('scale.pkl', 'rb') as f:
        scaler = pickle.load(f)
    print(f"\nScaler feature names: {scaler.feature_names_in_ if hasattr(scaler, 'feature_names_in_') else 'Not available'}")
    print(f"Scaler n_features: {scaler.n_features_in_ if hasattr(scaler, 'n_features_in_') else 'Not available'}")
except Exception as e:
    print(f"Error loading scaler: {e}")

# Check model
try:
    with open('Rainfall.pkl', 'rb') as f:
        model = pickle.load(f)
    print(f"\nModel type: {type(model)}")
    print(f"Model feature names: {model.feature_names_in_ if hasattr(model, 'feature_names_in_') else 'Not available'}")
except Exception as e:
    print(f"Error loading model: {e}")
