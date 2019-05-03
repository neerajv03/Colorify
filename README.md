# Colorify     
Training a machine to color black and white images    
    
This project is a web application that would take grayscale images and provide you with a color image.    
    
There are 3 implementations used in this project.    
    
1) Using Algorithmia API - This is the API created by Algorithmia.     
2) Using Open CV - This implementation is using the models created, we have written a open Cv program to use that model.    
3) Using Tensorflow - This is an implementation where the model is created by us.    
    
The Following implementation is then deployed to Heroku Application. provided in the link above.    
    
    
Project Structure    
    
.  
├── app.py  
├── Aptfile  
├── backend  
│   ├── colorizeImage.py  
│   ├── colorizeImagetf.py  
│   ├── tensorFlow  
│   │   ├── model_2500.h5  
│   │   ├── model_2500.json  
│   │   ├── model.h5  
│   │   ├── model.h5_6000  
│   │   ├── model.json  
│   │   ├── model.json_6000  
│   │   ├── result  
│   │   ├── result_100_epoch  
│   │   ├── result_2500  
│   │   ├── result_400_epoch  
│   │   ├── tensor_flow_colorify.ipynb  
│   │   ├── tensorflow_model_1.json  
│   │   ├── tensorflow_model.h5  
│   │   ├── tensorflow_model.h5_18000  
│   │   ├── tensorflow_model.json  
│   │   ├── tensorflow_model.json_18000  
│   │   ├── Test  
│   │   │   └── 6.1.01.tiff  
│   │   └── Train  
│   ├── TensorFlowModels  
│   │   ├── model.h5  
│   │   └── model.json  
│   ├── usingAlgorithmiaApi.py  
│   ├── usingOpenCVMethod.py  
│   └── usingTensorFlow.py  
├── getModels.sh  
├── node_modules  
│   └── fullpage.js  
│       ├── dist  
│       │   ├── fullpage.css  
│       │   ├── fullpage.extensions.min.js  
│       │   ├── fullpage.js  
│       │   ├── fullpage.min.css  
│       │   ├── fullpage.min.css.map  
│       │   ├── fullpage.min.js  
│       │   └── fullpage.min.js.map  
│       ├── LICENSE  
│       ├── package.json  
│       ├── README.md  
│       └── vendors  
│           ├── easings.js  
│           ├── easings.min.js  
│           ├── easings.min.js.map  
│           ├── scrolloverflow.js  
│           ├── scrolloverflow.min.js  
│           └── scrolloverflow.min.js.map  
├── package-lock.json  
├── Procfile  
├── pts_in_hull.npy  
├── README.md  
├── References  
│   └── References.txt  
├── requirements.txt  
├── static  
│   ├── css  
│   │   ├── imagePreview.css  
│   │   └── template.css  
│   ├── graphs  
│   ├── js  
│   │   ├── imagePreview.js  
│   │   └── template.js  
│   ├── overviewImages  
│   ├── result  
│   └── uploads  
└── templates  
    └── home.html  
  
22 directories, 50 files  
