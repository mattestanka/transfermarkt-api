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
git clone https://github.com/YOUR-USERNAME/transfermarkt-api.git

# Navigate to the project directory
cd transfermarkt-api

# Install dependencies using uv
uv sync

# Start the API server (default port: 8000)
uv run python -m app.main

# Or specify a custom port
uv run python -m app.main --port 8080

# Access the API
open http://localhost:8000/
```

### Running via Docker
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/transfermarkt-api.git

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

### Environment Variables

| Variable                  | Description                                               | Default      |
|---------------------------|-----------------------------------------------------------|--------------|
| `RATE_LIMITING_ENABLE`    | Enable rate limiting feature for API calls                | `false`      |
| `RATE_LIMITING_FREQUENCY` | Delay allowed between each API call (see [slowapi](https://slowapi.readthedocs.io/en/latest/)) | `2/3seconds` |

## Changes from Original

- Fixed regex error in age and birthdate parsing
- Migrated from Poetry to [uv](https://docs.astral.sh/uv/) for dependency management

## Credits

Original project by [felipeall](https://github.com/felipeall/transfermarkt-api)
