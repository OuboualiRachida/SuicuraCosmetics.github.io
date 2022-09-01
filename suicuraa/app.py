from flask import Flask,render_template,request,flash

app = Flask(__name__)
import mysql.connector


conn = mysql.connector.connect(host='localhost',port='3308',
                                    database='suicura',
                                    user= 'root',
                                    password='')



cursor = conn.cursor()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog_list.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/testimonial")
def client():
    return render_template('testimonial.html')

@app.route('/contactus/', methods=['GET', 'POST'])
def contactus():
            
            if request.method=='POST':
                nom=request.form['fullname']
                
                email=request.form['email']
                Tele=request.form['tele']
                subject=request.form['subject']
                message=request.form['message']
                
                
                cursor = conn.cursor()    
                cursor.execute('''INSERT INTO  users VALUES(%s,%s,%s,%s,%s)''',(nom,email,Tele,subject,message))
                conn.commit()
                cursor.close()
                
                            
            
            
            return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=True)
