from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"  # sqlite
SQLALCHEMY_DATABASE_URL = (
    # postgres
    "postgresql://todo:test1234!@localhost/TodoApplicationDatabase"
)
# SQLALCHEMY_DATABASE_URL = (
#     # mysql
#     "mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase"
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},  # sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
