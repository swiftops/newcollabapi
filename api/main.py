from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection URI (replace with your PostgreSQL credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:HackM3@192.168.20.86/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy track modifications
db = SQLAlchemy(app)

# Define a model for comments
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

# Create database tables (you'll need to run this once)
with app.app_context():
    db.create_all()

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Hello, World!"

# Define a route to handle POST requests and store comments in the database
@app.route('/add_comment', methods=['POST'])
def add_comment():
    try:
        data = request.get_json()
        new_comment = Comment(text=data['text'])
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"message": "Comment added successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Define the custom port number here
custom_port = 8080  # Change this to your desired port number

# Run the web application with the custom port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=custom_port)
