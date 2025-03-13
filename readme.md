# Test task

## Setup

1. Clone repository:
   ```sh
   git clone git@github.com:MKisil/TestTask.git
   ```
2. Navigate into project directory:
   ```sh
   cd TestTask
   ```
3. Start application:
   ```sh
   docker compose up
   ```
4. Visit application in browser:
   - [http://localhost:5000](http://localhost:5000)

## Running Tests

Run tests:
   ```sh
   docker-compose run --rm app pytest tests/
   ```

## API Documentation

You can access API documentation at:
   - [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

