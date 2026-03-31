import os
from dotenv import load_dotenv
from pyscript import document
load_dotenv()

key = os.getenv("key")
print(key)

