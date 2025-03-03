keycloak-token-cli
===

Exchange an authorization code for a JWT token from keycloak.
Set up a public client first.

```
$ pdm install
$ python token.py
INFO:     Started server process [10328]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
Visit this URL in your browser: https://keycloak.k8.juju.net/realms/juju/protocol/openid-connect/auth?client_id=public-client&response_type=code&redirect_uri=http://localhost:9999/callback&scope=openid&state=&nonce=

---------ACCESS TOKEN---------
ey...
---------ACCESS TOKEN---------
...
```
