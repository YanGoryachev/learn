from sqlalchemy import create_engine, select, insert, delete, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv()
url = getenv("URL")
eng = create_engine(url=url)


class Base(DeclarativeBase):
    pass

class State(Base):

    __tablename__ = "state" # Выбрать имя таблицы на выбор

    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column()

class Check:
    
    def __init__(self, db, eng):
        self.db = db
        self.eng = eng

    def check_database(self, name_table):
        self.db.metadata.create_all(eng)
        return {"error":0}

ses = sessionmaker(eng)

class DataBase:
    
    def __init__(self, db, session):
        self.session = session
        self.db = db

    def select_data(self):
        with self.session() as ses:
            res = ses.execute(select(self.db))
            result = res.scalars().all()

            return result
    
    def insert_data(self, **kwargs):
        with self.session() as ses:
            ses.execute(insert(self.db).values(**kwargs))

            ses.commit()
    
    def delete_data(self, id):
        with self.session() as ses:
            ses.execute(delete(self.db).filter(self.db.id == id))

            ses.commit()
    
    def update_data(self, id, **kwargs):
        with self.session() as ses:
            ses.execute(update(self.db).values(**kwargs).filter(self.db.id == id))

            ses.commit()
            
