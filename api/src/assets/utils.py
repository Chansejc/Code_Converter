from src import db

class UserQuery(db.Query):
    def __init__(self, username, sessiontime=None):
        if sessiontime: self.sessiontime = sessiontime
        self.username = username
