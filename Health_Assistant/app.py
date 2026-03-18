from flask import Flask, render_template, request

app = Flask(__name__)

# Knowledge base
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
    "vomiting": {
        "disease": "Food Poisoning or Stomach Infection",
        "description": "Vomiting can occur due to food poisoning or digestive problems.",
        "precautions": [
            "Drink small amounts of clean water frequently.",
            "Avoid oily and spicy food.",
            "Eat light foods like rice or bananas.",
            "Consult a doctor if it continues for 24 hours."
        ]
    },
    "headache": {
        "disease": "Migraine or Tension Headache",
        "description": "A headache can be caused by stress or dehydration.",
        "precautions": [
            "Get enough rest.",
            "Stay hydrated.",
            "Avoid bright lights.",
            "Consult doctor if severe."
        ]
    },
    "stomach pain": {
        "disease": "Indigestion or Gastric Infection",
        "description": "Abdominal pain due to digestion issues.",
        "precautions": [
            "Avoid spicy food.",
            "Drink clean water.",
            "Eat light meals.",
            "Consult doctor if severe."
        ]
    },
    "malaria": {
        "disease": "Malaria",
        "description": "A mosquito-borne disease caused by parasites.",
        "precautions": [
            "Use mosquito nets.",
            "Avoid stagnant water.",
            "Use repellents.",
            "Consult doctor immediately."
        ]
    }
}

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# 🔥 UPDATED ROUTE (IMPORTANT)
@app.route('/diagnosis', methods=['POST'])
def diagnosis():
    user_input = request.form.get('symptoms', '').lower()

    result = None

    for key in disease_data:
        if key in user_input:
            result = disease_data[key]
            break

    # If found
    if result:
        return render_template(
            "result.html",
            symptoms=user_input,
            disease=result["disease"],
            description=result["description"],
            precautions=result["precautions"]
        )

    # If not found
    else:
        return render_template(
            "result.html",
            symptoms=user_input,
            disease="No matching disease found",
            description="Sorry! we couldn't identify the disease.",
            precautions=[
                "Try entering more specific symptoms",
                "Stay calm and take rest",
                "Consult a doctor if needed"
            ]
        )


if __name__ == '__main__':
    app.run(debug=True)
