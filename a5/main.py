from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, String, Integer  # criar o mecanismo do banco de dados, e os atributos da tabela
from sqlalchemy.ext.declarative import declarative_base  # é onde será mapeada a classe que vai criar a tabela
from sqlalchemy.orm import Session, sessionmaker  # Session é um tipo, sessionmaker é para configurar o banco de dados
from pydantic import BaseModel  # para utilizar em classes para declarar atributos que serao entradas para os registros

app = FastAPI()

# SqlAlchemt
BASE_URL = "sqlite:///dataset_livros.db"  # qual banco e o nome do banco de dados

# cria o mecanismo do banco de dados
engine = create_engine(BASE_URL)

# configura o mecanismo
SessionLocal = sessionmaker(engine)  # é para acessar o banco de dados

Base = declarative_base()  # instanciando o declarative_base

class User(Base):  # estamos informando ao python que a classe é uma tabela
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)  # aqui estamos indicando o tipo dentro do sqlalchemy, por isso column e Integer. index indica que vai ser autoincrement
    username: str = Column(String, nullable=False)  # nullable=False é para incluir o not null

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db  # yield é um tipo de return, ele vai disponibilizar algo. a gente não está utilizando o return pois precisamos utilizar o finally em seguida para fechar o banco
    finally:
        db.close()  # sempre se deve fechar o db logo depois de realizar alguma operação

class UserBase(BaseModel):  # basemodel é do pydantic, e é aqui que o usuario vai poder realizar alterações
    username: str

@app.post("/user")
def create_user(user: UserBase, db: Session = Depends(get_db)):  # db é uma sessão (tipo), ela vai consultar o banco de dados
    db_user = User(username = user.username)  # acessando o atributo username da classe user_db e incluindo na classe User
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/user")  # acessar todos os usuarios
def read_users(db: Session = Depends(get_db)):  
    users = db.query(User).all()
    return {"Users": users}

@app.get("/users/{id_user}")
def read_user(id_user: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id_user).all()  # precisa do all ou first para retornar o valor com um valor de dicionario e nao com o objeto do banco de dados
    return {"user": user}