from abc import ABC, abstractmethod

class Mydb(ABC):
    @abstractmethod
    def commit(self):
        pass
    def rollback(self):
        pass

class Oracle(Mydb):
    def commit(self):
        print("commit of oracle")
    def rollback(self):
        print("rollback of oracle")

class Mysql(Mydb):
    def commit(self):
        print("commit of mysql")
    def rollback(self):
        print("rollback of mysql")


def comman(db):
    db.commit()
    db.rollback()

comman(Oracle())
comman(Mysql())
