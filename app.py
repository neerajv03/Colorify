"""
@Author: Neeraj Venugopal
@Date: 27th February 2018
This is the main Python Server Code

"""

# Using Flask framework and not Django :P
import os
import logging as logger
import backend.usingAlgorithmiaApi as usingAlgorithmiaApi
import backend.usingOpenCVMethod as usingOpenCVMethod
from flask import Flask, request, render_template, jsonify

logger.basicConfig(level=logger.INFO)
app = Flask(__name__)
 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
uploadFolder = os.path.join(APP_ROOT, 'static/uploads')

@app.route("/")
def webPageStartup():
    logger.info("Process Start")
    return render_template("home.html")

@app.route("/algorithmiaApi", methods=['POST'])
def callAlgorithmiaApi():
    logger.info("Algorithmia API Called")
    file = request.files['image']

    filePath =  "/".join([uploadFolder, file.filename])
    toWebPage = usingAlgorithmiaApi.colorifyimage(file, filePath, file.filename)
    logger.info("Image Path is %s", toWebPage)

    return render_template("home.html", user_image = toWebPage)

@app.route("/openCvMethod", methods=['POST'])
def callOpenCvMethod():
    print("Inside Open CV REST CALL")
    logger.info("Open CV method Called")
    file = request.files['openCVImage']
    filePath =  "/".join([uploadFolder, file.filename])
    toWebPage = usingOpenCVMethod.openCvCaller(file, filePath, file.filename)
    return render_template("home.html", image_opencv = toWebPage)

if __name__ == "__main__":
    app.run(debug=False, use_evalex=False)
