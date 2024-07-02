from flask import Flask, render_template, jsonify, request
from database import load_athletes_from_db, load_athlete_from_db, add_time_into_db

app = Flask(__name__)
       
@app.route("/")
def hello_swimdata():
    athletes = load_athletes_from_db()
    return render_template ("home.html", athletes=athletes)

@app.route("/api/athletes")
def list_athletes():
    athletes = load_athletes_from_db()
    return jsonify(athletes)

@app.route("/athlete/<idAthlete>")
def show_athlete(idAthlete):
    athlete = load_athlete_from_db(idAthlete)
    if not athlete:
        return "Not found", 404
    return render_template("athletepage.html", athlete=athlete)

@app.route("/athlete/<idAthlete>/time", methods = ['POST'])
def insert_time_into_db(idAthlete):
    data = request.form
    athlete = load_athlete_from_db(idAthlete)
    add_time_into_db(idAthlete, data)
    
    return render_template("time_submitted.html",                                                  application=data,
                            athlete=athlete)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)