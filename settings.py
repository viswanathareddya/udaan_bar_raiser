import pymongo


class Connection(object):
    def __init__(self):
        self.username = 'bar_raiser'
        self.password = 'BarRaiser'
        self.db_name = 'bar_raiser'
        self.hostname = 'cluster0.okutn.mongodb.net'

    def client(self):
        service = pymongo.MongoClient(
            f"mongodb+srv://{self.username}:{self.password}@{self.hostname}/{self.db_name}?retryWrites=true&w=majority")
        return service[self.db_name]
