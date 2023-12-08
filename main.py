from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Use render_template to render an HTML template
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def upload_image():
    # Assuming you want to handle image uploads here
    # Access the uploaded file using request.files
    uploaded_file = request.files['file']
    
    # Process the uploaded file as needed
    # You can save it, analyze it, etc.

    return jsonify({"message": "Image uploaded successfully"})

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
