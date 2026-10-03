import os
import sys
import webbrowser
import threading

PORT = 5000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

try:
    from flask import Flask, send_from_directory

    app = Flask(__name__, static_folder=BASE_DIR)

    @app.route('/')
    def index():
        return send_from_directory(BASE_DIR, 'index.html')

    @app.route('/style.css')
    def styles():
        return send_from_directory(BASE_DIR, 'style.css')

    if __name__ == '__main__':
        print("==================================================")
        print(f"  StudyBuddy running at: http://localhost:{PORT}")
        print("  Press Ctrl+C to stop.")
        print("==================================================")
        # Open browser in 0.8s
        threading.Timer(0.8, open_browser).start()
        app.run(host='0.0.0.0', port=PORT, debug=False)

except ImportError:
    # Zero-dependency standard library fallback
    import http.server
    import socketserver

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=BASE_DIR, **kwargs)

    if __name__ == '__main__':
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print("==================================================")
            print(f"  StudyBuddy (StdLib) running at: http://localhost:{PORT}")
            print("  Press Ctrl+C to stop.")
            print("==================================================")
            threading.Timer(0.8, open_browser).start()
            httpd.serve_forever()
