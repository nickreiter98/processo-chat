import pm4py
import os
from pathlib import Path

def visualize_process(file_path:str):
    
    path = Path(os.getcwd())
    path = path.joinpath(file_path)

    log = pm4py.read_xes(str(path))
    bpmn = pm4py.discovery.discover_bpmn_inductive(log)
    pm4py.vis.save_vis_bpmn(bpmn, "first_try.png")   
