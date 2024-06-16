import asyncio
import logging
import os
import sys
from typing import Dict, List

import aiomysql
import aiohttp
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from atm_software.atm_ui import ATMUI
from atm_software.atm_business_logic import ATMBusinessLogic
from atm_software.atm_communication import ATMCommunication
from components.pi_coin_wallet import PiCoinWallet
from components.fiat_currency_converter import FiatCurrencyConverter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration from environment variables
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'atm_database')

BACKEND_URL = os.environ.get('BACKEND_URL', 'https://backend.example.com/api')
BACKEND_API_KEY = os.environ.get('BACKEND_API_KEY', 'secret_api_key')
BACKEND_CERT_FILE = os.environ.get('BACKEND_CERT_FILE', 'path/to/backend_cert.pem')
BACKEND_KEY_FILE = os.environ.get('BACKEND_KEY_FILE', 'path/to/backend_key.pem')

# Load backend certificate and key
with open(BACKEND_CERT_FILE, 'rb') as f:
    backend_cert = serialization.load_pem_x509_certificate(f.read(), default_backend())
with open(BACKEND_KEY_FILE, 'rb') as f:
    backend_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

class ATMSystem:
    def __init__(self):
        self.atm_ui = ATMUI()
        self.atm_business_logic = ATMBusinessLogic()
        self.atm_communication = ATMCommunication()
        self.pi_coin_wallet = PiCoinWallet()
        self.fiat_currency_converter = FiatCurrencyConverter()

        self.db_pool = aiomysql.create_pool(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

    async def start(self):
        """
        Start the ATM system
        """
        await self.atm_ui.start()
        await self.atm_business_logic.start()
        await self.atm_communication.start()
        await self.pi_coin_wallet.start()
        await self.fiat_currency_converter.start()

        # Initialize database connection
        async with self.db_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT 1')
                result = await cur.fetchone()
                if result:
                    logger.info('Database connection established')

    async def stop(self):
        """
        Stop the ATM system
        """
        await self.atm_ui.stop()
        await self.atm_business_logic.stop()
        await self.atm_communication.stop()
        await self.pi_coin_wallet.stop()
        await self.fiat_currency_converter.stop()

        # Close database connection
        self.db_pool.close()
        await self.db_pool.wait_closed()

async def main():
    atm_system = ATMSystem()
    try:
        await atm_system.start()
        while True:
            # Main loop
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await atm_system.stop()

if __name__ == '__main__':
    asyncio.run(main())
