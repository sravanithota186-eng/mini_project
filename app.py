from flask import Flask, render_template, request

app = Flask(__name__)
diseases = {
    "diabetes": {
        "description": "A chronic condition that affects blood sugar levels.",
        "symptoms": "Increased thirst, frequent urination, fatigue",
        "treatment": "Insulin therapy, diet control, exercise"
    },
    "malaria": {
        "description": "A mosquito-borne infectious disease.",
        "symptoms": "Fever, chills, sweating, headache",
        "treatment": "Antimalarial medications"
    },
    "covid": {
        "description": "Respiratory illness caused by coronavirus.",
        "symptoms": "Fever, cough, breathing difficulty",
        "treatment": "Supportive care, vaccination"
    }
}

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/search", methods=["POST"])
def search():

    disease_name = request.form["disease"].lower()

    result = diseases.get(disease_name)

    return render_template(
        "result.html",
        disease=disease_name,
        details=result
    )
if __name__ == "__main__":
    app.run(debug=True)
