# API Reference: Cryptocashout ATM System

## Endpoints

### Transactions

* **POST /api/transactions**
	+ Create a new transaction
	+ Request Body:
		- `amount`: transaction amount
		- `currency`: transaction currency
		- `user_id`: user ID
	+ Response:
		- `transaction_id`: transaction ID
		- `status`: transaction status (pending, completed, failed)
* **GET /api/transactions/:id**
	+ Retrieve a transaction by ID
	+ Request Params:
		- `id`: transaction ID
	+ Response:
		- `transaction_id`: transaction ID
		- `amount`: transaction amount
		- `currency`: transaction currency
		- `status`: transaction status (pending, completed, failed)

### Fiat Exchange Rates

* **GET /api/rates**
	+ Retrieve real-time fiat exchange rates
	+ Response:
		- `rates`: an object with fiat exchange rates (e.g. `{ "USD": 1.0, "EUR": 0.88, ... }`)

### Users

* **POST /api/users**
	+ Create a new user
	+ Request Body:
		- `username`: user username
		- `password`: user password
	+ Response:
	- `user_id`: user ID
* **GET /api/users/:id**
	+ Retrieve a user by ID
	+ Request Params:
		- `id`: user ID
	+ Response:
		- `user_id`: user ID
		- `username`: user username

## Authentication

All API endpoints require authentication using a JSON Web Token (JWT) in the `Authorization` header.

## Error Handling

All API endpoints return a JSON response with an `error` property in case of an error.

## Rate Limiting

The API has a rate limit of 100 requests per minute per IP address.

## Contact Us

If you have any questions or concerns, please don't hesitate to contact us at [support@cryptocashout.com](mailto:support@cryptocashout.com).
