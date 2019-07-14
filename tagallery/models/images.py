from sqlalchemy import Column, Boolean, String, Index, DateTime


class Image(Base):
    __tablename__ = 'image'

    path = Column(String, primary_key=True, unique=True)

    user_login = Column(String, nullable=False)
    owner = relationship('User', back_populates='images')
    tags = relationship('Tag', back_populates='images')

    __table_args__ = (
            ForeignKeyConstraint([user_login], ['user.login'], ondelete='CASCADE'),
    )
