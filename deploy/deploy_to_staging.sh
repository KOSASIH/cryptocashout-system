#!/bin/bash

# Set environment variables
export ENVIRONMENT="staging"
export API_URL="https://staging-api.cryptocashout.com"
export DATABASE_URL="mongodb://staging-db:27017/"
export JWT_SECRET="staging_jwt_secret"

# Stop any existing containers
docker stop cryptocashout-atm-staging cryptocashout-backend-staging

# Remove any existing containers
docker rm cryptocashout-atm-staging cryptocashout-backend-staging

# Build the ATM image
docker build -t cryptocashout-atm-staging -f atm/Dockerfile .

# Build the backend image
docker build -t cryptocashout-backend-staging -f backend/Dockerfile .

# Run the ATM container
docker run -d --name cryptocashout-atm-staging -p 8082:8080 cryptocashout-atm-staging

# Run the backend container
docker run -d --name cryptocashout-backend-staging -p 8083:8081 cryptocashout-backend-staging

# Configure the backend environment variables
docker exec -it cryptocashout-backend-staging bash -c "export ENVIRONMENT=$ENVIRONMENT && export API_URL=$API_URL && export DATABASE_URL=$DATABASE_URL && export JWT_SECRET=$JWT_SECRET"

# Start the backend service
docker exec -it cryptocashout-backend-staging bash -c "python backend/app.py"

# Print a success message
echo "Deployment to staging successful!"
