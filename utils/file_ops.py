import os

def read_file(path: str) -> bytes:
    """Reads a file as bytes."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    
    with open(path, 'rb') as f:
        return f.read()

def write_file(path: str, data: bytes, overwrite: bool = False) -> None:
    """Writes bytes to a file, preventing accidental overwrites unless specified."""
    if os.path.exists(path) and not overwrite:
        raise FileExistsError(f"File already exists: {path}")
        
    with open(path, 'wb') as f:
        f.write(data)
