import os

def email_client():

    os.system("echo '|--------------------------------------|'")
    os.system("echo '|---------- Starting server -----------|'")
    os.system("echo '|---------- Email Client --------------|'")
    os.system("echo ''")
    os.system("nc -l -p 1300")
    os.system("echo ''")
    os.system("echo '|---------------- End -----------------|'")

email_client()