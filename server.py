from turtle import color
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html",w = 8, h = 8, color1 = "red", color2 = "black")
@app.route('/<int:w>/<int:h>')
def board1(w,h):
    return render_template("index.html",w = w,h = h, color1 = "red", color2 = "black")
@app.route('/4')
def board2():
    return render_template("index.html",w = 8,h = 4, color1 = "red", color2 = "black")
@app.route('/<int:w>/<int:h>/<color1>/<color2>') 
def board3(w,h,color1,color2):
    return render_template("index.html",w = w,h = h, color1 = color1, color2 = color2)


















if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.