# Create Python Virtual environment
# python3 -m venv venv

# improt library PyQt5, an application development package
# pip install PyQt5
# https://pypi.org/project/PyQt5/
from PyQt5.QtWidgets import *

# pip install PyQtWebEngine -- web engine packages
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *

import sys

# Creating a class
class MainWindow(QMainWindow):
    # Creating a constructor
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        # set home page url
        self.browser.setUrl(QUrl('https://google.com/'))
        self.setCentralWidget(self.browser)
        # show browser at maximum size
        self.showMaximized()
        
        # creating a tool bar
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)
       
        # BACK BUTTON
        # creating the back button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        # adding button to the tool bar
        tool_bar.addAction(back_button)
        
        # FORWARD BUTTON
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        # adding button to the tool bar
        tool_bar.addAction(forward_button)
        
        # REFRESH BUTTON
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        # adding the button to the tool bar
        tool_bar.addAction(refresh_button)
        
        # HOME BUTTON
        home_button = QAction('Home', self)
        # creating a new method called go home that will go back to the home page
        home_button.triggered.connect(self.go_home)
        # adding home button
        tool_bar.addAction(home_button)
        
        # URL BAR
        # creating the url bar
        self.url_bar = QLineEdit()
        # if enter is pressed, connect to another method
        tool_bar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.go_to_url) 
        
        # if the url is changed you need to do a new connection
        self.browser.urlChanged.connect(self.new_url)
        
    def go_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))
        
    def go_to_url(self):
        # if you get the text that is the URL
        url = self.url_bar.text()
        
        # checking if https:// is found in url
        if "https://" not in str(url):
            url = "https://" + str(url)
        
        # set url 
        self.browser.setUrl(QUrl(url))
    
    def new_url(self, url):
        # checking if https:// is found in url
        if "https://" not in str(url):
            url = "https://" + str(url)
        self.url_bar.setText(url.toString())
        
        

app = QApplication(sys.argv)
QApplication.setApplicationName('Web Browser'); 
window = MainWindow()
app.exec()