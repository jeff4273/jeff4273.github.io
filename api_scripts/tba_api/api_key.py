def get_api_key():
    with open("api_scripts/key.txt", "r") as file:
        return file.read().strip()