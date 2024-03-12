import os
from pathlib import Path
import subprocess

REPO_DIR = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip())
os.chdir(REPO_DIR)
subprocess.run('git clone https://github.com/tensorflow/models', shell=True)
os.chdir('models')
subprocess.run('git reset --hard 9a7c33a', shell=True)
subprocess.run('git clean -df ', shell=True)
os.chdir('research')
print(Path().resolve())

subprocess.run('protoc object_detection/protos/*.proto --python_out=.', shell=True)
subprocess.run('cp object_detection/packages/tf2/setup.py .', shell=True)


