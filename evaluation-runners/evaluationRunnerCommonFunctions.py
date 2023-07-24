import os
import sys

global EPICpy_Path
EPICpy_Path = '../EPICpy/Tests'


# Move working directory to parent folder
working_dir = os.getcwd()

print(working_dir)

if not working_dir.endswith('EPICpy-Evaluation'):
    os.chdir("../")
sys.path.append(os.getcwd())

print(sys.path)
from ExperimentRunner import run_test
