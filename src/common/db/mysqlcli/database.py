from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@798@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql://root:admin@798@182.254.159.57:3306/db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin798@182.254.159.57:3306/web"
engine=create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()