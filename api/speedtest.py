from http.server import BaseHTTPRequestHandler
import speedtest
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        st = speedtest.Speedtest()
        response = {
            "download": round(st.download() / 1_000_000, 2),
            "upload": round(st.upload() / 1_000_000, 2)
        }
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
