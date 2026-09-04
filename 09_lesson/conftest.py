import pytest
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, future=True)


@pytest.fixture
def db_connection():
    conn = engine.connect()
    yield conn
    conn.close()