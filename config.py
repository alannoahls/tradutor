import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
