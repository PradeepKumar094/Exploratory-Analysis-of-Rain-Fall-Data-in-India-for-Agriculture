# 🌧️ Rainfall Prediction System for Indian Agriculture

A machine learning-powered web application that predicts rainfall patterns to support agricultural decision-making in India. This system helps farmers and agricultural planners make informed decisions about crop planning, irrigation management, and harvesting schedules.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![ML](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Screenshots](#screenshots)
- [Documentation](#documentation)
- [Video Demo](#video-demo)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

Agriculture in India heavily depends on rainfall patterns. Unpredictable weather conditions lead to poor crop selection, inefficient water management, and financial losses. This project addresses these challenges by providing:

- **Accurate Predictions**: ML model with 87.5% accuracy
- **User-Friendly Interface**: Intuitive web-based input form
- **Real-Time Results**: Instant rainfall predictions
- **Visual Feedback**: Immersive result pages with animations
- **Agricultural Support**: Data-driven decision making for farmers

## ✨ Features

### Core Functionality
- 🔮 **Rainfall Prediction**: Predicts next-day rainfall based on 21 meteorological parameters
- 📊 **Multiple ML Models**: Trained and evaluated Random Forest, XGBoost, Decision Tree, and KNN
- 🎨 **Beautiful UI**: Responsive design with full-screen result pages
- ⚡ **Fast Response**: Predictions in under 3 seconds
- 🌐 **Web-Based**: Accessible from any modern browser

### Technical Features
- Data preprocessing pipeline (encoding, scaling, imputation)
- Model serialization for production deployment
- Input validation and error handling
- Responsive grid layout for input form
- Animated visual effects on result pages

## 📁 Repository Structure

```
rainfall-prediction-india/
│
├── 📂 documents/                    # Complete project documentation
│   ├── 1_Ideation_Phase.pdf
│   ├── 2_Requirement_Analysis.pdf
│   ├── 3_Project_Design_Phase.pdf
│   ├── 4_Project_Planning_Phase.pdf
│   ├── 5_Project_Development_Phase.pdf
│   ├── 6_Project_Documentation.pdf
│   └── 7_Project_Demonstration.pdf
│
├── 📂 project-files/                # Source code and models
│   ├── app.py                       # Flask application
│   ├── requirements.txt             # Python dependencies
│   ├── .gitignore                   # Git ignore rules
│   │
│   ├── 📂 data/
│   │   └── WeatherAUS.csv          # Training dataset
│   │
│   ├── 📂 templates/
│   │   ├── index.html              # Input form
│   │   ├── chance.html             # Rain expected page
│   │   └── noChance.html           # No rain page
│   │
│   ├── 📂 static/                   # Static assets (future)
│   │
│   ├── Rainfall_prediction.ipynb   # Model training notebook
│   │
│   ├── Rainfall.pkl                # Trained ML model
│   ├── scale.pkl                   # Feature scaler
│   ├── encoder.pkl                 # Label encoders
│   └── imputer.pkl                 # Missing value imputer
│
├── 📂 video-demo/                   # Project demonstration
│   └── demo.mp4                     # Video walkthrough
│
└── README.md                        # This file
```

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.3.0**: Web framework
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning models
- **XGBoost**: Gradient boosting

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling and animations
- **JavaScript**: Interactive elements

### Data Science
- **Jupyter Notebook**: Model development
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical plots

### Deployment
- **Pickle**: Model serialization
- **Git**: Version control
- **GitHub**: Code hosting

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/rainfall-prediction-india.git
cd rainfall-prediction-india/project-files
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Model Files
Ensure these files exist in the `project-files/` directory:
- ✅ Rainfall.pkl
- ✅ scale.pkl
- ✅ encoder.pkl
- ✅ imputer.pkl

### Step 5: Run Application
```bash
python app.py
```

Access the application at: **http://localhost:5000**

## 📖 Usage

### Making a Prediction

1. **Open the Application**
   - Navigate to `http://localhost:5000` in your browser

2. **Enter Meteorological Data**
   - Fill in all 21 required fields:
     - Location (dropdown)
     - Temperature data (Min, Max, 9am, 3pm)
     - Rainfall and Evaporation
     - Wind data (Direction, Speed, Gusts)
     - Humidity (9am, 3pm)
     - Atmospheric pressure (9am, 3pm)
     - Cloud cover (9am, 3pm)
     - Rain today (Yes/No)

3. **Submit Form**
   - Click "🔮 Predict Rainfall" button

4. **View Results**
   - **Rain Expected**: Rainy scene with animated raindrops
   - **No Rain**: Sunny beach scene

5. **Make Another Prediction**
   - Click "🔄 Check Again" to return to form

### Sample Test Case (Rain Expected)

```
Location: Sydney
Min Temperature: 18.5°C
Max Temperature: 22.3°C
Rainfall: 8.5 mm
Evaporation: 2.4 mm
Sunshine: 3.2 hours
Wind Gust Direction: W
Wind Gust Speed: 44 km/h
Wind Direction 9am: SW
Wind Direction 3pm: W
Wind Speed 9am: 20 km/h
Wind Speed 3pm: 28 km/h
Humidity 9am: 85%
Humidity 3pm: 75%
Pressure 9am: 1008.5 hPa
Pressure 3pm: 1006.2 hPa
Cloud Cover 9am: 7 oktas
Cloud Cover 3pm: 8 oktas
Temperature 9am: 19.5°C
Temperature 3pm: 21.0°C
Rain Today: Yes
```

## 📊 Model Performance

Our machine learning model was trained on the Australian Weather Dataset and evaluated using multiple metrics:

| Metric | Score |
|--------|-------|
| **Accuracy** | 87.5% |
| **Precision** | 85.2% |
| **Recall** | 83.8% |
| **F1-Score** | 84.5% |

### Models Evaluated
- ✅ Random Forest Classifier (Selected)
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

The Random Forest model was selected for production due to its superior performance and reliability.

## 📸 Screenshots

### Input Form
![Input Form](screenshots/input-form.png)
*Clean, responsive input form with organized grid layout*

### Rain Expected Result
![Rain Expected](screenshots/rain-expected.png)
*Immersive rainy scene with animated raindrops*

### No Rain Result
![No Rain](screenshots/no-rain.png)
*Beautiful beach scene indicating clear weather*

## 📚 Documentation

Comprehensive documentation is available in the `documents/` folder:

1. **Ideation Phase** - Problem statement, objectives, and scope
2. **Requirement Analysis** - Functional and non-functional requirements
3. **Project Design Phase** - System architecture and component design
4. **Project Planning Phase** - Timeline, resources, and risk management
5. **Project Development Phase** - Implementation guide with code examples
6. **Project Documentation** - Installation, user manual, and troubleshooting
7. **Project Demonstration** - Demo script and presentation guide

Each document is available in PDF format for easy reference.

## 🎥 Video Demo

A complete video demonstration is available in the `video-demo/` folder, showcasing:
- Application walkthrough
- Live prediction examples
- Feature highlights
- Use case scenarios

**Watch the demo**: [video-demo/demo.mp4](video-demo/demo.mp4)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/YOUR_USERNAME/rainfall-prediction-india.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Commit Changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

4. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Open Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 🐛 Known Issues & Future Enhancements

### Known Issues
- Background images require internet connection
- Limited to 15 Australian locations

### Planned Enhancements
- [ ] Add Indian locations with localized data
- [ ] Multi-day rainfall forecasts
- [ ] Mobile application (iOS/Android)
- [ ] Real-time weather API integration
- [ ] Multi-language support
- [ ] Historical prediction tracking
- [ ] Advanced agricultural recommendations
- [ ] Crop-specific insights
- [ ] SMS/Email notifications
- [ ] API for third-party integration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- Australian Bureau of Meteorology for the weather dataset
- Scikit-learn and XGBoost communities for ML libraries
- Flask community for the web framework
- Open source contributors

## 📞 Contact

**Project Maintainer**: Your Name

- 📧 Email: your.email@example.com
- 🐙 GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- 💼 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🌟 Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📢 Sharing with others

---

**Made with ❤️ for Indian Agriculture**

*Empowering farmers with data-driven decisions*
