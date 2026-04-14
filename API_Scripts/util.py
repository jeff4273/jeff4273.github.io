def get_api_key():
    with open("key.txt", "r") as f:
        return f.read().strip()