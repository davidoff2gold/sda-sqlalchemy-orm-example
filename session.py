from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:bk6yq5chf@localhost:3306/blog"
)
Session = sessionmaker(bind=engine)  # klasa
session = Session()  # instancja klasy
