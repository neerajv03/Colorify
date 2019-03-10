"""
@Author: Neeraj Venugopal
@Date: 27th February 2018
This is the main Python Server Code

"""

# Using Flask framework and not Django :P
import os
import logging as logger
import backend.image_upload as imageUpload
from flask import Flask, request, render_template

logger.basicConfig(level=logger.INFO)
app = Flask(__name__)
 
uploadFolder = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = uploadFolder

@app.route("/")
def webPageStartup():
    logger.info("Process Start")
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'nee.jpg')
    return render_template("home.html")

@app.route("/uploadOtherApiImage", methods=['POST'])
def uploadFile():
    logger.info("Upload File Called")
    file = request.files['image']
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    toWebPage = imageUpload.postUploadImage(file, filePath)
    logger.info("Image Path is %s", toWebPage)
        # fileName = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # logger.info("File Name is %s", fileName )
        # fileName = fileName.replace("\\","/")
        # logger.info("File Name is %s", fileName )
        # fileName = 'uploads/nee.jpg'
    return render_template("home.html", user_image = toWebPage)

if __name__ == "__main__":
    app.run(debug=False, use_evalex=False)
