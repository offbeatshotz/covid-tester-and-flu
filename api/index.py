from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Simulate processing time
    time.sleep(1.5)
    
    covid_risk = random.choice(["Low", "Moderate", "High"])
    flu_risk = random.choice(["Low", "Moderate", "High"])
    
    return jsonify({
        "status": "success",
        "results": {
            "covid": {
                "risk": covid_risk,
                "message": "No significant COVID markers found." if covid_risk == "Low" else "Minor indicators present." if covid_risk == "Moderate" else "Strong correlation with known markers."
            },
            "flu": {
                "risk": flu_risk,
                "message": "No significant Flu markers found." if flu_risk == "Low" else "Minor indicators present." if flu_risk == "Moderate" else "Strong correlation with known markers."
            }
        }
    })

@app.route('/')
def home():
    return "API is active"

if __name__ == '__main__':
    app.run()
