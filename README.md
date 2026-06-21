# Father's Day Web App

## Overview
A premium, highly customizable Father's Day website built with **Python Flask**. It features:
- A beautiful, responsive design with glassmorphism and subtle micro‑animations.
- An interactive "gift" element that reveals a heartfelt message when clicked.
- A gallery that displays high‑quality images (generated earlier) with captions.
- Easy theming and content customization via `config.json`.

## Quick Start
```bash
# Clone (already in scratch) – navigate to the project folder
cd C:\Users\ethan\.gemini\antigravity\scratch\fathers-day-app

# Create a virtual environment (if not already created)
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```
Open `http://127.0.0.1:5000` in a browser.

## Configuration (`config.json`)
All visual aspects (colors, fonts, texts) are defined in `config.json`. Edit the file to change:
- Theme colors (`background_color`, `primary_color`, etc.)
- Header titles and intro text
- Gift box colors and the message displayed on click
- Gallery entries (add objects with `image` and `caption`).

## Development
- **Templates**: `templates/index.html` uses Jinja2 to inject the JSON config.
- **Static assets**: `static/style.css` holds the premium styling; `static/script.js` handles the gift interaction and optional confetti.
- **Adding images**: place image files under `static/images/` and reference them in `config.json`.

## Deployment (Production)
For production replace the built‑in server with a WSGI server such as **gunicorn** or **waitress**.
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
Configure a reverse proxy (NGINX/Apache) as needed.

## Customization Tips
- Change the font families by editing the `@import` URLs at the top of `style.css` (Google Fonts).
- Adjust animation timings in `style.css` for a different feel.
- Extend the gift logic in `script.js` to play a sound or show a modal.

## License
MIT – feel free to adapt and share.
