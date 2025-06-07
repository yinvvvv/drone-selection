from flask import Flask, render_template, request, jsonify
from db_utils import get_drones
from decision.filiter import filter_drones
from decision.wsm import wsm
from decision.ahp import ahp
from decision.topsis import topsis
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select', methods=['POST'])
def select():
    criteria = request.json  # Get filter criteria from frontend
    drones = get_drones(r"C:\Users\lenovo\Desktop\drone-selection-main\drone-selection\drone _original.csv")    # Read all drone data
    filtered = filter_drones(drones, criteria)  # Filter drones
    return jsonify({"success": True, "drones": filtered})

@app.route('/rank', methods=['POST'])
def rank():
    data = request.json
    drones = data["drones"]
    weights = data["weights"]

    wsm_result = wsm(drones, weights)
    ahp_result = ahp(weights, drones)
    topsis_result = topsis(drones, weights)

    return jsonify({"success": True, "wsm": wsm_result, "ahp": ahp_result, "topsis": topsis_result})

if __name__ == '__main__':
    app.run(debug=True)
