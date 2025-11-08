# transfermarkt-api

This is my fork of [felipeall/transfermarkt-api](https://github.com/felipeall/transfermarkt-api). I've fixed a regex error for age and birthdate parsing and migrated the project to use [uv](https://docs.astral.sh/uv/).

This project provides a lightweight and easy-to-use interface for extracting data from [Transfermarkt](https://www.transfermarkt.com/) by applying web scraping processes and offering a RESTful API service via FastAPI. With this service, developers can seamlessly integrate Transfermarkt data into their applications, websites, or data analysis pipelines.

**Note:** The deployed application is for testing purposes only and has rate limiting enabled. For production use or customization, consider hosting your own instance.

## API Documentation

Interactive API documentation (Swagger UI): https://transfermarkt-api.fly.dev/

## Installation & Usage

### Running Locally
```bash
# Clone the repository
git clone https://github.com/mattestanka/transfermarkt-api.git

# Navigate to the project directory
cd transfermarkt-api

# Install dependencies using uv
uv sync

# Start the API server (default port: 8000)
uv run python -m app.main

# Or specify custom options
uv run python -m app.main --port 8080 --timeout 15 --rate-limit 1.0 --max-retries 3

# Access the API
open http://localhost:8000/
```

### Running via Docker
```bash
# Clone the repository
git clone https://github.com/mattestanka/transfermarkt-api.git

# Navigate to the project directory
cd transfermarkt-api

# Build the Docker image
docker build -t transfermarkt-api .

# Run the container
docker run -d -p 8000:8000 transfermarkt-api

# Access the API
open http://localhost:8000/
```

## Configuration

### Command-Line Options

| Option            | Description                                                  | Default |
|-------------------|--------------------------------------------------------------|---------|
| `--port`          | Port to run the server on                                    | `8000`  |
| `--timeout`       | Request timeout in seconds (for Transfermarkt scraping)     | `10`    |
| `--rate-limit`    | Minimum seconds between requests to Transfermarkt            | `0.5`   |
| `--max-retries`   | Maximum number of retries for failed requests                | `2`     |

### Environment Variables

| Variable                  | Description                                                  | Default      |
|---------------------------|--------------------------------------------------------------|--------------|
| `RATE_LIMITING_ENABLE`    | Enable rate limiting feature for API endpoints               | `false`      |
| `RATE_LIMITING_FREQUENCY` | Delay allowed between each API call (see [slowapi](https://slowapi.readthedocs.io/en/latest/)) | `2/3seconds` |
| `REQUEST_TIMEOUT`         | Request timeout in seconds (for Transfermarkt scraping)     | `10`         |
| `REQUEST_RATE_LIMIT`      | Minimum seconds between requests to Transfermarkt            | `0.5`        |
| `REQUEST_MAX_RETRIES`     | Maximum number of retries for failed requests                | `2`          |

**Note:** Command-line options take precedence over environment variables.

## Changes from Original

- Fixed regex error in age and birthdate parsing
- Migrated from Poetry to [uv](https://docs.astral.sh/uv/) for dependency management
- Added request timeout to prevent indefinite hangs
- Implemented connection pooling for better performance
- Added rate limiting for Transfermarkt requests to avoid overloading their servers
- Implemented automatic retry logic for failed requests
- Added command-line options for runtime configuration

## Credits

Original project by [felipeall](https://github.com/felipeall/transfermarkt-api)
