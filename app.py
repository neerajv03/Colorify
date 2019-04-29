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
import backend.usingTensorFlow as usingTensorFlow
from flask import Flask, request, render_template, jsonify, redirect, url_for
import subprocess



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
    inputFolder = os.path.join('static', 'uploads')
    input_image = os.path.join(inputFolder, os.path.split(filePath)[1])
    logger.info("input: "+input_image)
    return render_template("home.html", scrollToAnchor="UsingAlgorithmia", user_image = toWebPage, input_image = input_image)

@app.route("/openCvMethod", methods=['POST'])
def callOpenCvMethod():
    modelPath = "/".join([APP_ROOT,"getModels.sh"])
    modelsDir = "/".join([APP_ROOT,"models"])
    if os.path.exists(modelsDir) is False:
        subprocess.call(modelPath, shell=True)
    print("Inside Open CV REST CALL")
    logger.info("Open CV method Called")
    file = request.files['openCVImage']
    filePath =  "/".join([uploadFolder, file.filename])
    print(filePath)
    toWebPage = usingOpenCVMethod.openCvCaller(file, filePath, file.filename)
    inputFolder = os.path.join('static', 'uploads')
    input_image = os.path.join(inputFolder, os.path.split(filePath)[1])
    print("input: "+input_image)
    print("output: "+toWebPage[0])
    print("graph: "+toWebPage[1])

    return render_template("home.html",scrollToAnchor="UsingOpenCV", image_opencv = toWebPage[0], input_image1 = input_image, histogram_open_cv = toWebPage[1])



@app.route("/tensorflowmethod", methods=['POST'])
def callTensorFlowMethod():
    logger.info("Tensor Flow method Called")
    file = request.files['tensorFlowImage']
    filePath =  "/".join([uploadFolder, file.filename])
    toWebPage = usingTensorFlow.tensorflowcaller(file, filePath, file.filename)
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=False, use_evalex=False)
