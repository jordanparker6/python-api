import os
import secrets
from typing import Dict, Any, List
from pydantic import AnyHttpUrl

# ~~~~~ APP ~~~~~
PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'python-api')
API_VERSION: str = os.getenv('API_VERSION', '/v1')

# ~~~~~ NETWORKING ~~~~~
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

# ~~~~~ DATA_BASE ~~~~~
DATABASE: Dict[str, Any] = {
    'type': os.environ.get('type', 'postgresql'),
    'database': os.environ.get('database', 'python-api'),
    'username': os.environ.get('username', 'admin'),
    'password': os.environ.get('password', 'admin'),
    'host': os.environ.get('host', 'localhost'),
    'port': os.environ.get('port', 5432)
}

# ~~~~~ SECRET ~~~~~
SECRET_KEY: str = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))

# ~~~~~ JWT ~~~~~
ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 60 * 24 * 8)