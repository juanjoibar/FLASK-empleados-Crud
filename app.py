from os import curdir
from flask import Flask
from flask import render_template,request
from pymysql import cursors
from werkzeug.utils import redirect
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistemas1121' 

mysql.init_app(app)

@app.route('/')
def index():
    #sql = "INSERT INTO `sistemas1121`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'daniel', 'daniel@gmail.com', 'foto.jpg');"
    sql = "SELECT * FROM `sistemas1121`.`empleados`;"
    
    conn = mysql.connect()

    cursor = conn.cursor()
    
    cursor.execute(sql)
    empleados = cursor.fetchall()

    conn.commit()

    
    #conn = mysql.connect()
    #cursor = conn.cursor()
    #cursor.execute(sql)
    #conn.commit()
    #return render_template('empleados/index.html')
    return render_template('empleados/index.html', empleados = empleados)

@app.route("/create")
def create():

    return render_template('empleados/create.html')


@app.route("/store",methods = ['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    now = datetime.now()  
    tiempo = now.strftime("%Y%H%M%S")
    if _foto.filename!= '':
        _nuevonombreFoto = tiempo + _foto.filename 
        _foto.save("uploads/"+_nuevonombreFoto)

    sql = "INSERT INTO `sistemas1121`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s , %s);"
    datos = (_nombre, _correo , _nuevonombreFoto)
            
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    sql = "SELECT * FROM `sistemas1121`.`empleados`;"
    
    conn = mysql.connect()

    cursor = conn.cursor()
    
    cursor.execute(sql)
    empleados = cursor.fetchall()

    conn.commit()

    return render_template('empleados/index.html', empleados = empleados )

@app.route('/destroy/<int:id>')
def destroy(id):
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `sistemas1121`.`empleados` WHERE id = %s ", (id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')    
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    #sql = "SELECT * FROM `sistemas1121`.`empleados` where id = %s", id 
    cursor.execute("SELECT * FROM `sistemas1121`.`empleados` WHERE id = %s ", (id))
    #cursor.execute(sql)
    empleados = cursor.fetchall()
    conn.commit()
    return render_template('empleados/edit.html', empleados = empleados)

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    id = request.form['txtId']
    sql = "UPDATE `sistemas1121`.`empleados` SET `nombre` = %s , `correo` = %s WHERE id = %s ; "
    datos = (_nombre, _correo,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/')



#    return render_template('/')

 


if __name__ == '__main__':
    app.run(debug=True)