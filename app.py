from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pygame
import threading

app = Flask(__name__)
# app.secret_key = ''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/game_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'User already exists!'}), 400

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True}), 201

@app.route('/play')
def play():
    return render_template('play.html')  # Serve the game page

def run_game():
    # Initialize Pygame and start the game loop here
    pygame.init()
    # (Insert the Pygame code here, ensuring to pass the username if needed)

if __name__ == '__main__':
    db.create_all()  # Create database tables
    game_thread = threading.Thread(target=run_game)
    game_thread.start()  # Run the game in a separate thread
    app.run(debug=True)
