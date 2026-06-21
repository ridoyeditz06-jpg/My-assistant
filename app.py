from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# কনফিগারেশন লোড করা
with open('config.json', 'r') as f:
    config = json.load(f)

@app.route('/command', methods=['POST'])
def process():
    user_input = request.json.get('text', '').lower()
    
    # অ্যাপ খোলার কমান্ড চেক
    for app_name, cmd in config['apps'].items():
        if f"open {app_name}" in user_input:
            return jsonify({"action": "execute", "cmd": cmd, "msg": f"বস, আপনার জন্য {app_name} ওপেন করছি।"})
    
    # সেটিংস কমান্ড চেক
    for set_name, cmd in config['settings'].items():
        if set_name in user_input:
            return jsonify({"action": "execute", "cmd": cmd, "msg": f"বস, {set_name.replace('_', ' ')} করা হয়েছে।"})

    return jsonify({"action": "none", "msg": "বস, আমি এটি বুঝতে পারিনি।"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
