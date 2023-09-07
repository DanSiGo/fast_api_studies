from sqlalchemy import Column, String, Integer  # criar o mecanismo do banco de dados, e os atributos da tabela
from sqlalchemy.ext.declarative import declarative_base  # é onde será mapeada a classe que vai criar a tabela

Base = declarative_base()  # instanciando o declarative_base

class Livros(Base):  # estamos informando ao python que a classe é uma tabela
    __tablename__ = "livros"

    id: int = Column(Integer, primary_key=True, index=True)  # aqui estamos indicando o tipo dentro do sqlalchemy, por isso column e Integer. index indica que vai ser autoincrement
    titulo: str = Column(String, nullable=False)  # nullable=False é para incluir o not null
    descricao: str = Column(String, nullable=False)
    numero_paginas: int = Column(String, nullable=False)