import asyncio
import json
import logging
import os
import ssl
import sys
import time
from typing import Dict, List, Tuple

import aiohttp
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration from environment variables
BACKEND_URL = os.environ.get('BACKEND_URL', 'https://backend.example.com/api')
BACKEND_API_KEY = os.environ.get('BACKEND_API_KEY', 'ecret_api_key')
BACKEND_CERT_FILE = os.environ.get('BACKEND_CERT_FILE', 'path/to/backend_cert.pem')
BACKEND_KEY_FILE = os.environ.get('BACKEND_KEY_FILE', 'path/to/backend_key.pem')

# Load backend certificate and key
with open(BACKEND_CERT_FILE, 'rb') as f:
    backend_cert = serialization.load_pem_x509_certificate(f.read(), default_backend())
with open(BACKEND_KEY_FILE, 'rb') as f:
    backend_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

# Set up SSL context
ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain(BACKEND_CERT_FILE, keyfile=BACKEND_KEY_FILE)

class ATMCommunication:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.backend_url = BACKEND_URL
        self.backend_api_key = BACKEND_API_KEY

    async def send_request(self, method: str, endpoint: str, data: Dict = None) -> Tuple[int, Dict]:
        """
        Send a request to the backend service
        """
        headers = {'Authorization': f'Bearer {self.backend_api_key}'}
        async with self.session.request(method, f'{self.backend_url}/{endpoint}', json=data, headers=headers) as response:
            response_data = await response.json()
            return response.status, response_data

    async def get_user_balance(self, user_id: int) -> Tuple[int, Dict]:
        """
        Get the user's balance from the backend service
        """
        return await self.send_request('GET', f'users/{user_id}/balance')

    async def process_transaction(self, transaction_data: Dict) -> Tuple[int, Dict]:
        """
        Process a transaction with the backend service
        """
        return await self.send_request('POST', 'transactions', data=transaction_data)

    async def get_fiat_exchange_rate(self, fiat_currency: str) -> Tuple[int, Dict]:
        """
        Get the current fiat exchange rate from the backend service
        """
        return await self.send_request('GET', f'exchange_rates/{fiat_currency}')

    async def close(self):
        """
        Close the client session
        """
        await self.session.close()

async def main():
    communication = ATMCommunication()
    try:
        # Example usage
        user_id = 123
        balance_status, balance_data = await communication.get_user_balance(user_id)
        print(f'User {user_id} balance: {balance_data["balance"]}')

        transaction_data = {'amount': 10.0, 'currency': 'BTC'}
        transaction_status, transaction_data = await communication.process_transaction(transaction_data)
        print(f'Transaction processed: {transaction_data["transaction_id"]}')

        fiat_currency = 'USD'
        exchange_rate_status, exchange_rate_data = await communication.get_fiat_exchange_rate(fiat_currency)
        print(f'Fiat exchange rate for {fiat_currency}: {exchange_rate_data["rate"]}')
    finally:
        await communication.close()

if __name__ == '__main__':
    asyncio.run(main())
