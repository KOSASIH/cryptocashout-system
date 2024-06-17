// app/services/analytics.js
import axios from 'axios';

class AnalyticsService {
  async trackTransaction(transaction) {
    const response = await axios.post('https://analytics-api.com/track', {
      event: 'transaction',
      data: transaction,
    });
    return response.data;
  }
}

export default AnalyticsService;
