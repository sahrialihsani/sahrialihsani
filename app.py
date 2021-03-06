# Flask utils
from flask import Flask, request, render_template

# Define a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # app.run(host="0.0.0.0",debug=True,port="4100")
    app.run()
