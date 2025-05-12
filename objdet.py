from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11n.pt")

# Perform object detection on an image using the model
results = model("https://ultralytics.com/images/bus.jpg")

for res in results:
  res.save("busannotated.jpg")

