from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import os
import socket  # for socket

import chinacode


class MainPage(QWidget):

    def __init__(self):

        super().__init__()
        loadUi("deneme.ui",self)



        self.setWindowTitle('Network')
        self.setWindowIcon(QIcon('web.png'))




        #signol slot bağlantısı
        self.pingButton.clicked.connect(self.open_ping_page)
        self.ipButton.clicked.connect(self.open_ip_page)
        self.portButton.clicked.connect(self.open_nmap_open)


    def open_ip_page(self):
        adres=self.ipkutu.text()


        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as err:
            self.label_2.setText("socket creation failed with error %s" % (err))

        # default port for socket
        port = 80

        try:
            host_ip = socket.gethostbyname(adres)
        except socket.gaierror:

            # this means could not resolve the host
            self.label_2.setText("there was an error resolving the host")


        # connecting to the server
        s.connect((host_ip, port))

        self.label_2.setText(" port == %s host ismi== %s" % (host_ip, adres))









    def open_ping_page(self):
        new_name=self.pingkutu.text()
        hostname = new_name  # example
        response = os.system("ping   " + hostname)

        # and then check the response...
        if response == 0:

            self.label_2.setText(hostname+" up! ")



        else:
            self.label_2.setText(hostname + " down! ")





    def open_nmap_open(self):
        new_nmap_port=self.portkutu.text()
        port=self.spinBox.text()


        self.deneme(new_nmap_port,port)

    def deneme(self, new_nmap_port, port):

        print("tamam")
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("tamamm")
            new_nmap_port=int(new_nmap_port)
            port=int(port)
            print(type(port))
            client.connect((new_nmap_port,port))
            print("tamm")
            from_server = client.recv(4096)
            print(from_server)




        except socket.error as err:
            pass







