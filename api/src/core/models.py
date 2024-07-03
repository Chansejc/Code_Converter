from threading import activeCount
from typing import Dict, List, Tuple
from src import db
from src.accounts import models as account_models
import time
import zlib
import os

class NoFile(Exception): 
    pass

class DecompressionError:
    Value = Exception(ValueError)
    zlib = zlib.error
    UserNotFound = account_models.UserNotFound
    File = FileNotFoundError
    Type = TypeError

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
        self.user =  account_models.get_user(self.email, account_models.User) 
        self.files = self.get_files() 
        self.running = self.validate_session()
    
    def validate_session(self):
        pass    

    def get_files(self) -> List | None:
        files = None
        try:
            user_id:int =  self.user.id
            files = os.listdir(f"../../smorg/{user_id}")
        except [account_models.UserNotFound, FileNotFoundError] as e:
            if e == account_models.UserNotFound: raise account_models.UserNotFound
            if e == FileNotFoundError: raise FileNotFoundError
        finally:
            return files
            

    def __repr__(self) -> str:
        s = ""
        return s 

class FileNode:
    def __init__(self, filename: str, user: account_models.User, folder: str) -> None:
        self.name: str = filename 
        self.folder: str = folder
        self.user: account_models.User = user 
        with open(f"../../smorg/directories/{self.folder}/{self.name}","r" ) as f:
            content = f.read()
        self.contents: str = content
        self.lines: int = len(self.contents.split('/n'))
        
    def break_file(self,filename) -> List[str]:
        return filename.split("_")

    def __repr__(self) -> str:
        return f"<{self.user.id} : {self.folder.upper()}/{self.name} : Length {self.lines}>"

def genFilename():
    import random
    num = random.choice(range(0,1000000000))
    return num
