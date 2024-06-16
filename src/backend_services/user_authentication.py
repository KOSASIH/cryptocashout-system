import asyncio
import json
import logging
import os
import secrets
from typing import Dict, List

import aiohttp
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration from environment variables
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'backend_database')

# Load database connection
async def get_db_pool():
    return await aiomysql.create_pool(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

class UserAuthentication:
    def __init__(self):
        self.db_pool = get_db_pool()

    async def authenticate_user(self, username: str, password: str) -> Dict:
        """
        Authenticate a user
        """
        async with self.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM users WHERE username = %s', (username,))
                user_data = await cur.fetchone()
                if user_data:
                    # Verify password
                    password_hash = user_data['password_hash']
                    if secrets.compare_digest(password, password_hash):
                        return {'user_id': user_data['id'], 'username': user_data['username']}
                    else:
                        return {'error': 'Invalid password'}
                else:
                    return {'error': 'User not found'}

    async def register_user(self, username: str, password: str) -> Dict:
        """
        Register a new user
        """
        async with self.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('INSERT INTO users (username, password_hash) VALUES (%s, %s)', (username, secrets.hash_password(password)))
                user_id = await cur.lastrowid
                return {'user_id': user_id, 'username': username}

async def main():
    user_auth = UserAuthentication()
    try:
        # Example usage
        username = 'john_doe'
        password = 'my_secret_password'
        auth_data = await user_auth.authenticate_user(username, password)
        print(auth_data)

        new_username = 'jane_doe'
        new_password = 'another_secret_password'
        register_data = await user_auth.register_user(new_username, new_password)
        print(register_data)
    finally:
        await user_auth.db_pool.close()
        await user_auth.db_pool.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
