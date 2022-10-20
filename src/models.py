import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy import render_er



Base = declarative_base()

PostGuardado = Table("posts_guardados", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("posts_id", Integer, ForeignKey("posts.id")),
    Column("usuarios_id", Integer, ForeignKey("usuarios.id"))
    
)

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    cel = Column(Integer, nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    posts = relationship('Post', backref='usuarios', lazy=True)
    historias = relationship('Historia', backref='usuarios', lazy=True)
    

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False) 
    Hora = Column(DateTime, nullable=False)
    contenido = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    etiquetas = Column(Integer, nullable=False)
    hashtag = Column(DateTime, nullable=False)
    usuarios_ID = Column(Integer, ForeignKey("usuarios.id"))
    posts_guardados = relationship('Usuario', secondary=PostGuardado, lazy="subquery", backref=backref('posts', lazy=True))
   
    


class Historia(Base):
    __tablename__ = 'historias'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Hora = Column(DateTime, nullable=False)
    contenido = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    etiquetas = Column(Integer, nullable=False)
    hashtag = Column(DateTime, nullable=False)
    Usuario_ID = Column(Integer, ForeignKey("usuarios.id"))




   





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')