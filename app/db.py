from sqlmodel import SQLModel, create_engine

# All table models need to be imported before `SQLModel.metadata.create_all` is called.
# We'll import everything here to be safe.
from app import models

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def init_db():
    SQLModel.metadata.create_all(engine)
