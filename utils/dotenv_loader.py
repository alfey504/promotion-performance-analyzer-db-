import os

def load_dontenv(file_path: str = ".env"):
    with open(file_path) as f:
        for line in f:
            print(line)
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")

            os.environ(key, value)
            
