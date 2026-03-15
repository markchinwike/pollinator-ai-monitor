

from roboflow import Roboflow
rf = Roboflow(api_key="tDGpLNVSs4zJ1OVGt0Gg")
project = rf.workspace("marks-workspace-chqhs").project("pollinator_monitor_vb")
version = project.version(2)
dataset = version.download("yolov8")

yolo task=detect mode=train model=yolov8n.pt data=Pollinator_Monitor_vb-2/data.yaml epochs=25 imgsz=640 plots=True