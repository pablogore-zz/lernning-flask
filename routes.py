from flask      import Flask , render_template , request
from  models    import db
from forms      import SignupForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/jlt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'development-key'
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup",methods=["GET","POST"])
def singup():
    form = SignupForm()
    if request.method == 'POST':
        return 'Succesfully!!!'
    elif request.method=='GET':
        return render_template('signup.html' , form = form)

if __name__ == '__main__':
    app.run(debug=True)