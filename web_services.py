from os.path import exists
import uuid 
import os
import shutil
from pyparsing import opAssoc


def save_file_to_keep(file_code):
    dst_path="videos/keepers/"+ file_code+".mp4"
    src_path = "videos/" + file_code+".mp4"
    shutil.move(src_path, dst_path)
        

    
