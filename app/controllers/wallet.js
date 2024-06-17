// app/controllers/wallet.js
import { WalletController } from '../models/wallet';

class WalletController {
  async getWallet(req, res) {
    const wallet = await WalletController.findById(req.params.id);
    res.json(wallet);
  }

  async createWallet(req, res) {
    const wallet = new WalletController(req.body);
    await wallet.save();
    res.json(wallet);
  }
}

export default WalletController;
