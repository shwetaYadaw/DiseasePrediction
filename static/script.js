// SmartCrop - JavaScript for Health Prediction
// Handles all client-side logic and interactivity

let chartInstance = null;
let selectedSymptoms = [];

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    loadSymptoms();
});

/**
 * Load symptoms from backend and populate the UI
 */
async function loadSymptoms() {
    try {
        const response = await fetch('/api/symptoms');
        const data = await response.json();
        
        if (data.symptoms) {
            selectedSymptoms = [];
            populateSymptomsGrid(data.symptoms);
        }
    } catch (error) {
        console.error('Error loading symptoms:', error);
        showError('Failed to load symptoms. Please refresh the page.');
    }
}

/**
 * Populate the symptoms grid with checkboxes
 */
function populateSymptomsGrid(symptoms) {
    const grid = document.getElementById('symptomsGrid');
    grid.innerHTML = '';
    
    symptoms.forEach(symptom => {
        const id = 'symptom_' + symptom;
        const label = formatSymptomName(symptom);
        
        const wrapper = document.createElement('div');
        wrapper.innerHTML = `
            <input 
                type="checkbox" 
                id="${id}" 
                class="symptom-checkbox" 
                value="${symptom}"
                onchange="updateSymptomSelection()"
            />
            <label for="${id}" class="symptom-label">
                <span class="checkbox-custom">✓</span>
                <span>${label}</span>
            </label>
        `;
        
        grid.appendChild(wrapper.firstElementChild);
        grid.appendChild(wrapper.querySelector('label'));
    });
}

/**
 * Update selected symptoms and count
 */
function updateSymptomSelection() {
    const checkboxes = document.querySelectorAll('.symptom-checkbox:checked');
    selectedSymptoms = Array.from(checkboxes).map(cb => cb.value);
    
    const count = selectedSymptoms.length;
    document.getElementById('symptomCount').textContent = count;
    
    // Enable/disable predict button
    const predictBtn = document.getElementById('predictBtn');
    predictBtn.disabled = count === 0;
}

/**
 * Format symptom names for display (replace underscores with spaces, capitalize)
 */
function formatSymptomName(symptom) {
    return symptom
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

/**
 * Make prediction by sending selected symptoms to backend
 */
async function makePrediction() {
    if (selectedSymptoms.length === 0) {
        showError('Please select at least one symptom');
        return;
    }
    
    // Show loading spinner
    const spinner = document.getElementById('loadingSpinner');
    spinner.classList.add('active');
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ symptoms: selectedSymptoms })
        });
        
        const data = await response.json();
        spinner.classList.remove('active');
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(data.error || 'Prediction failed. Please try again.');
        }
    } catch (error) {
        spinner.classList.remove('active');
        console.error('Prediction error:', error);
        showError('An error occurred. Please try again.');
    }
}

/**
 * Display prediction results
 */
function displayResults(data) {
    const resultCard = document.getElementById('resultCard');
    
    // Update prediction box
    const predictionBox = document.getElementById('predictionBox');
    const riskClass = getRiskClass(data.confidence);
    
    predictionBox.innerHTML = `
        <div class="prediction-text">Prediction Result</div>
        <div class="prediction-risk ${riskClass}">${data.prediction}</div>
        <div style="margin-top: 0.5rem; color: var(--text-secondary); font-size: 0.95rem;">
            Risk Level: ${getRiskLevel(data.confidence)}
        </div>
    `;
    
    // Update stats
    document.getElementById('diabetesProb').textContent = data.diabetes_probability.toFixed(1) + '%';
    document.getElementById('healthyProb').textContent = data.not_diabetes_probability.toFixed(1) + '%';
    document.getElementById('confidenceScore').textContent = data.confidence.toFixed(1) + '%';
    document.getElementById('symptomsAnalyzed').textContent = data.symptoms_count;
    
    // Update health message
    const messageDiv = document.getElementById('healthMessage');
    messageDiv.textContent = data.message;
    messageDiv.className = 'health-message ' + getMessageClass(data.prediction);
    
    // Update chart
    updateChart(data.diabetes_probability, data.not_diabetes_probability);
    
    // Show result card with animation
    resultCard.style.display = 'block';
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Get CSS class based on risk level
 */
function getRiskClass(confidence) {
    if (confidence > 75) return 'risk-high';
    if (confidence > 50) return 'risk-moderate';
    return 'risk-low';
}

/**
 * Get risk level text
 */
function getRiskLevel(confidence) {
    if (confidence > 75) return '🔴 High Risk';
    if (confidence > 50) return '🟡 Moderate Risk';
    return '🟢 Low Risk';
}

/**
 * Get message CSS class
 */
function getMessageClass(prediction) {
    if (prediction === 'Diabetes') return 'danger';
    return 'success';
}

/**
 * Update or create the prediction probability chart
 */
function updateChart(diabetesProb, healthyProb) {
    const ctx = document.getElementById('predictionChart').getContext('2d');
    
    // Destroy existing chart
    if (chartInstance) {
        chartInstance.destroy();
    }
    
    // Create new chart
    chartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Diabetes Risk', 'Healthy Probability'],
            datasets: [{
                data: [diabetesProb, healthyProb],
                backgroundColor: [
                    'rgba(239, 68, 68, 0.8)',
                    'rgba(16, 185, 129, 0.8)'
                ],
                borderColor: [
                    'rgb(239, 68, 68)',
                    'rgb(16, 185, 129)'
                ],
                borderWidth: 2,
                borderRadius: 8,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 13,
                            weight: '500'
                        },
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed + '%';
                        }
                    },
                    padding: 12,
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleFont: { size: 13, weight: 'bold' },
                    bodyFont: { size: 12 }
                }
            }
        }
    });
}

/**
 * Reset the form and clear results
 */
function resetForm() {
    // Uncheck all checkboxes
    document.querySelectorAll('.symptom-checkbox').forEach(cb => {
        cb.checked = false;
    });
    
    selectedSymptoms = [];
    document.getElementById('symptomCount').textContent = '0';
    
    // Hide results
    document.getElementById('resultCard').style.display = 'none';
    
    // Destroy chart
    if (chartInstance) {
        chartInstance.destroy();
        chartInstance = null;
    }
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Show error message
 */
function showError(message) {
    alert(message);
}

/**
 * Keyboard shortcuts
 */
document.addEventListener('keydown', function(event) {
    // Press Enter to predict
    if (event.key === 'Enter' && selectedSymptoms.length > 0) {
        makePrediction();
    }
    
    // Press Escape to reset
    if (event.key === 'Escape') {
        resetForm();
    }
});

// Smooth scroll for navigation
document.querySelectorAll('a[href^="/"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.startsWith('/') && !href.includes('#')) {
            // Let browser handle navigation for actual pages
            return;
        }
        
        if (href.includes('#')) {
            e.preventDefault();
            const target = document.querySelector(href.substring(href.indexOf('#')));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});
