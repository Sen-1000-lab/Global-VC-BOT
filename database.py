import asyncpg

from config import DATABASE_URL

pool = None


async def connect_db():
    global pool

    if pool is None:
        pool = await asyncpg.create_pool(
            DATABASE_URL,
            min_size=1,
            max_size=10
        )

        print("✅ Database Connected")


async def get_pool():
    return pool


async def create_tables():

    pool = await get_pool()

    async with pool.acquire() as conn:

        # ユーザー
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """)

        # サーバー
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS guilds (
            guild_id BIGINT PRIMARY KEY,
            owner_id BIGINT,
            joined_at TIMESTAMP DEFAULT NOW()
        )
        """)

        # ルーム
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_id SERIAL PRIMARY KEY,
            owner_id BIGINT,
            room_name TEXT,
            room_type TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """)

        print("✅ Tables Created")
