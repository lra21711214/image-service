# image-service

Image management service<br>
Images can be saved, displayed, and resized.

# How to use?
```
git clone https://github.com/lra21711214/image-service.git
cd image-service
pip3 install -r requirements.txt
python3 app.py
```

# routing
```
@app.route('/', methods=['post'])
```
is route to post images.
upload file name is 'image'

```
@app.route('/<image_id>')
```
is Route to display the image.
If there is a get parameter (width), the width of the image is specified.
