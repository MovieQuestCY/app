from sqlalchemy.ext.asyncio import create_async_engine

class Database:
    def __init__(self):
        #Change the connection string to your own
        self.engine = create_async_engine("mysql+asyncmy://root:p4ssw0rd@db.neuvy.eu:3306") 

    async def get_engine(self):
        return self.engine
    
    async def get_connection(self):
        return await self.engine.connect()
    
    async def close_connection(self, connection):
        await connection.close()
