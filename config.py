import os
from dotenv import load_dotenv

load_dotenv()

# Настройки Flask приложения
SECRET_KEY = os.environ("SECRET_KEY")
ADMIN_USERNAME = os.environ("ADMIN_USERNAME")
ADMIN_PASSWORD = os.environ("ADMIN_PASSWORD")


