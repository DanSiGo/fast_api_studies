from sqlalchemy.orm import Session
from models import Livros

# Esse arquivo é onde é feito o CRUD, por meio de funções

class LivroCore:

    def create_book(db: Session, livro: Livros):
        db.add(livro)
        db.commit()
        db.refresh(livro)
        return livro
    
    def get_books(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Livros).offset(skip).limit(limit).all()
    
    def get_book(db: Session, livro_id: int):
        return db.query(Livros).filter(Livros.id == livro_id).first()
    
    def update_book(db: Session, livro_id: int, new_data: dict):
        livro = db.query(Livros).filter(Livros.id == livro_id).first()
        for key, value in new_data.items():
            setattr(livro, key, value)
        db.commit()
        db.refresh(livro)
        return livro
    
    def delete_book(db: Session, livro_id: int):
        livro = db.query(Livros).offset(Livros.id == livro_id).first()
        db.delete(livro)
        db.commit()
        db.refresh(livro)  # não precisa do refresh ao deletar algo
        return livro
