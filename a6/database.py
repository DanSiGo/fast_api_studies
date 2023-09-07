from sqlalchemy import create_engine, Column, String, Integer  # criar o mecanismo do banco de dados, e os atributos da tabela
from sqlalchemy.ext.declarative import declarative_base  # é onde será mapeada a classe que vai criar a tabela
from sqlalchemy.orm import Session, sessionmaker  # Session é um tipo, sessionmaker é para configurar o banco de dados

BASE_URL = "sqlite:///dataset_livros.db"  # qual banco e o nome do banco de dados

# cria o mecanismo do banco de dados
engine = create_engine(BASE_URL)

# configura o mecanismo
SessionLocal = sessionmaker(engine)  # é para acessar o banco de dados

def get_db():
    db = SessionLocal()
    try:
        yield db  # yield é um tipo de return, ele vai disponibilizar algo. a gente não está utilizando o return pois precisamos utilizar o finally em seguida para fechar o banco
    finally:
        db.close()  # sempre se deve fechar o db logo depois de realizar alguma operação
