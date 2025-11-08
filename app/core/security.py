from passlib.context import CryptContext

# Use Argon2 instead of bcrypt
pwd_context = CryptContext(
    schemes=["argon2"],
    default="argon2",
    argon2__time_cost=3,        # Number of iterations
    argon2__memory_cost=65536,  # Memory usage (64MB)
    argon2__parallelism=4,      # Number of parallel threads
    argon2__hash_len=32,        # Hash length
    argon2__salt_len=16,        # Salt length
    deprecated="auto"
)

def hash_password(password: str) -> str:
    """Hash a password using Argon2"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)