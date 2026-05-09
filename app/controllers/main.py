from fastapi import FastAPI, Depends
from sqlalchemy.orm import session
from app.models.database import sessionlocal, livro, init_db
from pydantic import BaseModel


app = FastAPI()

init_db()

class livroSchama(BaseModel):
    titulo = str
    autor = str

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/livros')
def listar_livros(db: session = Depends(get_db)):
    return db.query(livro).all()


@app.post('/livro')
def criar_livro(livro: livroSchama, db: session = Depends(get_db)):
    novo_livro = livro(titulo = livro.titulo, autor = livro.autor)
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro
    
