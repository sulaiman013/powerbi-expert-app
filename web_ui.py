"""
Power BI MCP Server V3 - Web UI
================================
Entry point for the modular Flask web application.

Supports both local (Ollama) and cloud (Azure AI Foundry) providers.

Run with: python web_ui.py
         Or double-click PowerBI_Expert.bat
Open: http://localhost:5050
"""

import logging
import sys
import webbrowser
import threading
import time
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("powerbi-v3-webui")

# Import the app factory
from src.web.app import run_server


def open_browser(url: str, delay: float = 1.5):
    """Open the browser after a short delay to ensure server is ready."""
    time.sleep(delay)
    webbrowser.open(url)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5050
    url = f'http://{host}:{port}'

    # Auto-open browser in background thread
    browser_thread = threading.Thread(target=open_browser, args=(url,), daemon=True)
    browser_thread.start()

    # Start the server (blocking)
    run_server(host=host, port=port, debug=False)
