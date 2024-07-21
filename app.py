from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello </h1>"



if __name__ == "__name__":
    app.run(host='0.0.0.0',port=5000,debug=False) 
    # debug=True will automatically reload the server when you make changes to the code