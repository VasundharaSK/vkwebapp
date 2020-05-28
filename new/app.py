from flask import Flask,render_template           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def home():                      # call method hello
    return render_template("home.html")
    
@app.route("/hello/")    
def about():                      # call method hello
    return render_template("about.html")    # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                   # run the flask app