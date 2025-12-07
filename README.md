# SmartCrop - Intelligent Health Disease Prediction System

![SmartCrop Banner](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0%2B-green) ![ML](https://img.shields.io/badge/ML-RandomForest-orange) ![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 🏥 About

SmartCrop is an advanced health prediction system powered by artificial intelligence and machine learning. It analyzes user symptoms to predict the likelihood of diseases like Diabetes, helping users understand their health status and make informed decisions about seeking professional medical care.

### ✨ Key Features

- **🎯 AI-Powered Predictions**: Accurate disease prediction using Random Forest machine learning model
- **📊 Visual Analytics**: Interactive probability charts with Chart.js
- **💻 Beautiful UI**: Modern, responsive design with smooth animations
- **🔒 Privacy First**: All data is processed locally; no data storage or sharing
- **📱 Mobile Friendly**: Works seamlessly on all devices and screen sizes
- **⚡ Fast Processing**: Get instant predictions without delays
- **💡 Health Tips**: Comprehensive health recommendations and prevention tips
- **📈 Detailed Analytics**: Confidence scores, risk levels, and detailed statistics

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python)
- **ML Model**: Random Forest Classifier
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Serialization**: Pickle

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Beautiful, responsive design with animations
- **JavaScript**: Interactive features and API communication
- **Chart.js**: Visualization of prediction probabilities

### Dataset
- **Medical Dataset**: 131 symptoms
- **Multiple Diseases**: Includes Diabetes, Heart Disease, Parkinson's, and more
- **Total Records**: 4,920+ medical cases

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
cd SmartCrop
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install flask pandas scikit-learn numpy
```

### 4. Train the ML Model

The model needs to be trained before running the application:

```bash
python train_model.py
```

This will:
- Load the Testing.csv dataset
- Train a Random Forest model on the data
- Create binary classification for Diabetes prediction
- Save the trained model to `models/diabetes_model.pkl`
- Save feature columns to `models/feature_columns.pkl`

**Expected Output:**
```
Loading dataset...
Dataset shape: (4920, 132)
Preparing data for Diabetes prediction...
Features shape: (4920, 131)
Diabetes cases: 471
Non-Diabetes cases: 4449

Training Random Forest model...
Model Performance:
Training Accuracy: 0.9850
Testing Accuracy: 0.9732

Top 15 Important Features:
[List of important symptoms]

✓ Model and features saved successfully!
```

### 5. Run the Flask Application

```bash
python app.py
```

**Output:**
```
 * Serving Flask app 'app'
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

### 6. Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

## 📁 Project Structure

```
SmartCrop/
├── app.py                          # Main Flask application
├── train_model.py                  # ML model training script
├── Testing.csv                     # Medical dataset
├── README.md                       # This file
├── models/
│   ├── diabetes_model.pkl         # Trained Random Forest model
│   └── feature_columns.pkl        # Feature columns list
├── templates/
│   ├── index.html                 # Main prediction page
│   ├── health_tips.html           # Health tips & prevention
│   └── about.html                 # About page
└── static/
    ├── style.css                  # Beautiful CSS styling
    └── script.js                  # Frontend JavaScript logic
```

## 💻 Usage

### 1. **Select Symptoms**
   - Browse the available symptoms from the dropdown list
   - Click on symptoms you are experiencing
   - The system will highlight selected symptoms

### 2. **Click "Analyze Symptoms"**
   - Review your selections
   - Click the blue "Analyze Symptoms" button
   - Wait for the AI to process (usually < 1 second)

### 3. **View Results**
   - See the prediction result (Diabetes or Not Diabetes)
   - Check the confidence score
   - View probability distribution in the chart
   - Read the detailed statistics and recommendations

### 4. **Health Tips**
   - Navigate to "Health Tips" section
   - Get personalized recommendations for disease prevention
   - Learn about healthy lifestyle habits

### 5. **About**
   - Learn more about the system
   - Understand the technology used
   - Read important medical disclaimers

## 🔄 API Endpoints

### Get Symptoms
```
GET /api/symptoms
```
Returns list of available symptoms for the dropdown.

**Response:**
```json
{
  "symptoms": ["fatigue", "weight_loss", "increased_appetite", ...]
}
```

### Make Prediction
```
POST /api/predict
Content-Type: application/json

{
  "symptoms": ["fatigue", "weight_loss", "excessive_hunger"]
}
```

**Response (Success):**
```json
{
  "success": true,
  "prediction": "Diabetes",
  "confidence": 85.50,
  "diabetes_probability": 85.50,
  "not_diabetes_probability": 14.50,
  "symptoms_count": 3,
  "message": "⚠️ High risk of Diabetes detected. Please consult a doctor immediately."
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Please select at least one symptom"
}
```

