from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Use render_template to render an HTML template
    #return render_template('index.html')
    message = '<!DOCTYPE html><html><head><title>Flask App</title></head><body><h1>Welcome GNOV, Je suis un serveur gratuit avec python</h1><!-- Add a button to navigate to the /image route --><a href="https://flask-production-7a55.up.railway.app/image"><button>Go to /image</button></a></body></html>'
    #message = "<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Hello World !</h1></body></html>"
    return message
   
@app.route('/image')
def image():
    image = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>Hello World !</h1><form action="/resultat" method="post"><label for="file">Upload your pic</label><input type="file" name="file"><button type="submit">Valider</button></form></body></html>'
    return image 

@app.route('/resultat')
def resultat():
    input_data = request.form['file']
    return 'Image uploaded'

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
