# Welcome to EPICpy-Evaluation
This repo is holds code which evaluates the performance of EPICpy.

# Contents
* [Setup](#Setup)


# Setup
This repo requires access to some version of EPICpy. The EPICpy repo should be contained in the same folder as this repo
i.e. both repos are folders within the same parent folder.


# ExperimentRunner.py

What is the file for

When are plans verified

Results

Execution can be resumed with results appended to the results file


# Running Files Titled 'ERX.py'

The directory 'evaluation-runners' contains files of the style 'ERX.py' where X is some number.
These files are a shortcut to running the following command: 
```commandline
python3 ExperimentRunner.py X
```

From these files the problems attempted by the planner are those which are uncommented within
the file.

Note that 'ER' files use the repositories root directory as the working directory.

These files can be run from the command line using the following command:
```commandline
python3 ER1.py
```

This command can also be run from the root directory of the repo using the command:
```commandline
python3 ./evaluation-runners/ER1.py
```

# Files Titled 'ExperimentRunner1.sh'

The directory 'evaluation-runners' contains files of the style 'ExperimentRunnerX.sh' where
X is some number. These files are SBATCH files which can be used to submit the evaluation of
a planner configuration to the SLURM queue.

From these files, SBATCH attributes such as job time, amount of cores, RAM etc. can be set.

# Planner Configurations