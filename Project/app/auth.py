from werkzeug.security import generate_password_hash, check_password_hash

def create_password(password):
    """Creates hashed password for User."""
    return generate_password_hash(password, method='sha256')

def check_password(password, hash):
    """Checks if hashed password matches with Users password and its hash."""
    return check_password_hash(hash, password)