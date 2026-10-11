from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy import select, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///AlunosDt.db")
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    curso = Column(String)
    nota = Column(Float)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

alunos = [Aluno(nome="Dantao", curso="Informática", nota=9.0),
        Aluno(nome="Luiz", curso="Informática", nota=9.5),
        Aluno(nome="Calazans", curso="Eletrônica", nota=8.5),
        Aluno(nome="Judazetti", curso="Eletrônica", nota=8.0),
        Aluno(nome="Patapa", curso="Informática", nota=10.0)]

session.query(Aluno).delete()
session.add_all(alunos)
session.commit()

# Q1
print("\nA) Todos os alunos")
query = select(Aluno)

for linha in session.execute(query):
    print(linha.Aluno.nome, linha.Aluno.curso, linha.Aluno.nota)

# Q2
print("\nB) Nome e nota")
query = select(Aluno.nome, Aluno.nota)

for linha in session.execute(query):
    print(linha.nome, linha.nota)

# Q3
print("\nC) Alunos de Informática")
query = select(Aluno).where(Aluno.curso == 'Informática')

for linha in session.execute(query):
    print(linha.Aluno.nome)

# Q4
print("\nD) Alunos com nota maior ou igual a 7")
query = select(Aluno).where(Aluno.nota >= 7).order_by(desc(Aluno.nota))

for linha in session.execute(query):
    print(linha.Aluno.nome, linha.Aluno.nota)

# Q5
print("\nE) Quantidade de alunos por curso")
query = (
    select(Aluno.curso, func.count(Aluno.id).label('qtd')).group_by(Aluno.curso))

for linha in session.execute(query):
    print(linha.curso, linha.qtd)

session.close()