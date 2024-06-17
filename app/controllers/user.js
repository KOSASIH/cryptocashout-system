// app/controllers/user.js
import { UserController } from '../models/user';

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
}

export default UserController;
