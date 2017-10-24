from flask import Flask,render_template
from data import shoplist
app = Flask(__name__)
shoplist=shoplist()

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
    return render_template("shop.html",shop=shoplist)
	
@app.route("/faq")
def faq():
    return render_template("faq.html")
				
	
@app.route("/login")
def login():
    return render_template("login.html")
			
		
@app.route("/register")
def regester():
    return render_template("regester.html")
	
if __name__ == "__main__":
    app.run(debug=True)











