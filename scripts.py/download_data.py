

from roboflow import Roboflow
rf = Roboflow(api_key="tDGpLNVSs4zJ1OVGt0Gg")
project = rf.workspace("marks-workspace-chqhs").project("pollinator_monitor_vb")
version = project.version(2)
dataset = version.download("yolov8")

