from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def receive_report():
    # Get the payload from the request
    json_payload = request.args.get('payload')
    
    if json_payload:
        try:
            # Decode the base64 payload
            decoded_json = base64.b64decode(json_payload).decode('ascii')
            report_data = json.loads(decoded_json)  # Convert JSON string to dict
            
            # Check and log each field explicitly
            sniff_timestamp = report_data.get('sniff_timestamp', 'N/A')
            layer = report_data.get('layer', 'N/A')
            srcPort = report_data.get('srcPort', 'N/A')
            dstPort = report_data.get('dstPort', 'N/A')
            ipSrc = report_data.get('ipSrc', 'N/A')
            ipDst = report_data.get('ipDst', 'N/A')
            highest_layer = report_data.get('highest_layer', 'N/A')
            
            print(f"Message reçu avec les informations suivantes :\n"
                  f"Timestamp: {sniff_timestamp}\n"
                  f"Layer: {layer}\n"
                  f"Source Port: {srcPort}\n"
                  f"Destination Port: {dstPort}\n"
                  f"Source IP: {ipSrc}\n"
                  f"Destination IP: {ipDst}\n"
                  f"Highest Layer: {highest_layer}\n")

            # Respond with a success message
            return jsonify({"status": "success", "message": "Data received successfully"}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": f"Error processing data: {str(e)}"}), 400
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
