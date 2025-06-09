from flask import Flask, render_template, request, jsonify
from db_utils import get_drones
from decision.filiter import filter_drones
from decision.ahp import calculate_ahp
from decision.topsis import calculate_topsis
from decision.feature_quantification import quantify_features
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/weights')
def weights():
    return render_template('weights.html')

@app.route('/select', methods=['POST'])
def select():
    criteria = request.json  # Get filter criteria from frontend
    csv_path = os.path.join(os.path.dirname(__file__), 'drone_original.csv')
    drones = get_drones(csv_path)    # Read all drone data
    filtered = filter_drones(drones, criteria)  # Filter drones
    return jsonify({"success": True, "drones": filtered})

@app.route('/rank', methods=['POST'])
def rank():
    data = request.json
    drones = data["drones"]
    selected_method = data.get("method", "ahp")
    if "stars" in data:
        stars = data["stars"]
        total = sum(stars.values())
        weights = {k: (v / total if total > 0 else 0) for k, v in stars.items()}
    else:
        weights = data["weights"]
    quantified_drones = quantify_features(drones)

    try:
        if selected_method == "topsis":
            result = calculate_topsis(weights,quantified_drones)
        elif selected_method == "ahp":
            result = calculate_ahp(weights, quantified_drones)
        else:
            return jsonify({
                "success": False, 
                "error": "Invalid method selected"
            }), 400
        
        return jsonify({
            "success": True, 
            "result": result,
            "method": selected_method,
            "weights": weights
        })
    except Exception as e:
        return jsonify({
            "success": False, 
            "error": str(e)
        }), 500
if __name__ == '__main__':
    app.run(debug=True)
