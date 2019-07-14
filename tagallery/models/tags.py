from sqlalchemy import Column, String, ForeignKeyConstraint


class Tag(Base):

    __tablename__ = 'image'

    title = Column(String, primary_key=True)
    user_login = Column(String, primary_key=True,
            nullable=False)

    owner = relationship('User', back_populates='images')
    images = relationship('Image', back_populates='images',
            foreign_keys='[TagAsImg.img_path, TagAsImg.tag_title]',
            secondary='tag_as_img')
    permissions = relationship('Permission', back_populates='images')

    __table_args__ = (
            ForeignKeyConstraint([user_login], ['user.login'], ondelete='CASCADE'),
    )
