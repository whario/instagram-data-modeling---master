import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

#import Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    date_post = Column(DateTime, nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_text = Column(String(250), nullable=False)

class Media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    type_media = Column(Enum(), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')