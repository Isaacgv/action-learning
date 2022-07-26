from os.path import exists
import uuid 
import os
import shutil
from pyparsing import opAssoc


def save_file_to_keep(filename):
    dst_path="videos/keepers/"+ filename+".mp4"
    src_path = "videos/" + filename+".mp4"
    shutil.move(src_path, dst_path)
        
    
def generate_code():
    return str(uuid.uuid4())[:10]
    
