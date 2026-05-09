import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, column, Integer, String
from sqlalchemy import sessionmaker

SLQLALCHEY_DATABASE_URL = 'postgresql://neondb_owner:npg_mrgpEQcZy14i@ep-odd-dew-aq5rzmdv-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

if SLQLALCHEY_DATABASE_URL.startswith('postgres://'):
    SLQLALCHEY_DATABASE_URL = SLQLALCHEY_DATABASE_URL.replace("postgres://" , "postgresql://")


engine = create_engine(SLQLALCHEY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


class livro(base):
    __tablename__ = 'livros'
    id = column(Integer, primary_key=True, index=True)
    titulo = column(String)
    autor = column(String)

    def init_db():
        base.metadata.creat_all(bind=engine)
