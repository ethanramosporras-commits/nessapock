import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)

# Base directory for the app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

def load_config():
    """Load configuration from config.json, fallback to defaults if error."""
    if not os.path.exists(CONFIG_PATH):
        # Default fallback config
        return {
            "theme": {
                "background_color": "#FAF6F0",
                "primary_color": "#D4AF37",
                "secondary_color": "#2C3E50",
                "text_color": "#333333",
                "card_background": "rgba(255, 255, 255, 0.9)",
                "font_title": "'Playfair Display', serif",
                "font_body": "'Montserrat', sans-serif"
            },
            "header": {
                "title": "¡Feliz Día del Padre!",
                "subtitle": "Un día especial para el mejor papá de todos.",
                "intro": "Querido papá, este espacio es para ti Gracias por todo tu amor y tu paciencia."
            },
            "gift": {
                "box_color": "#C0392B",
                "lid_color": "#A93226",
                "ribbon_color": "#F1C40F",
                "message": "Te amo mucho papá gracias por todo que has hecho por mi"
            },
            "gallery": []
        }
    
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        abort(500, description="Error loading config.json. Check syntax.")

@app.route('/')
def index():
    config_data = load_config()
    return render_template('index.html', config=config_data)

if __name__ == '__main__':
    # Running locally on port 5000, debug mode enabled for hot-reload of templates and config
    app.run(host='127.0.0.1', port=5000, debug=True)
