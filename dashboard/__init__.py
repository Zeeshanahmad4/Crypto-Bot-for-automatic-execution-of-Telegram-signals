from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # Set up any additional configurations here, such as database connections, authentication, etc.

    # Register blueprints
    from .views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    return app
# Dashboard Module 
