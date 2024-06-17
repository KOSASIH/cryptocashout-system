// app/models/user.js
import mongoose from 'ongoose';

const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  balance: Number,
});

const User = mongoose.model('User', userSchema);

export default User;
