from sqlalchemy import Column, Boolean, String, Index, DateTime


class User(Base):
    __tablename__ = 'user'

    login = Column(String, primary_key=True, unique=True)
    password = Column(String)

    images = relationship('Image', back_populates='owner',
            cascade='all, delete-orphan',
            foreign_keys='[Image.user_login]')

