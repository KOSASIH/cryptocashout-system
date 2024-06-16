#!/bin/bash

# Set environment variables
export ENVIRONMENT="production"
export API_URL="https://api.cryptocashout.com"
export DATABASE_URL="mongodb://production-db:27017/"
export JWT_SECRET="production_jwt_secret"

# Stop any existing containers
docker stop cryptocashout-atm cryptocashout-backend

# Remove any existing containers
docker rm cryptocashout-atm cryptocashout-backend

# Build the ATM image
docker build -t cryptocashout-atm -f atm/Dockerfile .

# Build the backend image
docker build -t cryptocashout-backend -f backend/Dockerfile .

# Run the ATM container
docker run -d --name cryptocashout-atm -p 8080:8080 cryptocashout-atm

# Run the backend container
docker run -d --name cryptocashout-backend -p 8081:8081 cryptocashout-backend

# Configure the backend environment variables
docker exec -it cryptocashout-backend bash -c "export ENVIRONMENT=$ENVIRONMENT && export API_URL=$API_URL && export DATABASE_URL=$DATABASE_URL && export JWT_SECRET=$JWT_SECRET"

# Start the backend service
docker exec -it cryptocashout-backend bash -c "python backend/app.py"

# Print a success message
echo "Deployment to production successful!"
