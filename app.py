from flask  import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)


app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="python_web_mysql"
mysql=MySQL(app)

#route defaul index
@app.route('/')
def index():
    cur=mysql.connection.cursor()
    data=cur.execute("select * from employee_detail")
    if data>0:
        employees=cur.fetchall()
        return render_template('index.html',employees=employees)
    cur.close()

# route for addemployee page    
@app.route('/addemployee',methods=['GET','POST'])
def addemployee():
    if request.method=='POST':
        employee_name=request.form['employee_name']
        cur=mysql.connection.cursor()
        cur.execute("insert into employee_detail (employee_name) values(%s)",(employee_name,))
        mysql.connection.commit()
        cur.close()

        return "success" 
    else :
        return render_template("addemployee.html")


if __name__=="__main__":
    app.run(debug=True)