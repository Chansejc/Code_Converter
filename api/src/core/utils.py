from typing import Dict, List
import os

class NoFile(Exception): 
    pass

class SessionHandler:
    def __init__(self) -> None:
        self.active_users: List[Dict[str, str]] = []

class Cacher:
    def __init__(self, username, session):
        self.session_tag = session
        self.running = self.validate_session()
        self.fs = f"/mnt/c/MyStuff/projects/converter/api/smorg/{username}"
        self.root = {}
    
    def validate_session(self):
        pass

    def __repr__(self) -> str:
        s = ""
        return s 


class NoFile(Exception):
    pass

class FileNode:
    def __init__(self, path, name) -> None:
        self.name = name
        self.path = path
        self.contents: str = self.getcontents()

    def getcontents(self):
        content: str = ""
        try:
            with open(self.path, "r") as f:
                content = f.read()
        except Exception as e:
            content = "None"
            if e == FileNotFoundError:
                raise NoFile
        finally:
            return content
    
    def __repr__(self) -> str:
        return f"<File: {self.name}>"

class FolderNode:
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path
        self.contents: List[FileNode] = [
                FileNode(os.path.join(self.path, i), i) 
                for i in os.listdir(os.path.join(self.path,self.name))
                ]
    def __repr__(self) -> str:
        return  \
        f"<{self.name.upper()}: {self.contents.__repr__()}>"
            

