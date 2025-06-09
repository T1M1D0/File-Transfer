import socket
import os
import sys

#Opening port 22 works pussy LETS FUCKING GOOOOOO!!!!!
#change change omg theres a change this is a test holy smokesssss

def elevate():
    if os.getuid() != 0:
        cmd = ("sudo", sys.executable, *sys.argv)
        os.execvp("sudo", cmd)

def open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    target_host = socket.gethostname()

    s.bind((socket.gethostname(), 22))
    s.listen(5)

    sel = int(input("Select an option:\n1) Scan Network to see if port 22 is open\n2) Await connection from port 22"))
    if sel == 2:
        print('Server is open hoe')

        while True:
            c, addr = s.accept()
            print('Connection recieved from', addr, '\nHost name:', target_host)
    else:
        addr = s.accept()
        ip_num = addr.split('.')
        print(ip_num)
#        for i in range(255):
        subnet = ip_num[0, 1, 2]+i.strip().join()
#            i+=1
        print(subnet)

    if KeyboardInterrupt:
        pass

    #transfer()


#def transfer():


def main():
    local_host = socket.gethostname()
    host_ip = socket.gethostbyname(local_host)
    elevate()
    open_port()

if __name__ == '__main__':
    main()
