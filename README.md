# colorify
Training a machine to color black and white images

This project would be a web application that would take grayscale images and provide you with a  color image.

Project Structure
.
├── app.py
├── backend
│   ├── colorizeImage.py
│   ├── models
│   │   ├── colorization_deploy_v2.prototxt
│   │   ├── colorization_release_v2.caffemodel
│   │   └── colorization_release_v2_norebal.caffemodel
│   ├── pts_in_hull.npy
│   ├── __pycache__
│   │   ├── colorizeImage.cpython-37.pyc
│   │   ├── image_upload.cpython-37.pyc
│   │   ├── usingAlgorithmiaApi.cpython-37.pyc
│   │   └── usingOpenCVMethod.cpython-37.pyc
│   ├── usingAlgorithmiaApi.py
│   └── usingOpenCVMethod.py
├── package-lock.json
├── Procfile
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── imagePreview.css
│   │   └── template.css
│   └── js
│       ├── imagePreview.js
│       └── template.js
└── templates
    └── home.html

7 directories, 21 files
