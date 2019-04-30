# Colorify
Training a machine to color black and white images/

This project is a web application that would take grayscale images and provide you with a color image./

There are 3 implementations used in this project.\

1) Using Algorithmia API - This is the API created by Algorithmia. 
2) Using Open CV - This implementation is using the models created, we have written a open Cv program to use that model.
3) Using Tensorflow - This is an implementation where the model is created by us.

The Following implementation is then deployed to Heroku Application. provided in the link above.


Project Structure/

./
├── app.py/
├── Aptfile/
├── backend/
│   ├── colorizeImage.py/
│   ├── colorizeImagetf.py/
│   ├── __pycache__/
│   │   ├── colorizeImage.cpython-37.pyc/
│   │   ├── colorizeImagetf.cpython-37.pyc/
│   │   ├── image_upload.cpython-37.pyc/
│   │   ├── usingAlgorithmiaApi.cpython-37.pyc/
│   │   ├── usingOpenCVMethod.cpython-37.pyc/
│   │   └── usingTensorFlow.cpython-37.pyc/
│   ├── tensorFlow/
│   │   ├── model_2500.h5/
│   │   ├── model_2500.json/
│   │   ├── model.h5/
│   │   ├── model.h5_6000/
│   │   ├── model.json/
│   │   ├── model.json_6000/
│   │   └── tensor_flow_colorify.ipynb/
│   ├── TensorFlowModels/
│   │   ├── model.h5/
│   │   └── model.json/
│   ├── usingAlgorithmiaApi.py/
│   ├── usingOpenCVMethod.py/
│   └── usingTensorFlow.py/
├── getModels.sh/
├── node_modules/
│   └── fullpage.js/
│       ├── dist/
│       │   ├── fullpage.css/
│       │   ├── fullpage.extensions.min.js/
│       │   ├── fullpage.js/
│       │   ├── fullpage.min.css/
│       │   ├── fullpage.min.css.map/
│       │   ├── fullpage.min.js/
│       │   └── fullpage.min.js.map/
│       ├── LICENSE/
│       ├── package.json/
│       ├── README.md/
│       └── vendors/
│           ├── easings.js/
│           ├── easings.min.js/
│           ├── easings.min.js.map/
│           ├── scrolloverflow.js/
│           ├── scrolloverflow.min.js/
│           └── scrolloverflow.min.js.map/
├── package-lock.json/
├── Procfile/
├── pts_in_hull.npy/
├── __pycache__/
│   └── app.cpython-37.pyc/
├── README.md/
├── requirements.txt/
├── static/
│   ├── css/
│   │   ├── imagePreview.css/
│   │   └── template.css/
│   ├── graphs/
│   │   ├── histogram_open_cv.png/
│   │   └── histogram_tensorflow.png/
│   ├── js/
│   │   ├── imagePreview.js/
│   │   └── template.js/
│   └── uploads/
│       ├── apple.jpeg/
│       ├── banana.jpeg/
│       ├── butterfly.jpeg/
│       ├── download.png/
│       ├── f.jpeg/
│       ├── flowers.jpeg/
│       ├── fox.jpeg/
│       ├── guava.jpeg/
│       ├── images.jpeg/
│       ├── neeTest.jpg/
│       ├── pineapple.jpeg/
│       ├── sample.jpeg/
│       └── simple-black-and-white-earth-md.png/
└── templates/
    └── home.html/
/
15 directories, 65 files/


