from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class MyTable(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

db.create_all()

@app.route('/insert_data')
def insert_data():
    new_data = MyTable(user_id=1, description='Example description')
    db.session.add(new_data)
    db.session.commit()
    return 'Data inserted successfully!'


if __name__ == '__main__':
    app.run(debug=True)
