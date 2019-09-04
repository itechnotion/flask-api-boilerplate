import datetime

from database import DB


class Job(object):

    def __init__(self, name):
        self.name = name
        self.created_date = datetime.datetime.utcnow()

    def insert(self):
        if not DB.find_one("jobs", {"name": self.name}):
            DB.insert(collection='jobs', data=self.json())

    def find(self):
        data=DB.find_one("jobs", {"name": self.name})
        return data

    def json(self):
        return {
            'name': self.name,
            'created_date': self.created_date
        }