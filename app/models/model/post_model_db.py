from sqlalchemy import Column, Integer, String, Table, MetaData

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('text', String(50))
)