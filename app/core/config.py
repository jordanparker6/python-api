"""Configuration File."""
import os
import secrets
from typing import Dict, Any, List

# ~~~~~ APP ~~~~~
PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'python-api')
API_VERSION: str = os.getenv('API_VERSION', '/v1')

# ~~~~~ NETWORKING ~~~~~
BACKEND_CORS_ORIGINS: List[str] = []

# ~~~~~ DATABASE ~~~~~
DATABASE: Dict[str, Any] = {
    'type': os.environ.get('DATBASE_TYPE', 'postgresql'),
    'database': os.environ.get('DATABASE', 'python-api'),
    'username': os.environ.get('DATABASE_USER', 'admin'),
    'password': os.environ.get('DATABASE_PASSWORD', 'admin'),
    'host': os.environ.get('DATABASE_HOST', 'localhost'),
    'port': os.environ.get('DATABASE_PORT', 5432)
}

# ~~~~~ SECRET ~~~~~
SECRET_KEY: str = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))

# ~~~~~ JWT ~~~~~
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', str(60 * 24 * 8)))

# ~~~~~ LOGGING ~~~~~
LOGLEVEL: str = os.getenv('LOGLEVEL', 'INFO')
