from pydantic import BaseModel

class LivrosCreate(BaseModel):
    titulo: str
    descricao: str
    numero_paginas: int

class LivrosResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    numero_paginas: int

class LivrosUpdate(BaseModel):
    titulo: str
    descricao: str
    numero_paginas: int