import numpy as np
import cv2 as cv
import argparse
import os
import os.path
import logging as logger
logger.basicConfig(level=logger.INFO)

resultFolder = os.path.join('static', 'result')

def usingTensorFlow(filepath, fileName):
    logger.info("inside tensor flow code")