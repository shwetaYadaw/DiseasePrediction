# SmartCrop Configuration Guide

## Environment Variables (Optional)

You can customize the application by setting these environment variables:

### Flask Configuration

```powershell
# Set Flask environment
$env:FLASK_ENV = "development"  # or "production"

# Set Flask app
$env:FLASK_APP = "app.py"

# Debug mode (development only!)
$env:FLASK_DEBUG = "1"  # 0 to disable
```

### Port Configuration

In `app.py`, modify the last line:

```python
# Current (port 5000)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Change port to 5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
```

## Project Structure Explanation

```
SmartCrop/
│
├── 📄 app.py                          # Main Flask application
│   ├── Loads trained model
│   ├── Defines API endpoints
│   ├── Handles predictions
│   └── Returns results as JSON
│
├── 📄 train_model.py                  # Model training script
│   ├── Loads Testing.csv
│   ├── Prepares data
│   ├── Trains Random Forest
│   └── Saves model to pickle
│
├── 📄 Testing.csv                     # Medical dataset
│   ├── 4920 rows (medical cases)
│   ├── 131 symptoms (features)
│   └── Disease labels (prognosis)
│
├── 📁 templates/                      # HTML templates
│   ├── index.html      (Main page with prediction form)
│   ├── about.html      (Application information)
│   └── health_tips.html (Prevention guidelines)
│
├── 📁 static/                         # Frontend assets
│   ├── style.css   (Beautiful styling & animations)
│   └── script.js   (Interactive features)
│
├── 📁 models/                         # Trained models (auto-created)
│   ├── diabetes_model.pkl      (Trained RF classifier)
│   └── feature_columns.pkl     (Symptom list)
│
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Complete documentation
├── 📄 QUICKSTART.md                   # Quick setup guide
├── 📄 setup_check.py                  # Environment verification
└── 📄 config_guide.md                 # This file
```

## File Dependencies

```
app.py (Flask app)
  ├── Requires: models/diabetes_model.pkl
  ├── Requires: models/feature_columns.pkl
  ├── Requires: templates/index.html
  ├── Requires: templates/about.html
  ├── Requires: templates/health_tips.html
  ├── Requires: static/style.css
  └── Requires: static/script.js

train_model.py (Model training)
  ├── Requires: Testing.csv
  └── Generates: models/diabetes_model.pkl
                 models/feature_columns.pkl
```

## Custom Modifications

### Change Disease Being Predicted

Currently predicting: **Diabetes**

To predict a different disease, modify `train_model.py`:

```python
# Line ~28: Change the disease
y = (df['prognosis'] == 'Diabetes ').astype(int)

# To:
y = (df['prognosis'] == 'Heart Disease').astype(int)
# or
y = (df['prognosis'] == "Parkinson's").astype(int)
```

### Change Application Name

Update these files:
1. `templates/index.html` - Change title and logo
2. `templates/about.html` - Update project name
3. `templates/health_tips.html` - Update branding
4. `static/style.css` - Update colors if desired

### Add Custom Styling

Edit `static/style.css`:
- Change colors: Modify `:root` CSS variables
- Adjust spacing: Modify `padding` and `margin` values
- Change fonts: Modify `font-family` property

### Modify Symptoms to Display

In `app.py`, the `DIABETES_SYMPTOMS` list contains the displayed symptoms:

```python
DIABETES_SYMPTOMS = [
    'fatigue', 'weight_loss', 'increased_appetite', 
    # Add or remove symptoms here
]
```

## Database Integration (Future)

To add database support for user history:

```python
# Install Flask-SQLAlchemy
pip install Flask-SQLAlchemy

# Modify app.py
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
db = SQLAlchemy(app)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptoms = db.Column(db.String(500))
    result = db.Column(db.String(100))
    confidence = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
```

## Performance Optimization

### 1. Model Loading Optimization
```python
# In app.py, add caching
from functools import lru_cache

@lru_cache(maxsize=1)
def load_model():
    # Load model once and cache
    pass
```

### 2. Frontend Optimization
- Minify CSS: `style.css`
- Minify JavaScript: `script.js`
- Compress images: Add favicon/logo

### 3. Server Optimization
```powershell
# Use production server (Gunicorn)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Security Considerations

### 1. Input Validation
Currently handled by Flask - symptoms must be from predefined list.

### 2. CORS (If needed)
```python
from flask_cors import CORS
CORS(app)
```

### 3. Rate Limiting (Recommended)
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/predict', methods=['POST'])
@limiter.limit("100 per hour")
def predict():
    # Your code
```

### 4. HTTPS (Production)
Use SSL/TLS certificate when deploying.

## Monitoring & Logging

Add logging for production:

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    logger.info('Prediction request received')
    # Your code
```

## Testing

Run setup check:
```powershell
python setup_check.py
```

Manual testing:
1. Open http://localhost:5000
2. Select multiple symptoms
3. Click "Analyze Symptoms"
4. Verify prediction displays correctly
5. Check confidence score and chart

## Troubleshooting Checklist

- [ ] Python version 3.8+
- [ ] All dependencies installed
- [ ] Model trained successfully
- [ ] Testing.csv exists in root
- [ ] All HTML templates present
- [ ] CSS and JS files in static/
- [ ] Port 5000 not in use
- [ ] No firewall blocking port 5000

## Deployment Checklist

- [ ] Test locally first
- [ ] Set `debug=False` for production
- [ ] Use environment variables for secrets
- [ ] Set up logging
- [ ] Use production WSGI server
- [ ] Configure HTTPS/SSL
- [ ] Set up monitoring and alerts
- [ ] Plan backup strategy
- [ ] Document API changes
- [ ] Create deployment guide

---

**Questions?** Check `README.md` for comprehensive documentation.
