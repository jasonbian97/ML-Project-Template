
from argparse import ArgumentParser
import os

readme_str = """
## Project Structure

**planning**: Contains miscellaneous files. It could be useful papers, vague thoughts, etc.

**data**: 

- raw. Raw data files. e.g. soft-link to my local ~/AllDataSets
- cache: Preprocessed datasets that don’t need to be re-generated every time you perform an analysis.
- munge: Preprocessing data munging code, the outputs of which are put in cache.

**config**: Contains parameter files to run scripts, e.g. .json,.yaml files. I can adjust hyperparam here. 

**src**:

- scripts. All the scripts. e.g. train.py, test.py
- lib: Helper library functions. 

**results**: 

- **logs**: Output of scripts and any automatic logging. e.g. tensorboard output.

- **reports**: Output reports and content that might go into reports such as tables. e.g. it contains Latex project.

**README**: Notes that orient any newcomers to the project.

**TODO**: list of future improvements and bug fixes you plan to make.
"""

todo_str = """
# TODO List
- Task1: XXX
- Task2: XXX
"""

def main(args):
    # create dirs
    os.makedirs(os.path.join(args.project_dir,"data"))
    os.makedirs(os.path.join(args.project_dir, "config"))
    os.makedirs(os.path.join(args.project_dir, "src"))
    os.makedirs(os.path.join(args.project_dir, "results"))

    os.makedirs(os.path.join(*[args.project_dir, "data", "raw"]))
    os.makedirs(os.path.join(*[args.project_dir, "data", "cache"]))
    os.makedirs(os.path.join(*[args.project_dir, "data", "munge"]))
    os.makedirs(os.path.join(*[args.project_dir, "results","logs"]))
    os.makedirs(os.path.join(*[args.project_dir, "results", "report"]))

    os.makedirs(os.path.join(*[args.project_dir, "src", "scripts"]))
    os.makedirs(os.path.join(*[args.project_dir, "src", "lib"]))
    
    with open(os.path.join(args.project_dir, "README.md"), "w") as file1:
        # Writing data to a file 
        file1.write(readme_str)

    with open(os.path.join(args.project_dir, "TODO.md"), "w") as file1:
        # Writing data to a file
        file1.write(todo_str)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--project_dir', dest='project_dir',
                        help='input the project directory',
                        default="./MyNewProject", type=str)

    args = parser.parse_args()

    # train
    main(args)
