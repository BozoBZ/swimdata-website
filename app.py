from flask import Flask, render_template, jsonify
from database import load_athletes_from_db, load_athlete_from_db

app = Flask(__name__)
       
@app.route("/")
def hello_swimdata():
    athletes = load_athletes_from_db()
    return render_template ("home.html", athletes=athletes)

@app.route("/api/athletes")
def list_athletes():
    athletes = load_athletes_from_db()
    return jsonify(athletes)

@app.route("/athlete/<id_athlete>")
def show_athlete(id_athlete):
    athlete = load_athlete_from_db(id_athlete)
    if not athlete:
        return "Not found", 404
    return render_template("athletepage.html", athlete=athlete)
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)