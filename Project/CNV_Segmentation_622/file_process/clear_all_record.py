import os

log_path = "../logs"
cp_path = "../checkpoints"
result_path = "../results"

for log in os.listdir(log_path):
    os.remove(os.path.join(log_path,log))

for cp in os.listdir(cp_path):
    os.remove(os.path.join(cp_path,cp))

for result in os.listdir(result_path):
    os.remove(os.path.join(result_path,result))