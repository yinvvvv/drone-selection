from flask import Flask, render_template, request, jsonify
from db_utils import get_drones
from decision.filiter import filter_drones
from decision.ahp import calculate_ahp
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
    drones = get_drones(r'C:\Users\wangh\Desktop\drone\drone-selection\drone-selection\drone _original.csv')    # Read all drone data
    filtered = filter_drones(drones, criteria)  # Filter drones
    return jsonify({"success": True, "drones": filtered})

@app.route('/rank', methods=['POST'])
def rank():
    data = request.json
    drones = data["drones"]
    if "stars" in data:
        stars = data["stars"]
        total = sum(stars.values())
        weights = {k: (v / total if total > 0 else 0) for k, v in stars.items()}
    else:
        weights = data["weights"]
    ahp_result = calculate_ahp(weights, drones)
    return jsonify({"success": True, "ahp": ahp_result})

if __name__ == '__main__':
    app.run(debug=True)
