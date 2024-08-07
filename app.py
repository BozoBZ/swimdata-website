from flask import Flask, render_template, jsonify, request
from database import load_athletes_from_db, load_athlete_from_db, add_time_into_db, load_times_from_db

app = Flask(__name__)

def format_swimtime(swimtime):
    if swimtime is None:
        return None
    else:
        return swimtime[0:1]+":"+swimtime[2:3]+"."+swimtime[4:5]     
       
@app.route("/")
def hello_swimdata():
    return render_template ("home.html")

@app.route("/api/athletes")
def list_athletes_jsonify():
    athletes = load_athletes_from_db()
    return jsonify(athletes)

@app.route("/athletes")
def list_athletes_tables():
    athletes = load_athletes_from_db()
    return render_template ("athletes.html", athletes=athletes)

@app.route("/athletes/<idAthlete>")
def show_athlete(idAthlete):
    athlete = load_athlete_from_db(idAthlete)
    if not athlete:
        return "Not found", 404
    return render_template("athlete_details.html", athlete=athlete)

@app.route("/times")
def list_times_tables():
    times = load_times_from_db()
    return render_template ("times.html", times=times)

@app.route("/times", methods = ['POST'])
def insert_time_into_db():
    data = request.form
    add_time_into_db(data)
    return render_template("time_submitted.html", data=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)