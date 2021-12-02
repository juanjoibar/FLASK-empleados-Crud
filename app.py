from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistemas1121' 

mysql.init_app(app)

@app.route('/')
def index():
    sql = "INSERT INTO `sistemas1121`.`empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'daniel', 'daniel@gmail.com', 'foto.jpg');"
    #sql = "SELECT * FROM sistemas1121.empleados;"
    
    conn = mysql.connect()

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    
    #conn = mysql.connect()
    #cursor = conn.cursor()
    #cursor.execute(sql)
    #conn.commit()

    return render_template('empleados/index.html')

#@app.route("/create")
#def create():
#    return render_template('empleados/create.html')
#@app.route("/store",methods ['POST'])
#def storage():
#    _nombre=request.form['txtNombre']
#    _correo=request.form['txtCorreo']
#    _foto=request.form['txtFoto']
    
#    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'daniel', 'daniel@gmail.com', 'foto.jpg');"
#    datos = (_nombre, _correo , _foto.filename)
    
#    conn = mysql.connect()
#   cursor = conn.cursor()
#    cursor.execute(sql, datos)
#    conn.commit()



if __name__ == '__main__':
    app.run(debug=True)