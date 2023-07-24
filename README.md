# Welcome to EPICpy-Evaluation
This repo is holds code which evaluates the performance of EPICpy.

# Contents
* [Setup](#Setup)
* [ExperimentRunner.py](#experimentrunnerpy)
* [Output Files](#output-files)
* [Running Files Titled 'ERX.py'](#running-files-titled-erxpy)
* [Files Titled 'ExperimentRunner1.sh'](#files-titled-experimentrunner1sh)
* [Planner Configurations](#planner-configurations)


# Setup
This repo requires access to some version of EPICpy. The EPICpy repo should be contained in the same folder as this repo
i.e. both repos are folders within the same parent folder.


# ExperimentRunner.py

**ExperiementRunner.py** is the main file of this repository. This is where all the evaluation setup,
execution, and recording is handled.

This file can be run using the command:
```commandline
python3 ExperimentRunner.py X
```
Where **X** is a number correlating to a strategy. For more information on which strategy each
number triggers, refer to section [planner-configurations](#planner-configurations).

The attributes recorded during search are as follows:
* Problem Name
* Number of Expansions Taken
* Solve Time
* Setup Time
* Total Number of Possible Facts
* Total Number of Facts in the Final State
* Percentage of Possible Facts in the Final State
* Total Number of Possible Fact Pairings
* Total Number of Fact Pairings in the Final State
* Percentage of Possible Fact Pairings in the Final State
* Number of States which were Novel
* Number of States which were *NOT* Novel
* Percentage of States which were Novel
* Number of Unique Facts Seen
* Number of Methods Used which were Novel
* Number of Methods Used which were *NOT* Novel
* Number of Times a Novel Method was used on a *Not* Novel State (When Using **Novelty Methods No Reset 
Solver** or **Hamming Novelty No Reset Solver**)
* Number of Times a Novel Method was used on a Novel State (When Using **Novelty Methods No Reset 
Solver** or **Hamming Novelty No Reset Solver**)
* If the Returned Plan was Verified
* If the Problem was Solved

Plans are verified is the following conditions are met:
1. The **Model** class being used is an instance of the class **PandaVerifyModel**
2. The **Progress Tracker** class being used is an instance of the class **PandaVerifyFormatTracker**
3. The host system is not Windows


## Output Files
Results files are named after the configuration of the planner as opposed to the number used to 
initiate the evaluation module. Each of these files is a CSV file. 
If the required output file does not exist it is automatically created. If one does exist then
results are appended to the end of the existing file.


# Running Files Titled 'ERX.py'

The directory 'evaluation-runners' contains files of the style 'ERX.py' where X is some number 
which refers to a planner configuration listed in section [Planner Configurations](#planner-configurations).
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
X is some number which refers to a planner configuration listed in section [Planner Configurations](#planner-configurations). These files are SBATCH files which can be used to submit the evaluation of
a planner configuration to the SLURM queue.

From these files, SBATCH attributes such as job time, amount of cores, RAM etc. can be set.

# Planner Configurations

Below is a table showing which planner configuration each number corresponds to.

| Number | Solver                                     | Search Queue                | Heuristic                              | Model Class  | Progress Tracker |
|--------|--------------------------------------------|-----------------------------|----------------------------------------|--------------|------------------|
| 1      | Partial Order Novelty Light                | GBFS                        | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 2      | Partial Order Novelty Light                | GBFS                        | Seen States Pruning                    | Panda Verify | Panda Verify     |
| 3      | Partial Order Novelty Light                | GBFS                        | Tree Distance (Seen States Pruning)    | Panda Verify | Panda Verify     |
| 4      | Partial Order Novelty                      | GBFS                        | N/A                                    | Panda Verify | Panda Verify     |
| 5      |                                            | GBFS                        | Tree Distance                          | Panda Verify | Panda Verify     |
| 6      | Partial Order Novelty                      | Novelty Tree Distance GBFS  | Tree Distance (Seen States Pruning)    | Panda Verify | Panda Verify     |
| 7      | Partial Order Novelty Light                | GBFS (Newest First)         | Tree Distance Seen States Pruning      | Panda Verify | Panda Verify     |
| 8      |                                            | GBFS (Newest First)         | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 9      |                                            | GBFS (Hamming Distance)     | Tree Distance (Seen States Pruining)   | Panda Verify | Panda Verify     |
| 10     | Patial Order Novelty (No Reset)            | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 11     | Partial Order Novelty (Level 2)            | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 12     | Partial Order Novelty (Methods)            | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 13     | Partial Order Novelty                      | Nocelty GBFS (Oldest First) |                                        | Panda Verify | Panda Verify     |
| 14     |                                            | GBFS                        | Landmarks                              | Panda Verify | Panda Verify     |
| 15     | Partial Order Novelty                      | Novelty Tree Distance GBFS  | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 16     | Partial Order Novelty (Level 2 - No Reset) | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 17     | Partial Order Novelty (Methods)            | Novelty GBFS (Oldest First) |                                        | Panda Verify | Panda Verify     |
| 18     | Partial Order Novelty (No Reset)           | Novelty Tree Distance GBFS  | Tree Distance (Seen States Pruning)    | Panda Verify | Panda Verify     |
| 19     | Partial Order Novelty (No Reset)           | Novelty Tree Distance GBFS  | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 20     | Partial Order Novelty                      | Novelty Tree Distance GBFS  | Landmarks                              | Panda Verify | Panda Verify     |
| 21     | Partial Order Novelty (No Reset)           | Novelty Tree Distance GBFS  | Landmarks                              | Panda Verify | Panda Verify     |
| 22     |                                            | GBFS (Hamming Distance)     | Landmarks                              | Panda Verify | Panda Verify     |
| 23     | Partial Order Novelty Light                | GBFS (Tree Distance)        | Landmarks                              | Panda Verify | Panda Verify     |
| 24     | Partial Order Novelty Light                | GBFS (Newest First)         | Landmarks                              | Panda Verify | Panda Verify     |
| 25     | Partial Order Novelty Light                | GBFS (Tree Distance)        | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 26     |                                            | GBFS (Landmarks)            | Tree Distance (Seen States Pruning)    | Panda Verify | Panda Verify     |
| 27     |                                            | GBFS (Landmarks)            | Hamming Distance (Seen States Pruning) | Panda Verify | Panda Verify     |
| 28     | Partial Order Novelty Methods & Tasks      | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 29     | Partial Order Novelty Methods & Tasks      | Novelty GBFS (Oldest First) |                                        | Panda Verify | Panda Verify     |
| 30     | Partial Order Hamming Novelty              |                             |                                        | Panda Verify | Panda Verify     |
| 31     | Partial Order Hamming Novelty (No Reset)   |                             |                                        | Panda Verify | Panda Verify     |
| 32     | Partial Order Novelty Methods (No Reset)   | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 33     | Partial Order Novelty Methods Only         | Novelty GBFS                |                                        | Panda Verify | Panda Verify     |
| 34     | Partial Order Novelty Light                | GBFS                        | Landmarks (No Reachability)            | Panda Verify | Panda Verify     |
