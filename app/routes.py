from flask import render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user
from app.models import Users, user_schema
from app.database import app, db

# Puxar rota onde ficam os usuários
@app.route('/')
def home():
    return render_template('home.html')
    

# Cadastrar um novo usuário    
@app.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        usuario = Users(f_name = request.form['f_name'],
                        l_name = request.form['l_name'], 
                        email = request.form['email'], 
                        gender = request.form['gender'],
                        birthdata = request.form['birthdata'], 
                        password = request.form['password'],
                        senha_confirme = request.form['senha_confirme'])
                         
        
        db.session.add(usuario)
        db.session.commit()
    
    return render_template('cadastro.html')


# Deletar um usuário (pelo id)
@app.route('/delete/<id>')
def delete(id):
    usuario = Users.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('login'))


# Editar ou atualizar um usuário (pelo id)
@app.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id):
    usuario = Users.query.get(id)
    if request.method == 'POST':
        usuario.f_name = request.form['f_name']
        usuario.l_name = request.form['l_name']
        usuario.email = request.form['email']
        usuario.gender = request.form['gender']
        usuario.birthdata = request.form['birthdata']
        usuario.password = request.form['password']
        usuario.senha_confirme = request.form['senha_confirme']
        
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('edit.html', usuario = usuario)


# Login 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        
        user = Users.query.filter_by(email=email).first()
        
        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('login.html')

# Logout 
@app.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')
