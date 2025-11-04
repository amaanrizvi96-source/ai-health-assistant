from flask import Flask, render_template, request

app = Flask(__name__)

# Simple symptom-based knowledge base
disease_data = {
    "fever": {
        "disease": "Common Cold or Viral Fever",
        "description": "A fever is a temporary increase in body temperature, often due to an infection.",
        "precautions": [
            "Drink plenty of fluids.",
            "Take rest and avoid exertion.",
            "Take paracetamol for high fever.",
            "Consult a doctor if fever lasts more than 3 days."
        ]
    },
    "cough": {
        "disease": "Respiratory Infection or Allergic Cough",
        "description": "Coughing helps clear your airways but persistent coughs may indicate infection.",
        "precautions": [
            "Drink warm fluids and honey with ginger.",
            "Avoid cold or dusty environments.",
            "Use cough syrup if necessary.",
            "Consult a doctor if cough persists for more than 2 weeks."
        ]
    },
    "headache": {
        "disease": "Migraine or Tension Headache",
        "description": "A headache can be caused by stress, dehydration, or eye strain.",
        "precautions": [
            "Get enough rest and sleep.",
            "Stay hydrated and avoid bright lights.",
            "Avoid skipping meals.",
            "Seek medical advice if headache is severe or frequent."
        ]
    },
    "stomach pain": {
        "disease": "Indigestion or Gastric Infection",
        "description": "Pain in the abdomen may occur due to digestive issues or infection.",
        "precautions": [
            "Avoid spicy and oily food.",
            "Drink clean water and stay hydrated.",
            "Eat light meals.",
            "Consult a doctor if pain is severe or persistent."
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.get('symptoms', '').lower()

    result = None
    for key in disease_data:
        if key in symptoms:
            result = disease_data[key]
            break

    if result:
        message = "🤖 Take care of yourself! Here’s what we found:"
        greeting = "🌿 Stay healthy and get well soon!"
        return render_template(
            'index.html',
            symptoms=symptoms,
            disease=result['disease'],
            description=result['description'],
            precautions=result['precautions'],
            message=message,
            greeting=greeting
        )
    else:
        return render_template(
            'index.html',
            symptoms=symptoms,
            disease="Unknown Condition",
            description="Sorry, we could not identify the issue. Please consult a doctor.",
            precautions=["Drink water", "Take rest", "Consult a healthcare provider."],
            message="🤖 I couldn’t recognize the symptoms.",
            greeting="Please stay safe and consult a doctor!"
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
