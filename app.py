from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"  # Folder to store uploaded artwork images

@app.route("/")
def home():
    return "Homepage"

if __name__ == "__main__":
    app.run(debug=True)
