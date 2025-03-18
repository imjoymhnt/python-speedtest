from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/speedtest', methods=['GET'])
def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()  # Finds the best test server
    
    download_speed = round(st.download() / 1_000_000, 2)  # Convert to Mbps
    upload_speed = round(st.upload() / 1_000_000, 2)  # Convert to Mbps

    return jsonify({
        "download_speed_mbps": download_speed,
        "upload_speed_mbps": upload_speed
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
