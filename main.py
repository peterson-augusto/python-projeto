from flask_marshmallow import Marshmallow
from app.database import app

ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
    

