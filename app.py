"""
Smart Health Disease Prediction Flask Application
Provides REST API for disease prediction based on symptoms
"""

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import json
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the trained model
try:
    with open('models/diabetes_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('models/feature_columns.pkl', 'rb') as f:
        feature_columns = pickle.load(f)
    
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    feature_columns = None

# All available symptoms
SYMPTOMS = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue',
    'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue',
    'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
    'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
    'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
    'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
    'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain',
    'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
    'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
    'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose',
    'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements',
    'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness',
    'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
    'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger',
    'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
    'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
    'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
    'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
    'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
    'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
    'distention_of_abdomen', 'history_of_alcohol_consumption', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
    'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
    'yellow_crust_ooze'
]

# Symptoms related to Diabetes (for better UX)
DIABETES_SYMPTOMS = [
    'fatigue', 'weight_loss', 'increased_appetite', 'polyuria', 'excessive_hunger',
    'irregular_sugar_level', 'family_history', 'weight_gain', 'nausea', 'high_fever',
    'weakness_in_limbs', 'muscle_pain', 'itching', 'visual_disturbances', 'headache',
    'depression', 'lethargy', 'restlessness', 'skin_rash', 'cold_hands_and_feets'
]

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    """Get list of symptoms for dropdown"""
    return jsonify({'symptoms': DIABETES_SYMPTOMS})

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Predict diabetes based on selected symptoms
    Expected JSON: {"symptoms": ["symptom1", "symptom2", ...]}
    """
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please run train_model.py first.'
            }), 500
        
        data = request.get_json()
        selected_symptoms = data.get('symptoms', [])
        
        if not selected_symptoms:
            return jsonify({
                'success': False,
                'error': 'Please select at least one symptom'
            }), 400
        
        # Create input array
        input_array = np.zeros(len(feature_columns))
        
        for symptom in selected_symptoms:
            if symptom in feature_columns:
                idx = feature_columns.index(symptom)
                input_array[idx] = 1
        
        # Make prediction
        prediction = model.predict([input_array])[0]
        probability = model.predict_proba([input_array])[0]
        
        # Get confidence score
        confidence = float(max(probability) * 100)
        
        # Prepare response
        response = {
            'success': True,
            'prediction': 'Diabetes' if prediction == 1 else 'Not Diabetes',
            'confidence': round(confidence, 2),
            'diabetes_probability': round(float(probability[1]) * 100, 2),
            'not_diabetes_probability': round(float(probability[0]) * 100, 2),
            'symptoms_count': len(selected_symptoms),
            'message': get_health_message(prediction, confidence)
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def get_health_message(prediction, confidence):
    """Generate appropriate health message based on prediction"""
    if prediction == 1:  # Diabetes
        if confidence > 80:
            return "⚠️ High risk of Diabetes detected. Please consult a doctor immediately."
        elif confidence > 60:
            return "⚠️ Moderate risk of Diabetes. Consult a healthcare professional."
        else:
            return "✓ Low risk of Diabetes, but monitoring is recommended."
    else:
        if confidence > 80:
            return "✓ Low risk of Diabetes. Maintain a healthy lifestyle!"
        else:
            return "✓ Symptoms suggest low diabetes risk, but medical consultation is advised."

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/health-tips')
def health_tips():
    """Health tips page"""
    return render_template('health_tips.html')

if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
