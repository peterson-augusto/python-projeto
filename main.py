from flask_marshmallow import Marshmallow
from app.database import app
from app.routes import redirect, render_template, request, url_for


ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
    
