#!/usr/bin/env python3
import sys
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
SITE_DIR = Path(__file__).parent / "mositlab-site"
DEFAULT_PORT = 8080
class SiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIR), **kwargs)
    def log_message(self, fmt, *args):
        method_color = "\033[94m"
        reset = "\033[0m"
        status = args[1] if len(args) > 1 else ""
        if status.startswith("2"):
            status_color = "\033[92m"
        elif status.startswith("3"):
            status_color = "\033[93m"
        else:
            status_color = "\033[91m"
        print(f"{method_color}[{self.address_string()}]{reset} {status_color}{fmt % args}{reset}")
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()
def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    if not SITE_DIR.exists():
        print(f"\033[91m✗ Папка сайта не найдена: {SITE_DIR}\033[0m")
        sys.exit(1)
    server = HTTPServer(("", port), SiteHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[91m✗ Сервер остановлен.\033[0m\n")
        server.server_close()
if __name__ == "__main__":
    main()