import backend.colorizeImagetf as colorizeImagetf
import argparse
import logging as logger
logger.basicConfig(level=logger.INFO)


def tensorflowcaller(file, filePath, fileName):
    logger.info("Tensor Flow Called")
    logger.info(filePath)
    logger.info(fileName)
    logger.info(file)
    file.save(filePath)
    return colorizeImagetf.usingTensorFlow(filePath, fileName)