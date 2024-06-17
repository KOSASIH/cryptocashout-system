// config/environment.js
module.exports = {
  NODE_ENV: 'development',
  PORT: 3000,
  DATABASE_URL: 'ongodb://localhost:27017/cryptocashout',
  BLOCKCHAIN_RPC_URL: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
  ANALYTICS_API_KEY: 'YOUR_ANALYTICS_API_KEY',
  JWT_SECRET_KEY: 'YOUR_SECRET_KEY',
  JWT_EXPIRATION_TIME: '1h',
  PASSWORD_SALT_ROUNDS: 10,
  TWO_FACTOR_AUTH_ENABLED: true,
};
