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
            "Wipe your body with lukewarm water to help reduce tempreture.",
            "Take paracetamol for high fever.",
            "Avoid oily and spicy foods.",
            "Do not sit directly under AC or in cold air.",
            "Wash your hands regularly to prevent spreading infection,especially in viral fever.",
            "Eat light and healthy food(like khichdi,lentils,fruits and dry fruits.)",
            "Consult a doctor if fever lasts more than 3 days."
        ],
        "video": "https://youtube.com/shorts/78zYCGGQ7xg?si=sAqOPnQPmuClMpN3"
    },
    "cough": {
        "disease": "Respiratory Infection or Allergic Cough",
        "description": "Coughing helps clear your airways but persistent coughs may indicate infection.",
        "precautions": [
            "Drink warm fluids and honey with ginger.",
            "Avoid cold or dusty environments.",
            "Use cough syrup if necessary.",
            "Stay away from ice cream,cold drinks and refrigerated foods and water.",
            "Take stream 1-2 times a day to clear congestion and ease breathing.",
            "When coughing,use tissue or elbow to prevent spreading infections.",
            "Proper sleep helps your immune system recover faster.",
            "Use a scarf and avoid sudden tempreture changes.",
            "A spoon of honey can reduce throat irritation and calm coughing.",
            "Consult a doctor if cough persists for more than 2 weeks."
        ],
        "video": "https://youtube.com/shorts/WBmMCG1m9oE?si=VnEZm3ND3um5ysC9"
    },
    "vomiting": {
        "disease": "Food Poisoning or Stomach Infection",
        "description": "Vomiting can occur due to food poisoning or digestive problems.",
        "precautions": [
            "Drink small amounts of clean water frequently.",
            "Take small sips of ORS or coconut water frequently to prevent dehydration.",
            "Doctors may suggest medicines like Ondansetron.",
            "Lie down and avoid sudden movements.",
            "Sip ginger tea or use ginger can help ro reduce nausea naturally.",
            "Avoid strong smells",
            "Wash your hands properly to avoid infections.",
            "Avoid oily and spicy food.",
            "Eat light foods like rice or bananas.",
            "Consult a doctor if it continues for 24 hours."
        ],
        "video": "https://youtube.com/shorts/n3qBsU1E7yg?si=04Rux6T_FJEWikNP"
    },
    "headache": {
        "disease": "Migraine or Tension Headache",
        "description": "A headache can be caused by stress or dehydration.",
        "precautions": [
            "Get enough rest.",
            "Stay hydrated.",
            "Avoid bright lights.",
            "Use mild pain relievers like Crocin and Paracetamol.",
            "Reduce time on laptop/phones to avoid eye strain.",
            "Avoid unnecessary use of phone",
            "Rest in a  quiet and dark room.",
            "Maintain proper posture.",
            "Avoid loud noise this can worsen headches,",
            "Don't skip meals.",
            "Consult doctor if severe."
        ],
        "video": "https://youtu.be/pKq07s3qWik?si=zRaB5RtYc6RjXcHc"
    },
    "stomach pain": {
        "disease": "Indigestion or Gastric Infection",
        "description": "Abdominal pain due to digestion issues.",
        "precautions": [
            "Avoid spicy food.",
            "Avoid physical activity and let your stomach relax.",
            "For mild pain, medicines like Dicycloverine(for cramps) and Paracetamol may help.",
            "Drink clean water.",
            "Avoid gas-forming foods like beans,carbonated drinks and junk foods.",
            "Eat slowly and in small portions.",
            "Wash your hands properly to avoid infections.",
            "Eat light meals.",
            "Consult doctor if severe."
        ],
        "video": "https://youtube.com/shorts/CC2IhNJyZsA?si=jAQoHy4sadqlPRNY"
    },
    "malaria": {
        "disease": "Malaria",
        "description": "A mosquito-borne disease caused by parasites.",
        "precautions": [
            "Sleep under a mosquito nets.",
            "Avoid stagnant water.",
            "Use repellents.",
            "Do not allow water to collect in coolers,buckets or pots-mosquitoes breed in stagnant water,",
            "Keep surrounding clean.",
            "Stay hydrated.",
            "Get tested early as soon as possible.",
            "Don't ignore symptoms.",
            "Consult doctor immediately."
        ],
        "video": "https://youtu.be/z5Ixzyfu5dk?si=PB1KzgTyBspPHUlz"
    },
    "dizziness": {
    "disease": "Dizziness / Vertigo",
    "description": "Dizziness is a feeling of being lightheaded, unsteady, or losing balance. It can be caused by dehydration, low blood pressure, or inner ear problems.",
    "precautions": [
        "Stay well hydrated throughout the day.",
        "Get up slowly to avoid sudden drops in blood pressure (Orthostatic Hypotension)",
        "Avoid sudden movements",
        "Eat regular, balanced meals to maintain sugar levels.",
        "Avoid skipping meals or long fasting periods.",
        "Limit caffeine and alcohol intake.",
        "Get enough sleep and rest daily.",
        "Avoid sudden head movements or quick position changes.",
        "Sit or lie down immediately if you feel dizzy.",
        "Manage stress and anxiety effectively.",
        "Avoid skipping meals.",
        "Consult a doctor if dizziness is frequent."
    ],
    "video": "https://youtu.be/o4GV-EbnMfI?si=GHib2D2RAHR_6ink"
},
    "low blood pressure": {
    "disease": "Hypotension",
    "description": "Low blood pressure can cause dizziness.",
    "precautions": [
        "Drink plenty of water throughout the day. Dehydration is a major cause of low BP",
        "Eat small meals",
        "Unlike high BP patients, people with low BP may benefit from slightly higher salt—but only under a doctor’s guidance.",
        "Large meals can cause a sudden drop in blood pressure. Eat smaller meals more often",
        "Getting up too quickly can lead to dizziness (called Orthostatic Hypotension). Rise slowly from sitting or lying positions.",
        "Caffeine can temporarily increase blood pressure. Useful during sudden drops (but don’t overdo it).",
        "Light activities like walking or yoga improve circulation and stabilize BP.",
        "Regularly check your BP to understand patterns and triggers.",
        "Avoid sudden standing",
        "Consult doctor"
    ],
    "video": "https://youtu.be/0HY91UCJseo?si=k0n7N7pk4OoW7cUr"
},
    "diabetes": {
    "disease": "Diabetes",
    "description": "Diabetes is a condition where blood sugar levels are too high.",
    "precautions": [
        "Avoid sugary foods",
        "Drink juice of Bitter Gourd if possible",
        "Eat more: whole grains, vegetables, fruits (low GI)",
        "At least 30 minutes (walking, cycling, yoga). Helps control sugar and improves insulin sensitivity.",
        "Water helps flush excess sugar through urine.",
        "Avoid Smoking and Alcohol 🚫",
        "Stress can increase blood sugar. Try meditation, breathing exercises, or relaxation techniques.",
        "Exercise regularly",
        "Monitor blood sugar levels",
        "Consult doctor regularly"
    ],
    "video": "https://youtube.com/shorts/HC7HLedb-O8?si=2zaPdMB463QD1EWd"
},
    "high blood pressure": {
    "disease": "Hypertension",
    "description": "High blood pressure increases risk of heart disease.",
    "precautions": [
        "Reduce salt intake",
        "Exercise daily",
        "At least 30 minutes (walking, jogging, yoga). Helps lower BP naturally.",
        "Losing even a few kilos can significantly reduce blood pressure.",
        "Smoking damages blood vessels and increases heart risk.",
        "Get Proper Sleep 😴,Poor sleep can worsen BP. Aim for 7–8 hours daily",
        "Avoid stress",
        "Check BP regularly",
        "Consult doctor regularly"
    ],
    "video": "https://youtu.be/E9zzPKiAGdY?si=tjvRFm58MnZs4sK2"
},
   "cold": {
    "disease": "Common Cold",
    "description": "A viral infection causing sneezing and runny nose.",
    "precautions": [
        "Avoid cold weather exposure. Keep your body, especially throat and chest, warm.",
        "Warm water, soups, and herbal teas help loosen mucus and keep you hydrated.",
        "Your body heals faster when you rest. Avoid heavy work and stress.",
        "Eat Light & Nutritious Food 🍲",
        "Take steam 1–2 times daily to relieve nasal congestion.",
        "Gargle with Warm Salt Water 🧂",
        "Stay away from ice cream, cold drinks, and refrigerated items.",
        "Wear a mask if needed—dust can worsen symptoms.",
        "Drink warm fluids",
        "Take rest",
        "Avoid cold weather",
        "Use steam inhalation"
    ],
    "video": "https://youtu.be/WNXFsCoJv8U?si=nQfgTuaVamuJd1l0"
},
"asthma": {
    "disease": "Asthma",
    "description": "A condition where airways become inflamed.",
    "precautions": [
        "Follow your doctor’s instructions for inhalers (e.g., Salbutamol) to quickly relieve symptoms.",
        "Avoid dust and smoke",
        "Wear a Mask in Pollution 😷",
        "Stay away from smoking and second-hand smoke—it’s a major trigger.",
        "Light exercise like walking or yoga is beneficial, but avoid overexertion.",
        "Stress can trigger asthma attacks. Practice breathing exercises or meditation.",
        "Flu or infections can worsen asthma. Annual flu shots are helpful.",
        "Track breathing patterns and warning signs like wheezing or shortness of breath.",
        "Use inhaler",
        "Exercise carefully",
        "Consult doctor"
    ],
    "video": "https://youtube.com/shorts/MJyyV3TxNII?si=OoriSLjyGw9C5Suu"
},
"dengue": {
    "disease": "Dengue Fever",
    "description": "A mosquito-borne viral disease.",
    "precautions": [
        "Avoid mosquito bites",
        "Avoid Stagnant Water,Mosquitoes breed in standing water.",
        "Sleep under nets and install window screens to stay protected.",
        "Rest is essential for recovery and boosting immunity.",
        "Regular blood tests are important, as dengue can lower platelets.",
        "Eat Light & Nutritious Food 🍲",
        "Use nets and repellents",
        "Drink fluids",
        "Consult doctor immediately",
        "Always consult a doctor—dengue can become serious if not treated properly."
    ],
    "video": "https://youtu.be/6-MX2MJOpQk?si=htUZRbNg6TmHL1rg"
},
"hairfall": {
    "disease": "Hair Loss (Alopecia)",
    "description": "Hair fall can occur due to stress, poor diet, hormonal imbalance, or genetics.",
    "precautions": [
        "Maintain a healthy diet rich in protein and vitamins",
        "Avoid excessive use of hair styling products",
        "Reduce stress through exercise or meditation",
        "Handle wet hair gently to prevent breakage",
        "Use mild, sulfate-free shampoo.",
        "Oil your hair regularly to nourish roots.",
        "Reduce stress to avoid Telogen Effluvium.",
        "Avoid tight hairstyles that pull hair roots.",
        "Stay well hydrated daily.",
        "Check for underlying issues like anemia or thyroid problems.",
        "Use natural remedies like aloe vera or amla.",
        "Use mild shampoos and avoid harsh chemicals",
        "Consult a doctor if hair fall is severe"
    ],
    "video": "https://youtube.com/shorts/GCrSmd-R1vM?si=QihpGctgvYyr9RFJ"
},
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
            precautions=result["precautions"],
            video=result["video"]
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
