#! python3.7
# devOps Server-Template ausfüller

from selenium import webdriver
import sys

# DevOps mm Browser aufrufen
browser = webdriver.Firefox()
browser.get('https://dev.azure.com/CEMA-NRW/Projekte%20Diakonie%20Ruhr/_workitems/recentlyupdated/')
linkElem = browser.find_element_by_class_name("msContextualMenu-link root-77")
linkElem.click()
