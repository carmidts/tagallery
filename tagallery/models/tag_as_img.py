class TagAsImg(Base):
    __tablename__ = 'tag_as_img'

    img_path = Column(String, primary_key=True, nullable=False)
    tag_title = Column(String, primary_key=True, nullable=True)

    __tablen_args = (
            ForeignKeyConstraint([tag_title], ['tag.title'], ondelete='CASCADE'),
            ForeignKeyConstraint([img_path], ['image.path'], ondelete='CASCADE'),
    )
