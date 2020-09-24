import os
import glob
from flask import Flask, request, send_from_directory, jsonify, send_file
from PIL import Image
from werkzeug.utils import secure_filename
from lib import file_check, resize
import uuid
import base64
import mimetypes
app = Flask(__name__)

UPLOAD_FOLDER = './image'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/<image_id>')
def return_image(image_id):
    image_path = glob.glob('image/'+image_id+'.*')
    if image_path and os.path.isfile(image_path[0]):
        content_type = mimetypes.guess_type(image_path[0])[0]
        if request.args.get('width'):
            return send_file(resize(image_path[0], request.args.get('width')), mimetype=content_type)
        else:
            return send_file(image_path[0], mimetype=content_type)
    else:
        return jsonify({"request": "failure", "error": "No image"})
    
    
@app.route('/', methods=['post'])
def upload():
    image = request.files['image']
    if image and file_check(image.filename, ALLOWED_EXTENSIONS):
        _, ext = os.path.splitext(image.filename)
        image_id = str(uuid.uuid4())
        image_name = secure_filename(image_id + ext.lower())
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        return jsonify({"request": "success", "image_id": image_id})
    elif not image:
        return jsonify({"request": "failure", "error": "There is no image file"})
    else:
        return jsonify({"request": "failure", "error": "Improperly formatted image"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)