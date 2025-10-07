import os
import shutil


def copy_src_dest(src, dest):
    if not os.path.isfile(src):
        if not os.path.exists(dest):
            os.mkdir(dest)
        else:
            shutil.rmtree(dest)
            os.mkdir(dest)
        src_contents = os.listdir(src)
        for content in src_contents:
            copy_src_dest(f"{src}/{content}", f"{dest}/{content}")
    else:
        shutil.copy(src, dest)
