import uvicorn
import argparse  # Import the argparse library
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from starlette.responses import RedirectResponse

from app.api.api import api_router
from app.settings import settings

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[settings.RATE_LIMITING_FREQUENCY],
    enabled=settings.RATE_LIMITING_ENABLE,
)
app = FastAPI(title="Transfermarkt API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
app.include_router(api_router)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Transfermarkt API")
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="The port to run the server on (default: 8000)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Request timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=0.5,
        help="Minimum seconds between requests to Transfermarkt (default: 0.5)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=2,
        help="Maximum number of retries for failed requests (default: 2)",
    )
    args = parser.parse_args()

    # Update settings with command-line arguments
    settings.REQUEST_TIMEOUT = args.timeout
    settings.REQUEST_RATE_LIMIT = args.rate_limit
    settings.REQUEST_MAX_RETRIES = args.max_retries

    print(f"Starting Transfermarkt API on port {args.port}")
    print(f"Settings: timeout={args.timeout}s, rate_limit={args.rate_limit}s, max_retries={args.max_retries}")

    uvicorn.run("app.main:app", host="0.0.0.0", port=args.port, reload=True)
