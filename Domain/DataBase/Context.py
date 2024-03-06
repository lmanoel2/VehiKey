from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123456@localhost/vehikey_db')
Session = sessionmaker(bind=engine)
