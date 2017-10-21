from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/contact")
def contact():
    return render_template("contact.html")
		
@app.route("/shop")
def shop():
    return render_template("shoppinglist.html")
	
	
@app.route("/login")
def login():
    return render_template("login.html")
			
		
@app.route("/register")
def regester():
    return render_template("regester.html")
	
if __name__ == "__main__":
    app.run(debug=True)











