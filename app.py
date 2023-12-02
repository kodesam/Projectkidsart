import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"  # Folder to store uploaded artwork images

@app.route("/")
def home():
    return "Homepage"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['artwork']
        filename = secure_filename(f.filename)
        # Save the uploaded file to the UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')

@app.route("/gallery")
def gallery():
    folder_path = app.config['UPLOAD_FOLDER']
    artworks = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path)]
    return render_template('gallery.html', artworks=artworks)
