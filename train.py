from ultralytics import YOLO
import torch

#model load
model = YOLO("architecture/yolov8n.yaml")    # train in nano model
# model = YOLO("architecture/yolov8s.yaml")    # train in small model
# model = YOLO("architecture/yolov8m.yaml")    # train in medium model
# model = YOLO("architecture/yolov8l.yaml")    # train in large model
# model = YOLO("architecture/yolov8x.yaml")    # train in xlarge model



# Start training
model.train(data="config.yaml", epochs=150, batch=16)

# Save trained model
#model.save("Path_hole.pt")