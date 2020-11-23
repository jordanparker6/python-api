"""Utility functions for security.
"""
from datetime import datetime, timedelta
from typing import Any, Union
import jose.jwt as jwt
from passlib.context import CryptContext

from app.core import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """Encodes a JWT

    Args:
        subject (Union[str, Any]): The content of the JWT.
        expires_delta (timedelta, optional): The JWT expiry timedelta. Defaults to None.

    Returns:
        str: The JWT hash.
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a password against a hashed pasword using passlib

    Args:
        plain_password (str): The raw pasword string.
        hashed_password (str): A hashed password string.

    Returns:
        bool: Outcome of the password verification.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hashes a password string using passlib.

    Args:
        password: The password.

    Returns:
        The password hash.
    """
    return pwd_context.hash(password)
