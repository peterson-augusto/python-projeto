from flask_marshmallow import Marshmallow
from app.routes import redirect, render_template, request
from app.database import app

ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
    

# ! Faltando fazer autenticação de usuários !
# ! Armazenar dados da data do usuário(dia, mês e ano) !
# ! Conectar ao banco de dados !