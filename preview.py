"""Preview the website locally.

    python preview.py              -> serves the site at http://localhost:8000 and opens your browser
    python preview.py --port 8080  -> use a different port
    python preview.py --no-browser -> don't open a browser window

Stop the server with Ctrl+C. Nothing here is needed on GitHub Pages.
"""

import argparse
import http.server
import os
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOT_FOUND_PAGE = ROOT / "404.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        # Always serve fresh files so edits show up on reload.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        # Mimic GitHub Pages: unknown URLs get the site's own 404 page.
        if code == 404 and NOT_FOUND_PAGE.exists():
            body = NOT_FOUND_PAGE.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


class Server(http.server.ThreadingHTTPServer):
    # On Windows, address reuse lets two servers share one port; refuse instead.
    allow_reuse_address = os.name != "nt"


def main():
    parser = argparse.ArgumentParser(description="Preview the website locally.")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    # Use the next free port if the requested one is taken.
    for port in range(args.port, args.port + 20):
        try:
            server = Server(("127.0.0.1", port), Handler)
            break
        except OSError:
            continue
    else:
        raise SystemExit(f"No free port between {args.port} and {args.port + 19}.")

    url = f"http://localhost:{port}/"
    print(f"Serving {ROOT}")
    print(f"Open {url}  (press Ctrl+C to stop)")
    if not args.no_browser:
        threading.Timer(0.6, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
