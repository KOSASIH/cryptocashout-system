// app/controllers/user.js
import { UserController } from '../models/user';
import { WalletController } from '../models/wallet';
import { TransactionController } from '../models/transaction';

class UserController {
  async getUser(req, res) {
    const user = await UserController.findById(req.params.id);
    res.json(user);
  }

  async createUser(req, res) {
    const user = new UserController(req.body);
    await user.save();
    res.json(user);
  }

  async getWallet(req, res) {
    const wallet = await WalletController.findOne({ userId: req.params.id });
    res.json(wallet);
  }

  async createTransaction(req, res) {
    const transaction = new TransactionController(req.body);
    await transaction.save();
    res.json(transaction);
  }
}

export default UserController;
