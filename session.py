from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:bk6yq5chf@localhost:3306/blog"
)
Session = sessionmaker(bind=engine)  # klasa
Session = Session()  # instancja klasy
