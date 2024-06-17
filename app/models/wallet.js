// app/models/wallet.js
import mongoose from 'ongoose';
import bcrypt from 'bcrypt';

const walletSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  address: String,
  privateKey: String,
  balance: Number,
});

walletSchema.methods.generatePrivateKey = function() {
  const privateKey = bcrypt.hashSync(this.address, 10);
  return privateKey;
};

const Wallet = mongoose.model('Wallet', walletSchema);

export default Wallet;
