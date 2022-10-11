import requests
import os, sys

class BearerAuth(requests.auth.AuthBase):
  def __init__(self, token):
    self.token = token

  def __call__(self, r):
    r.headers["authorization"] = "Bearer " + self.token
    return r

def get_public_ip():
  api_url = "https://api.ipify.org?format=json"
  response = requests.get(api_url)
  if response.json():
    if "ip" in response.json():
      return response.json()["ip"]

def update_location_network(account, location, name, ip, token):
  api_url = f"https://api.cloudflare.com/client/v4/accounts/{account}/gateway/locations/{location}"
  update = {
    "name": name,
    "networks": [
      {
        "network": f"{ip}/32"
      }
    ],
    "client_default": True
  }
  print(update)
  response = requests.put(
    api_url,
    json=update,
    auth=BearerAuth(token)
  )
  return response.status_code == 200

def check_env():
  okay = True
  vars = [
    "CF_ACCOUNT",
    "CF_LOCATION",
    "CF_LOCATION_NAME",
    "CF_TOKEN"
  ]
  for var in vars:
    if not os.environ.get(var):
      print(f"Cannot find {var}")
      okay = False
  return okay

if __name__ == "__main__":
  if not check_env():
    print("Exiting")
    sys.exit(1)
  
  ip = get_public_ip()
  print(f"Got public IP of {ip}")
  okay = update_location_network(
    account = os.environ.get("CF_ACCOUNT"),
    location = os.environ.get("CF_LOCATION"),
    name = os.environ.get("CF_LOCATION_NAME"),
    ip = ip,
    token = os.environ.get("CF_TOKEN")
  )
  if okay:
    print("Update complete")
  else:
    print("Did not get 200 response code")