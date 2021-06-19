import socket 
import string
import threading
import sys



def main():
    global irc

    print("Bievenue sur IRC Client !")
    print("Entrez l'hote auquel vous voulez vous connecter")

    host = input()

    print("Entrez le port")

    port = int(input())

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Connecting to: " + host + ":" + str(port))

    irc.connect((host, port))

    print("Enter your Nickname")

    nick = input()

    irc.send(('USER ' + nick + ' 0 * :Aynbo' + '\r\n').encode())
    irc.send(('NICK ' + nick + '\r\n').encode())

    print("Entrez le nom du cannal à rejoindre")
    
    channel = input()

  
    irc.send(('JOIN ' + channel + '\r\n').encode())

    cmd = ""

    listener()

    while (cmd != "/quit"):
        cmd = input(':' + nick + ' PRIVMSG ' + channel + ' :')

        if (cmd == "/quit"):
            irc.send(('QUIT :Au Revoir \r\n').encode())

        else:
            irc.send(('PRIVMSG ' + channel + ' :' + cmd + '\r\n').encode())
        
        listenr_thread = threading.Thread(target=listener)
        listenr_thread.daemon = True
        listenr_thread.start()


def listener():
    buffer = irc.recv(1024)
    msg = buffer.decode()

    if (msg[0] == 'PONG'):
        irc.send(('PONG \r\n').encode())

    print(msg)

main()