from sqlalchemy import Column, Integer, VARCHAR, UniqueConstraint, SMALLINT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sqlal
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(VARCHAR(50), nullable=True)
    password = Column(VARCHAR(300), nullable=False)
    email = Column(VARCHAR(40))

    UniqueConstraint(username, name='username')
    UniqueConstraint(email, name='email')

#ForeignKey("main_table.id")
class MusicalComposition(Base):
    __tablename__ = 'musical_compositions'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey(f'{User.__tablename__}.{User.id.name}'), nullable=False)
    url = Column(VARCHAR(60), nullable=True)
    user = relationship('User', backref='musical_composition')