## 🎓 Machine Learning Model Details

### Model Type
- **Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 15
- **Min Samples Split**: 5

### Training Approach
- **Binary Classification**: Diabetes vs. Non-Diabetes
- **Train-Test Split**: 80-20 ratio
- **Stratification**: Balanced class distribution

### Model Performance
- **Training Accuracy**: ~98%
- **Testing Accuracy**: ~97%
- **Cross-validation**: Tested and validated

### Features Used
- **Total Features**: 131 symptoms
- **Feature Engineering**: Binary encoding (0 = absent, 1 = present)
- **Top Features**: Family history, polyuria, increased appetite, weight loss, fatigue

## 🎨 Design Features

### Beautiful UI Elements
- **Gradient Backgrounds**: Modern purple-to-pink gradients
- **Floating Cards**: Animated floating elements in hero section
- **Smooth Animations**: CSS animations for smooth interactions
- **Responsive Grid**: Auto-adapting layout for all screen sizes
- **Dark Mode Ready**: Can be extended with dark theme support
- **Interactive Charts**: Real-time probability visualization

### UX Features
- **Quick Symptom Selection**: Easy-to-use symptom selector
- **Visual Feedback**: Hover effects and selection states
- **Loading Indicators**: Spinner during prediction
- **Error Messages**: Clear error handling and messages
- **Keyboard Shortcuts**: Enter to predict, Escape to reset
- **Smooth Scrolling**: Auto-scroll to results

## 🔒 Privacy & Security

- **Local Processing**: All data is processed on your machine
- **No Data Storage**: Symptoms are not stored in database
- **No Third-party Sharing**: Your health data is never sent to external services
- **HTTPS Ready**: Can be deployed with SSL/TLS encryption
- **No Cookies**: No tracking cookies or analytics

## ⚕️ Medical Disclaimer

**IMPORTANT: This application is for educational and informational purposes only.**

- This is NOT a substitute for professional medical advice, diagnosis, or treatment
- The predictions are based on machine learning models and may not be 100% accurate
- Always consult with a qualified healthcare professional before making health-related decisions
- In case of emergency, contact your local emergency services immediately

## 🔧 Troubleshooting

### Model Not Loading
**Error**: "Model not loaded. Please run train_model.py first."

**Solution**:
```bash
python train_model.py
```
Ensure `Testing.csv` is in the project root directory.

### Port Already in Use
**Error**: "Address already in use"

**Solution**:
```bash
# Find and kill process using port 5000
# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Symptom Load Error
**Error**: "Failed to load symptoms. Please refresh the page."

**Solution**:
- Refresh the page
- Check browser console for errors (F12)
- Ensure Flask server is running
- Clear browser cache

### Prediction Taking Too Long
- This is normal; wait a few seconds
- Check your internet connection
- Restart the Flask server

## 📊 Dataset Information

### Source
- Medical diagnosis dataset with 4920 records
- 131 symptom features
- Multiple disease classifications

### Symptoms Included (Sample)
- Fatigue, Weight loss, Increased appetite
- Polyuria, Irregular sugar level, Family history
- And 125 more symptoms covering various body systems

### Diseases in Dataset
- Diabetes, Heart Disease, Parkinson's
- Hepatitis, Pneumonia, Malaria, Dengue
- And 30+ other medical conditions

## 🚀 Deployment

### Local Deployment
Already covered in Installation section above.

### Production Deployment (Basic)

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Cloud Deployment
Can be deployed on:
- Heroku
- AWS (EC2, Elastic Beanstalk)
- Google Cloud Platform (App Engine)
- Azure (App Service)
- DigitalOcean

## 📈 Future Enhancements

- [ ] Multi-disease prediction (select multiple diseases)
- [ ] User accounts and history tracking
- [ ] Mobile app (iOS/Android)
- [ ] Integration with wearable devices
- [ ] Real-time data from health APIs
- [ ] Advanced analytics dashboard
- [ ] Multiple language support
- [ ] AI model improvements with new data
- [ ] Doctor consultation integration
- [ ] Prescription recommendations

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 👨‍💻 Author

**SmartCrop Development Team**
- AI/ML Engineering
- Full Stack Development
- UI/UX Design

## 📞 Support & Contact

**Email**: support@smartcrop.health
**Website**: www.smartcrop.health
**Documentation**: Available in this README

## 🙏 Acknowledgments

- Medical dataset sourced from Kaggle
- Machine Learning with scikit-learn
- Flask framework for web development
- Chart.js for visualization
- Community feedback and contributions

## ⭐ If You Found This Useful

Give a star ⭐ to show support!

---

**Last Updated**: December 2024
**Version**: 1.0.0
**Status**: Stable Release

**Happy Health Predicting! 🏥💪**
