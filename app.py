"""
@Author: Neeraj Venugopal
@Date: 27th February 2018
This is the main Python Server Code

"""

# Using Flask framework and not Django :P
import os
import logging as logger
import backend.image_upload as imageUpload
from flask import Flask, request, render_template, jsonify

logger.basicConfig(level=logger.INFO)
app = Flask(__name__)
 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
uploadFolder = os.path.join(APP_ROOT, 'static/uploads')

@app.route("/")
def webPageStartup():
    logger.info("Process Start")
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'nee.jpg')
    return render_template("home.html")

@app.route("/uploadOtherApiImage", methods=['POST'])
def uploadFile():
    logger.info("Upload File Called")
    file = request.files['image']

    filePath =  "/".join([uploadFolder, file.filename])
    toWebPage = imageUpload.colorifyimage(file, filePath, file.filename)
    logger.info("Image Path is %s", toWebPage)

    return render_template("home.html", user_image = toWebPage)

if __name__ == "__main__":
    app.run(debug=False, use_evalex=False)
