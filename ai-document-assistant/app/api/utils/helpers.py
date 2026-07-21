import os
import hashlib



def create_folder(path):

    if not os.path.exists(path):

        os.makedirs(path)



def get_file_hash(file_path):


    sha256 = hashlib.sha256()


    with open(file_path,"rb") as file:


        while chunk := file.read(4096):

            sha256.update(chunk)



    return sha256.hexdigest()



def allowed_file(filename):


    return filename.lower().endswith(
        ".pdf"
    )