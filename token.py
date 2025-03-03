# Exchange an authorization code for a JWT token from keycloak.
import os
import signal

from fastapi import FastAPI
from keycloak import KeycloakOpenID

KEYCLOAK_SERVER_URL = "https://keycloak-admin.k8.juju.net"
REALM_NAME = "juju"
CLIENT_ID = "public-client"

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                 client_id=CLIENT_ID,
                                 realm_name=REALM_NAME,
                                 verify=False)

config_well_known = keycloak_openid.well_known()

auth_url = keycloak_openid.auth_url(
    redirect_uri="http://localhost:9999/callback",
    scope="openid")

print(f"Visit this URL in your browser: {auth_url}")

app = FastAPI()


@app.get("/callback")
def callback(code: str):
  access_token = keycloak_openid.token(
      grant_type='authorization_code',
      code=code,
      redirect_uri="http://localhost:9999/callback")
  print("ACCESS TOKEN".center(30, '-'))
  print(access_token["access_token"])
  print("ACCESS TOKEN".center(30, '-'))
  os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="0.0.0.0", port=9999)
