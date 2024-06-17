// app/routes/api.js
import express from 'express';
import UserController from '../controllers/user';
import BlockchainService from '../services/blockchain';
import AnalyticsService from '../services/analytics';

const router = express.Router();

router.get('/users/:id', UserController.getUser);
router.post('/users', UserController.createUser);
router.get('/balance/:address', BlockchainService.getBalance);
router.post('/transactions', AnalyticsService.trackTransaction);

export default router;
