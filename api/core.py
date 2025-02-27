from ..settings import SiteSettings
from ..api.util.api_collections import SiteApiInterface

site = SiteSettings()

query = "Inception"

# headers = {"X-API-KEY": site.api_key.get_secret_value(),
#            "X-HOST_API": site.api_host
#            }
headers = {"accept": "application/json"}


url = site.api_host
params = {"query": query}

site_api = SiteApiInterface()

if __name__ == "__main__":
    site_api()




