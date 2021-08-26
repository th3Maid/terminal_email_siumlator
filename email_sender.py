import os

def email_share():

    os.system("echo '|--------------------------------------|'")
    os.system("echo '|---------- Email Client --------------|'")
    os.system("echo ''")
    des = input("Destinatario: ")
    asu = input("Assunto: ")
    msg = input("Mensagem: ")
    os.system("echo ''")
    os.system("echo 'Destinatario: %s - Assunto: %s - Mensagem: %s' | nc localhost 1300" % (des, asu, msg))
    os.system("echo ''")
    os.system("echo '|---------------- End -----------------|'")

email_share()