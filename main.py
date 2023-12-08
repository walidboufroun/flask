from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Use render_template to render an HTML template
    #return render_template('index.html')
    #message = "<!DOCTYPE html><html><head>    <title>Flask App</title></head><body>    <h1>Welcome GNOV, Je suis un serveur gratuit avec python</h1>    <!-- Add a button to navigate to the /image route -->    <a href="{{ url_for('upload_image') }}"><button>Go to /image</button></a>    </body></html>"
    message = "walid"
    return message
   
@app.route('/image')
def image():
    return 'IMAGE PAGE' 

@app.route('/resultat')
def resultat():
    return 'Resulatat'

@app.route('/calcul')
def calcule():
    number1 = 2 
    number2 = 3 
    number3 = number1 + number2 
    return number3

@app.route('/gnov-image', methods=['GET'])
def get_gnov_image():
    # Assuming you want to provide some image data in response
    # You can customize this based on your requirements
    image_data = {
        "image_url": "https://example.com/gnov-image.jpg",
        "description": "This is the GNOV image"
    }

    return jsonify(image_data)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
