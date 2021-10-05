from abc import ABC,abstractmethod

class Db(ABC):
    @abstractmethod
    def commit(self):
        print("commit of Db")

    @abstractmethod
    def rollback(self):
        pass
    def dml(self):
        print("dml command")

class Oracle(Db):

    def commit(self):
        print("commit of Oracle")
        super().commit()
    def rollback(self):
        print("rollback of ORacle")

o=Oracle()
o.commit()
o.rollback()

class Mysql(Db):
    def commit(self):
        print("commit of mysql")
        super().commit()
    def rollback(self):
        print("rollback of mysql")

m=Mysql()
m.dml()
class Db2:
    def commit(self):
        print("Comit of Db2")
    def rollback(self):
        print("rollback of Db2")

Db.register(Db2)
print(issubclass(Db2,Db))
d=Db2()
d.commit()

              
