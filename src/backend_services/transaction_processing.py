import asyncio
import json
import logging
import os
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

class TransactionProcessing:
    def __init__(self):
        self.db_pool = get_db_pool()

    async def process_transaction(self, transaction_data: Dict) -> Dict:
        """
        Process a transaction
        """
        async with self.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('INSERT INTO transactions (user_id, amount, currency) VALUES (%s, %s, %s)', (
                    transaction_data['user_id'],
                    transaction_data['amount'],
                    transaction_data['currency']
                ))
                transaction_id = await cur.lastrowid
                return {'transaction_id': transaction_id}

    async def get_transaction_history(self, user_id: int) -> List[Dict]:
        """
        Get a user's transaction history
        """
        async with self.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM transactions WHERE user_id = %s', (user_id,))
                transaction_data = await cur.fetchall()
                return [{'transaction_id': row['id'], 'amount': row['amount'], 'currency': row['currency']} for row in transaction_data]

async def main():
    transaction_processing = TransactionProcessing()
    try:
        # Example usagetransaction_data = {'user_id': 123, 'amount': 10.0, 'currency': 'BTC'}
        transaction_id = await transaction_processing.process_transaction(transaction_data)
        print(transaction_id)

        user_id = 123
        transaction_history = await transaction_processing.get_transaction_history(user_id)
        print(transaction_history)
    finally:
        await transaction_processing.db_pool.close()
        await transaction_processing.db_pool.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
