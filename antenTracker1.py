from paramiko import SSHClient
import threading
import time
from threading import Timer


def signalLevel():
    """This is used to measure signal level of an antenna"""
    # Connect
    client = SSHClient()
    client.load_system_host_keys()

    flag1 = True
    while flag1:
        client.connect('192.168.1.11', username='anadolurobotik', password='64732MYrobo')
        index = 0

        flag2 = True
        # Run a command (execute PHP interpreter)
        while flag2:
            try:
                if index == 21:
                    flag1, flag2 = False
                    break
                else:
                    stdin, stdout, stderr = client.exec_command("iwconfig ath0 | grep -i Signal")

                    sonuc = stdout.read()
                    sonuc = sonuc.decode("utf-8")
                    print(sonuc[15:28])
                    print(sonuc[23:25])
                    print("Measurement number: ", index)
                    index += 1
            except:
                return flag2

        # Close the client itself
        client.close()




if __name__ == '__main__':
    timer = Timer(1, signalLevel)
    timer.start()
    # wait for the timer to finish
    print('Waiting for the timer...')
