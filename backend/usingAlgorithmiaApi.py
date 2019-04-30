import os
from sightengine.client import SightengineClient
import logging as logger
logger.basicConfig(level=logger.INFO)

import Algorithmia
import filetype
from Algorithmia.acl import ReadAcl, AclType
from PIL import Image
import io

# https://demos.algorithmia.com/colorize-photos/

# Authenticate with your API key
apiKey = "simwoLLSO25EL5rwWl7DSjlsXTu1"
# Create the Algorithmia client object
client = Algorithmia.client(apiKey)

# Instantiate a DataDirectory object, set your data URI and call create
nlp_directory = client.dir("data://Harika25/nlp_directory")
# Create your data collection if it does not exist
if nlp_directory.exists() is False:
    nlp_directory.create()

# Create the acl object and check if it's the .my_algos default setting
acl = nlp_directory.get_permissions()  # Acl object
acl.read_acl == AclType.my_algos  # True

# Update permissions to private
nlp_directory.update_permissions(ReadAcl.private)
nlp_directory.get_permissions().read_acl == AclType.private # True


resultFolder = os.path.join('static', 'result')


# def postUploadImage(uploadImage, uploadImagePath):
#     logger.info("In this post Upload Image")
#     uploadImage.save(uploadImagePath)
#     logger.info("Leaving the function")

#     fileName = os.path.join(resultFolder, 'nee.jpg')
#     return fileName


def colorifyimage(file,filepath,filename):
    print(filepath)
    file.save(filepath)
    image_file = "data://Harika25/nlp_directory/"+filename
    if client.file(image_file).exists() is False:
        client.file(image_file).putFile(filepath)
    # Algorithm Implementation
    input = {
        "image": image_file
    }
    algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
    algo.set_options(timeout=300) # optional
    output = algo.pipe(input).result
    output_file = output['output']

    # Download the file
    if client.file(output_file).exists() is True:
        localfile = client.file(output_file).getBytes()
        img = Image.open(io.BytesIO(localfile))
        img = img.convert("RGB")

        # saving the colored image to the result directory in static folder
        output_filename = "colorized_algorithmia_"+filename
        result = os.path.join(resultFolder, output_filename)
        print(result)
        img.save(result)

    return result