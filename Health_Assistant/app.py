from flask import Flask, render_template, request

app = Flask(__name__)

# Simple symptom-based knowledge base
disease_data = {
    "Fever": {
        "disease": "Common Cold or Viral Fever",
        "description": "A fever is a temporary increase in body temperature, often due to an infection.",
        "precautions": [
            "Drink plenty of fluids.",
            "Take rest and avoid exertion.",
            "Take paracetamol for high fever.",
            "Consult a doctor if fever lasts more than 3 days."
        ]
    },
    "Cough": {
        "disease": "Respiratory Infection or Allergic Cough",
        "description": "Coughing helps clear your airways but persistent coughs may indicate infection.",
        "precautions": [
            "Drink warm fluids and honey with ginger.",
            "Avoid cold or dusty environments.",
            "Use cough syrup if necessary.",
            "Consult a doctor if cough persists for more than 2 weeks."
        ]
    },
    "Vomiting": {
    "disease": "Food Poisoning or Stomach Infection",
    "description": "Vomiting can occur due to food poisoning, stomach infection, dehydration, or digestive problems.",
    "precautions": [
        "Drink small amounts of clean water frequently.",
        "Avoid oily, spicy, and heavy foods.",
        "Eat light foods like rice, toast, or bananas.",
        "Take oral rehydration solution (ORS) if needed.",
        "Consult a doctor if vomiting continues for more than 24 hours."
    ]
},
    "Headache": {
        "disease": "Migraine or Tension Headache",
        "description": "A headache can be caused by stress, dehydration, or eye strain.",
        "precautions": [
            "Get enough rest and sleep.",
            "Stay hydrated and avoid bright lights.",
            "Avoid skipping meals.",
            "Seek medical advice if headache is severe or frequent."
        ]
    },
    "Stomach pain": {
        "disease": "Indigestion or Gastric Infection",
        "description": "Pain in the abdomen may occur due to digestive issues or infection.",
        "precautions": [
            "Avoid spicy and oily food.",
            "Drink clean water and stay hydrated.",
            "Eat light meals.",
            "Consult a doctor if pain is severe or persistent."
        ]
    },
    "Malaria": {
        "disease": "Malaria",
        "description": "Malaria is caused by Plasmodium parasites transmitted through mosquito bites.",
        "precautions": [
            "Sleep under mosquito nets.",
            "Avoid stagnant water near your home.",
            "Use mosquito repellents.",
            "Consult a doctor immediately for a blood test and treatment."
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

    # If disease found
    if result:
        return render_template(
            "index.html",
            symptoms=symptoms,
            disease=result["disease"],
            description=result["description"],
            precautions=result["precautions"]
        )

    # If no disease found
    else:
        return render_template(
            "index.html",
            symptoms=symptoms,
            disease="Unknown Disease",
            description="No matching disease found based on the symptoms provided.",
            precautions=[
                "Try entering more specific symptoms",
                "Drink plenty of water",
                "Take proper rest",
                "Consult a doctor if symptoms continue"
            ]
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

