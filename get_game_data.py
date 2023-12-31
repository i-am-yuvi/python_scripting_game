import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"

# find all the directories that matches the "game" string
def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory:
                path = os.path.join(source, directory)
                game_paths.append(path)
        
        break

    return game_paths


#get the source & target directory and combine them with the cwd 
def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    print(game_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass your source & target directory")

    source, target = args[1:]
    main(source, target)