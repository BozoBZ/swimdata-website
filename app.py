from flask import Flask, render_template, jsonify

app = Flask(__name__)

ATHLETES = [
    {
        'id': 1,
        'vorname': 'Pietro',
        'nachname': 'Bonelli',
        'ge': 'M',
        'geburtsdatum': '10.10.2006'
    },
    {
        'id': 2,
        'vorname': 'Marina',
        'nachname': 'Badstübner',
        'ge': 'W',
        'geburtsdatum': '10.11.2013'
    },
    {
        'id': 3,
        'vorname': 'Jascha',
        'nachname': 'Luft',
        'ge': 'M',
        'geburtsdatum': '01.10.2011'
    },
    {
        'id': 4,
        'vorname': 'Liz',
        'nachname': 'Brunner',
        'ge': 'M',
        'geburtsdatum': '12.12.2012'
    },
    {
        'id': 5,
        'vorname': 'Alexander',
        'nachname': 'Kutscher',
        'ge': 'M',
        'geburtsdatum': '12.01.2011'
    }
]

@app.route("/")
def hello_world():
    return render_template ("home.html", athletes=ATHLETES)

@app.route("/api/athletes")
def list_athletes():
    return jsonify(ATHLETES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)