from flask import Flask, render_template, jsonify
from database import load_athletes_from_db

app = Flask(__name__)
       
@app.route("/")
def hello_swimdata():
    athletes = load_athletes_from_db()
    return render_template ("home.html", athletes=athletes)

@app.route("/api/athletes")
def list_athletes():
    return jsonify(athletes)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)