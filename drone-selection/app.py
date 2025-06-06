from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_drones():
    conn = sqlite3.connect('drones.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM drones')
    drones = [dict(row) for row in c.fetchall()]
    conn.close()
    return drones

def select_drone(payload, range_required, endurance_required):
    # 简单决策逻辑：满足所有需求的无人机
    suitable = [
        drone for drone in DRONES
        if drone["payload"] >= payload
        and drone["range"] >= range_required
        and drone["endurance"] >= endurance_required
    ]
    # 返回第一个合适的无人机
    return suitable[0] if suitable else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select', methods=['POST'])
def select():
    data = request.json
    payload = data.get('payload', 0)
    range_required = data.get('range', 0)
    endurance_required = data.get('endurance', 0)
    drone = select_drone(payload, range_required, endurance_required)
    if drone:
        return jsonify({"success": True, "drone": drone})
    else:
        return jsonify({"success": False, "message": "未找到合适的无人机"})

if __name__ == '__main__':
    app.run(debug=True)