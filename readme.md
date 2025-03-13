# Test task

## Setup

1. Clone the repository:
   ```sh
   git clone git@github.com:MKisil/TestTask.git
   ```
2. Navigate into the project directory:
   ```sh
   cd TestTask
   ```
3. Start the application using Docker Compose:
   ```sh
   docker compose up
   ```
4. Visit the application in your browser:
   - [http://localhost:5000](http://localhost:5000)

## Running Tests

Run the tests:
   ```sh
   docker-compose run --rm app pytest tests/
   ```

## API Documentation

You can access the API documentation at:
   - [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

