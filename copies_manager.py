import os
import shutil
import zipfile
from pathlib import Path


def run_copy(source, destination, logger):
    #TODO: selective of world, world_nether and world_the_end folders only.
    if not os.path.isdir(destination):
        if os.path.isdir(source):
            shutil.copytree(source, destination)

    else:
        logger.info(f"Copy at the location {destination} was already created. May be restarting too fast?")


def list_copies(copies_dir):
    copies = [copy for copy in Path(copies_dir).iterdir()]
    copies.sort()
    copies = [f"{copies_dir}/{copy_name}" for copy_name in copies]
    return copies


def compress(directory):
    return