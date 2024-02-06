## Keycloak
* realm: bank
* client-id: bank-app
* client-secret: rifb7zJJzE2RKStq74pEPMg29W5GkyIC
* user: bank-app-user
* pass: bankappuserpass

```shell
curl -X POST \
  'http://localhost:2380/auth/realms/bank/protocol/openid-connect/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=banp-app-user' \
  -d 'password=bankappuserpass' \
  -d 'grant_type=password' \
  -d 'client_id=bank-app' \
  -d 'client_secret=rifb7zJJzE2RKStq74pEPMg29W5GkyIC'
```

curl http://localhost:9080/anything/of-foo -H "host:adagio-korat.gateway.bank" \
-H "Authorization:Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJHMEZyRk0zT1pjSXhPOE45Z2M2Q3N0RW5pT2lPOW8tX2ZOV0REdmR4Rlg0In0.eyJleHAiOjE3MDY4ODA1MjksImlhdCI6MTcwNjg4MDIyOSwianRpIjoiOGYxZGE0MTYtMzUyMy00MDRjLWFhZjYtMmMyZjQ2MjE0ZDA1IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDoyMzgwL2F1dGgvcmVhbG1zL2JhbmsiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMDcyNDczZjktZTI3OS00NmE1LTk0ODItZjY0ZmIxYzZjZmQ1IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYmFuay1hcHAiLCJzZXNzaW9uX3N0YXRlIjoiNTNkYjc5YTUtYzg3NC00NWEyLTg1NWMtZjQ1NWVlY2YxNjQ3IiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0Il0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZGVmYXVsdC1yb2xlcy1iYW5rIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiNTNkYjc5YTUtYzg3NC00NWEyLTg1NWMtZjQ1NWVlY2YxNjQ3IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6ImJhbnAtYXBwLXVzZXIifQ.d7n-L9uP2lSFNrHGglm5DBwlIYXC-FCoUJQwtAvj6W0jacR0gXVXq4YEzi3g-AEjljxGia4_eOYp2voqjDCtI3-VJYi0_SwBU56bGNiMXNZ7zHXsLde7Frf-iJQwNR9hXq0p9DNQ4srzljHBEs6uG3WdMGs4eNKuXNzbLpejGerp37nAa9d1542Z3Mpq7wlvSXqLoCC3pvnSeIiGHI0k_G-gq6IaMVhplzMYM-FcpCclfQ9NNVVL_YhHPtJJiHzHVTh5u10Pd0cINulZNubfIDHTOTnTPsbjS1jX4mnWMq8yRiAc-Ms63HvsI2QGi7hQRxxqy3zOdmG5O6f86t6seg"

RS256 public key


"jwt-auth": {
    "key": "preferred_username",
    "public_key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxZS56Wt4ybJQqmxEa5nR7cZ7sbuywvDtEwRWbzey7VNjO34GAA6mzT9XKzQK4/X8rGpWjJdfYV3DWoGyRpWQZClVOEgMFN/y0ZySrcSLsqSG7MccXVPFL5xKCVndYbD76ae9T/SY52AqT1Ly1/KKA1ehEYAaxP6n9IQ3/SSOlUMhqZUnqZs8AXDm+5ZzUs4TG+ypyMIQfgldeSPVElZTAZKBPUG2gMU+/7GjXCHoR+DQSB0elpPjFOq8dTifzK1P1JNuy7xWOjKjo5f3gGEx9jucxFej2iIzA2DC1NIa5F2uAlfRtG3AyQhyKOR78koG86afBhYL0A+VscXv8pWDsQIDAQAB",
    "algorithm": "RS256"
}

"openid-connect":{
    "bearer_only": true,
    "realm": "bank",
    "token_signing_alg_values_expected": "RS256",
    "public_key": "-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxZS56Wt4ybJQqmxEa5nR7cZ7sbuywvDtEwRWbzey7VNjO34GAA6mzT9XKzQK4/X8rGpWjJdfYV3DWoGyRpWQZClVOEgMFN/y0ZySrcSLsqSG7MccXVPFL5xKCVndYbD76ae9T/SY52AqT1Ly1/KKA1ehEYAaxP6n9IQ3/SSOlUMhqZUnqZs8AXDm+5ZzUs4TG+ypyMIQfgldeSPVElZTAZKBPUG2gMU+/7GjXCHoR+DQSB0elpPjFOq8dTifzK1P1JNuy7xWOjKjo5f3gGEx9jucxFej2iIzA2DC1NIa5F2uAlfRtG3AyQhyKOR78koG86afBhYL0A+VscXv8pWDsQIDAQAB
    -----END PUBLIC KEY-----"
}

{
    "client_id": "bank-app",
    "client_secret": "rifb7zJJzE2RKStq74pEPMg29W5GkyIC",
    "discovery": "http://localhost:2380/auth/realms/bank",
    "introspection_endpoint": "http://localhost:2380/auth/realms/bank",
    "bearer_only": true,
    "realm": "bank",
    "token_signing_alg_values_expected": "RS256",
    "public_key": "IIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxZS56Wt4ybJQqmxEa5nR7cZ7sbuywvDtEwRWbzey7VNjO34GAA6mzT9XKzQK4/X8rGpWjJdfYV3DWoGyRpWQZClVOEgMFN/y0ZySrcSLsqSG7MccXVPFL5xKCVndYbD76ae9T/SY52AqT1Ly1/KKA1ehEYAaxP6n9IQ3/SSOlUMhqZUnqZs8AXDm+5ZzUs4TG+ypyMIQfgldeSPVElZTAZKBPUG2gMU+/7GjXCHoR+DQSB0elpPjFOq8dTifzK1P1JNuy7xWOjKjo5f3gGEx9jucxFej2iIzA2DC1NIa5F2uAlfRtG3AyQhyKOR78koG86afBhYL0A+VscXv8pWDsQIDAQAB"
}
{
    "public_key": "-----BEGIN PUBLIC KEY-----\\nIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxZS56Wt4ybJQqmxEa5nR7cZ7sbuywvDtEwRWbzey7VNjO34GAA6mzT9XKzQK4/X8rGpWjJdfYV3DWoGyRpWQZClVOEgMFN/y0ZySrcSLsqSG7MccXVPFL5xKCVndYbD76ae9T/SY52AqT1Ly1/KKA1ehEYAaxP6n9IQ3/SSOlUMhqZUnqZs8AXDm+5ZzUs4TG+ypyMIQfgldeSPVElZTAZKBPUG2gMU+/7GjXCHoR+DQSB0elpPjFOq8dTifzK1P1JNuy7xWOjKjo5f3gGEx9jucxFej2iIzA2DC1NIa5F2uAlfRtG3AyQhyKOR78koG86afBhYL0A+VscXv8pWDsQIDAQAB\\n-----END PUBLIC KEY-----",
    "bearer_only": true,
    "realm": "your-realm",
    "introspection_endpoint": "http://keycloak:2380/auth/realms/bank/protocol/openid-connect/token/introspect",
    "token_signing_alg_values_expected": "RS256",
    "scope": "openid email profile",
    "ssl_verify": false
}
