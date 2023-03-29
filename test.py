import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("API_KEY")
print(key)
