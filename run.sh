
#!/bin/sh

pwd
which python
which pip
python --version

pip install -r requirements.txt
# uvicorn api:enroller --reload --host 0.0.0.0 --port 10000
uvicorn api:enroller --proxy-headers --host 0.0.0.0 --port 10000



# — ssl-certfile <fullchain certificate in PEM> — ssl-keyfile <RSA / ECC Private Key>  
#  — ssl-cert-reqs 1 --ssl-ca-certs <fullchain certificates in PEM> 
#  — port 443