from sqlalchemy import Table, Column, Integer, String, MetaData
from app.db import meta

payments = Table(
    "payments", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("upi_id", String(50), nullable=False),
    Column("amount", Integer, nullable=False),
    Column("status", String(20), nullable=False),
)