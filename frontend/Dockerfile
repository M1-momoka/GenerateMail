# Use the official Node.js image with the specified version
FROM node:20.10.0

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["npm", "run", "dev"]
