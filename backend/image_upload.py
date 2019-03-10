import os
from sightengine.client import SightengineClient
import logging as logger
logger.basicConfig(level=logger.INFO)

resultFolder = os.path.join('static', 'uploads')


def postUploadImage(uploadImage, uploadImagePath):
    logger.info("In this post Upload Image")
    uploadImage.save(uploadImagePath)
    logger.info("Leaving the function")

    fileName = os.path.join(resultFolder, 'nee.jpg')
    return fileName
 