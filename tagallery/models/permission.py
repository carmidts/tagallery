class Permission(Base):
    __tablename__ = 'permission'

    tag = Column(String, primary_key=True, nullable=False)
    tag_owner = Column(String, primary_key=True, nullable=False)
    to_user = Column(String, primary_key=True, nullable=False)

    __tablen_args = (
            ForeignKeyConstraint([tag], ['tag.title'], ondelete='CASCADE'),
            ForeignKeyConstraint([tag_owner], ['tag.owner'], ondelete='CASCADE'),
            ForeignKeyConstraint([to_user], ['user.login'], ondelete='CASCADE'),
    )
