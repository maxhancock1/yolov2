# YOLO (You Only Look Once): Used in research for Neuroprosthesis for object detection and classification 

----

## Background: Object detection plays a crucial role in neuroprosthetics, which are designed to help individuals with disabilities by restoring or supplementing the function of their sight. Detecting objects and classfiying them is very important to allow the patients to live a safe and more comfortable life:

## Instructions 

Access to the pre-trained models that are used for 
### For all of the following commands, run within the following: 
```bat
cd /home/root/ObjectDetection/
```
### Install the pre-trained models
```bat
$ wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
```

```bat
$ wget https://pjreddie.com/media/files/yolov3.weights
```

```bat
$ wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

### Output Dog

![](images/dog_output.png)

### Image Output
![](images/image_output.png)
