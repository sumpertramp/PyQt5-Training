"""
===============================================================================
File: ESP32_PyQt5_Access_Point.py
Date: [22.01.2024]

Description:
   This PyQt5-based application facilitates the connection to an ESP32 device.
   It includes a main window with options to connect to an Access Point (AP).
   The connection parameters (IP address and port number) are stored in a 
   configuration file (config.json). The application displays information and 
   error messages using QMessageBox. The connection status is visually 
   represented with icons.

Author's Introduction:
  - Name: Sümeyye Derelli
  - Occupation: Embedded System Engineer
  - Contact: smyydrll@gmail.com
  
===============================================================================
"""



import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QToolBar, QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class ESP32Client(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("ESP32 Connection Application")
        self.setGeometry(100, 100, 400, 200)

        # Define ip_edit and port_edit elements
        self.ip_edit = QLineEdit()
        self.port_edit = QLineEdit()

        # Create a toolbar and add a connect action
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        self.connect_action = QAction(QIcon("APdisconnect.png"), "Connect to AP", self)
        self.connect_action.triggered.connect(self.show_connect_dialog)
        toolbar.addAction(self.connect_action)

    def show_connect_dialog(self):
        # Show the connection dialog when the connect action is triggered
        dialog = ConnectDialog(self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            ip = dialog.ip_edit.text()
            port = dialog.port_edit.text()

            if not ip or not port:
                self.show_error("IP address and port number cannot be empty.")
                return

            # Create a TCP socket and attempt to connect to the specified IP and port
            socket = QTcpSocket()
            socket.connectToHost(ip, int(port))

            if socket.waitForConnected(1000):
                self.connect_action.setIcon(QIcon("APconnect.png"))
                self.save_config(ip, port)
                self.show_message("Connection successful.")
            else:
                self.show_error("Connection error: Check the IP address and port number.")

    def save_config(self, ip, port):
        # Save the configuration (IP and port) to a JSON file
        config = {"ip": ip, "port": port}
        with open("config.json", "w") as f:
            json.dump(config, f)

    def show_message(self, message):
        # Display an information message box
        QMessageBox.information(self, "Information", message)

    def show_error(self, message):
        # Display an error message box
        QMessageBox.critical(self, "Error", message)

class ConnectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the connection dialog
        self.setWindowTitle("Connect to AP")
        self.setGeometry(200, 200, 300, 150)

        self.ip_label = QLabel("IP Address:")
        self.ip_edit = QLineEdit()

        self.port_label = QLabel("Port Number:")
        self.port_edit = QLineEdit()

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_edit)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_edit)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

        # Load configuration from the JSON file when initializing the dialog
        self.load_config()

    def load_config(self):
        # Load configuration (IP and port) from a JSON file and set the values in the dialog
        with open("config.json", "r") as f:
            config = json.load(f)
            self.ip_edit.setText(config["ip"])
            self.port_edit.setText(config["port"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ESP32Client()
    window.show()
    sys.exit(app.exec_())