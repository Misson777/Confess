from flask import Flask, request, jsonify
from models import db, User, Confession
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(
        name=data['name'],
        age=data['age'],
        city=data['city'],
        school=data['school'],
        gender=data['gender']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"status": "User Registered", "user_id": user.id})

@app.route('/confess', methods=['POST'])
def confess():
    data = request.json
    confession = Confession(
        user_id=data['user_id'],
        crush_name=data['crush_name'],
        crush_birthday=datetime.strptime(data['crush_birthday'], '%Y-%m-%d').date(),
        crush_city=data['crush_city'],
        first_meet_place=data['first_meet_place'],
        crush_school=data['crush_school']
    )
    db.session.add(confession)
    db.session.commit()
    match_found = check_for_match(confession)
    return jsonify({"status": "Confession Submitted", "match_found": match_found})

def check_for_match(confession):
    potential_match = Confession.query.filter_by(
        crush_name=confession.crush_name,
        crush_birthday=confession.crush_birthday,
        crush_city=confession.crush_city,
        crush_school=confession.crush_school,
        first_meet_place=confession.first_meet_place,
        match_found=False
    ).first()

    if potential_match:
        confession.match_found = True
        potential_match.match_found = True
        db.session.commit()
        return True
    return False

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)