# SmartCrop - Quick Start Guide

Get up and running in 5 minutes! 🚀

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## ⚡ Quick Setup (Windows PowerShell)

### Step 1: Navigate to Project
```powershell
cd "c:\Users\HP\Desktop\SmartCrop"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```powershell
python -m venv venv
venv\Scripts\Activate
```

### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Pandas (data processing)
- NumPy (numerical computing)
- Scikit-learn (machine learning)

### Step 4: Train the ML Model
```powershell
python train_model.py
```

**Expected Output:**
```
Loading dataset...
Dataset shape: (4920, 132)
Training Random Forest model...
Model Performance:
Training Accuracy: 0.9850
Testing Accuracy: 0.9732
✓ Model and features saved successfully!
```

### Step 5: Run the Application
```powershell
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

### Step 6: Open in Browser
Open any web browser and go to:
```
http://localhost:5000
```

## 🎯 Using the Application

1. **Select Symptoms** - Click on symptoms you're experiencing
2. **Click "Analyze Symptoms"** - Get instant AI prediction
3. **View Results** - See confidence score, probability, and chart
4. **Read Recommendations** - Get health tips and guidance
5. **Explore More** - Check Health Tips and About pages

## 🛑 Stopping the Application

Press `CTRL+C` in the terminal to stop the Flask server.

## ❌ Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
**Solution:** Install requirements again
```powershell
pip install -r requirements.txt
```

### "Model not loaded" Error
**Solution:** Train the model first
```powershell
python train_model.py
```

### Port 5000 Already in Use
**Solution:** Change the port in `app.py` (line: `app.run(... port=5000)`) to another port like 5001

### Can't find Testing.csv
**Ensure** Testing.csv is in the `c:\Users\HP\Desktop\SmartCrop\` directory

## 📁 What Each File Does

| File | Purpose |
|------|---------|
| `app.py` | Main Flask web application |
| `train_model.py` | ML model training script |
| `Testing.csv` | Medical dataset (131 symptoms) |
| `templates/index.html` | Main prediction page |
| `templates/about.html` | About the application |
| `templates/health_tips.html` | Health prevention tips |
| `static/style.css` | Beautiful styling (colors, animations) |
| `static/script.js` | Frontend interactivity |
| `models/diabetes_model.pkl` | Trained ML model (auto-generated) |
| `requirements.txt` | Python dependencies list |
| `README.md` | Complete documentation |

## 🎨 Features Overview

✨ **Beautiful Interface** - Modern gradient design with animations
📊 **Real-time Chart** - Visual probability distribution
🔒 **Privacy** - All data processed locally
⚡ **Fast** - Sub-second predictions
📱 **Mobile Ready** - Works on all devices
🏥 **Health Tips** - Prevention guidelines included
🤖 **AI Powered** - 97%+ accuracy predictions

## 📊 Example Prediction

**Input Symptoms:**
- Fatigue
- Weight Loss
- Increased Appetite
- Irregular Sugar Level

**Output:**
```
Prediction: Diabetes
Confidence: 87.50%
Diabetes Probability: 87.50%
Healthy Probability: 12.50%
Message: ⚠️ High risk detected. Consult a doctor.
```

## 🔄 Update or Retrain Model

To retrain the model with new data:

1. Replace `Testing.csv` with your data
2. Run: `python train_model.py`
3. Restart the app: `python app.py`

## 📚 More Information

- Full Documentation: Read `README.md`
- API Endpoints: See section in `README.md`
- ML Model Details: See `train_model.py`

## ⚕️ Important Reminder

⚠️ **This is NOT medical advice!** Always consult with a healthcare professional.

---

**All set! Enjoy using SmartCrop! 🎉**

Need help? Check `README.md` for detailed documentation.
