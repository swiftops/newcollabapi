from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Hello, World!"

# Define the custom port number here
custom_port = 8080  # Change this to your desired port number

# Run the web application with the custom port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=custom_port)
