import uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime

Base = declarative_base()

# Generate a unique_id | uuid v4
def gen_uuid():
    unique_id = str(uuid.uuid4())
    return unique_id

# Generate a random password if user password is not provided
# def random_password(): 
#     pass 

# Database Models | Schemas
class Password(Base):

    __tablename__ = 'hashes'

    id = Column(Integer(), primary_key=True)
    unique_id = Column(String(250), nullable=False, unique=True, default=gen_uuid())
    account = Column(String(80), nullable=False, unique=False)
    password = Column(String(1024), nullable=False) # Use random_password fn here
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        str_repr = {}
        str_repr["unique_id"] = self.unique_id
        str_repr["account"] = self.account
        str_repr["password"] = self.password
        str_repr["date_created"] = self.date_created
        return str_repr

# from sqlalchemy import Column, Integer, String, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# author_publisher = Table(
#     "author_publisher",
#     Base.metadata,
#     Column("author_id", Integer, ForeignKey("author.author_id")),
#     Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
# )

# book_publisher = Table(
#     "book_publisher",
#     Base.metadata,
#     Column("book_id", Integer, ForeignKey("book.book_id")),
#     Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
# )

# class Author(Base):
#     __tablename__ = "author"
#     author_id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     books = relationship("Book", backref=backref("author"))
#     publishers = relationship(
#         "Publisher", secondary=author_publisher, back_populates="authors"
#     )

# class Book(Base):
#     __tablename__ = "book"
#     book_id = Column(Integer, primary_key=True)
#     author_id = Column(Integer, ForeignKey("author.author_id"))
#     title = Column(String)
#     publishers = relationship(
#         "Publisher", secondary=book_publisher, back_populates="books"
#     )

# class Publisher(Base):
#     __tablename__ = "publisher"
#     publisher_id = Column(Integer, primary_key=True)
#     name = Column(String)
#     authors = relationship(
#         "Author", secondary=author_publisher, back_populates="publishers"
#     )
#     books = relationship(
#         "Book", secondary=book_publisher, back_populates="publishers"
#     )
