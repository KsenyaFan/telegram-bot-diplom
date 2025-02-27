import os

from dotenv import load_dotenv
from pydantic import BaseModel, SecretStr, StrictStr

load_dotenv()

class SiteSettings(BaseModel):
    api_key: SecretStr = SecretStr(os.getenv('X-API-KEY', None))
    api_host: StrictStr = os.getenv('HOST_API', None)

