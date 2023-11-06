import cv2
import numpy as np
import os


# Pre-trained models from YOLO community - to be referenced
weights_path = "yolov3.weights"

config_path = "yolov3.cfg"

# Check if the weights and cfg files are in the right path
if not os.path.isfile(weights_path):
    raise ValueError("Weights file yolov3.weights not found!")

if not os.path.isfile(config_path):
    raise ValueError("Config file yolov3.cfg not found!")

net = cv2.dnn.readNet(weights_path, config_path)
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Make the image 2D
layer_names = net.getLayerNames()
output_layers_indices = net.getUnconnectedOutLayers().flatten()
output_layers = [layer_names[i - 1] for i in output_layers_indices]


# Loading image

image = cv2.imread("image/image.jpeg")
image = cv2.resize(image, None, fx=0.4, fy=0.4)
height, width, channels = image.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Showing information on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Label and display the label with the confidence that the prediction is what it thinks it is
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = np.random.uniform(0, 255, size=(3,))
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, f"{label}: {int(confidence * 100)}%", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()