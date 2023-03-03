from models.db import Database
from sqlalchemy import text

async def get_all_users():
    db = Database()
    query = text("SELECT * FROM users")
    connection = await db.get_connection()
    result = await connection.execute(query)
    await db.close_connection(connection)
    print(result.keys())
    return result
