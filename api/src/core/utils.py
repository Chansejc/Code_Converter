from typing import Dict, List, Tuple
from src import db
from src.accounts import models
import time
import os

class NoFile(Exception): 
    pass

class CacheHandler:
    def __init__(self) -> None:
        self.active = True
        self.max_age = 990000000000 # time in nanoseconds
        self.init_time: int = time.time_ns()
        self.active_users: List[Dict[str, str]] = []

        if not self.active:
            pass
    
    def check_active(self):
        time_spent = (time.time_ns() - self.init_time)
        if time_spent > self.max_age:
            self.active = False
            
class UserCache: #Meant for use when a user goes to look at their profile and sees all of the files that haven't been deleted in the past.
    def __init__(self, email):
        self.email = email
        self.user =  list(filter(lambda x: x.email == self.email, db.session.query(models.User).all()))[0]
        self.files = self.get_files() 
        self.running = self.validate_session()
        self.root = {}
    
    def validate_session(self):
        pass    

    def get_files(self):
        files: List = list(filter(lambda x: x.id == self.user.id, db.session.query(models.User).all()))

    def __repr__(self) -> str:
        s = ""
        return s 

class FileNode:
    def __init__(self, filename) -> None:
        sig_list = self.break_file(filename)
        self.id: str = sig_list[0] #Actual Filename | First 7 characters
        self.folder: str =sig_list[1] #Signature for the directory it is held in | Characters 8 - 13
        self.user: str = sig_list[2] #ID of the user the file is associated with | the users id
        with open(f"../../smorg/directories/{self.folder}/","r" ) as f:
            content = f.read()
        self.contents: str = content
        
    def break_file(self,filename) -> List[str]:
        return filename.split("_")

    def __repr__(self) -> str:
        return  \
        f"<{self.id.upper()}: {self.contents.__repr__()}>"
            

