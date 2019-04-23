import backend.colorizeImage as colorizeImage
import argparse
import logging as logger
logger.basicConfig(level=logger.INFO)


# parser = argparse.ArgumentParser(description='Colorize GreyScale Image')
# parser.add_argument('--input', help='Path to image.')
# args = parser.parse_args()
# testFile = colorizeImage.usingOpenCVMethod(args.input)

def openCvCaller(file, filePath, fileName):
    logger.info("Open CV Processor Called")
    logger.info(filePath)
    logger.info(fileName)
    logger.info(file)
    file.save(filePath)
    return colorizeImage.usingOpenCVMethod(filePath, fileName)