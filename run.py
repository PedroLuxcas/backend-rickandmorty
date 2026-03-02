import os
from app import create_app

config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"\n🚀 Server running at http://localhost:{port}")
    print(f"📡 Environment: {config_name}")
    app.run(host='0.0.0.0', port=port, debug=(config_name == 'development'))