// app/services/blockchain.js
import Web3 from 'web3';

class BlockchainService {
  async getBalance(address) {
    const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));
    const balance = await web3.eth.getBalance(address);
    return balance;
  }
}

export default BlockchainService;
