import os
import json
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')
OUTPUT_PATH = os.path.join(BASE_DIR, 'index.html')

def build():
    if not os.path.exists(CONFIG_PATH):
        print(f"Error: {CONFIG_PATH} not found.")
        return

    # Load configuration
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('index.html')

    # Mock Flask's url_for in case it's used elsewhere in templates
    def url_for(endpoint, filename):
        return f"static/{filename}"

    # Render template
    rendered_html = template.render(config=config, url_for=url_for)

    # Write output to index.html in the root
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print("Static index.html has been generated successfully in the root directory!")

if __name__ == '__main__':
    build()
