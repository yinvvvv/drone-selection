from flask import Flask, render_template, request, jsonify
from db_utils import get_drones
from decision.filiter import filter_drones

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select', methods=['POST'])
def select():
    criteria = request.json  # Get filter criteria from frontend
    drones = get_drones()    # Read all drone data
    filtered = filter_drones(drones, criteria)  # Filter drones
    return jsonify({"success": True, "drones": filtered})

if __name__ == '__main__':
    app.run(debug=True)