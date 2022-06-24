
def liquiFormat()
from xml.dom import minidom
import os 

root = minidom.Document()
  
xml = root.createElement('databaseChangeLog') 
xml.setAttribute('xmlns', 'http://www.liquibase.org/xml/ns/dbchangelog')
xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
xml.setAttribute('xmlns:ext', 'http://www.liquibase.org/xml/ns/dbchangelog-ext')
xml.setAttribute('xmlns:pro', 'http://www.liquibase.org/xml/ns/pro')
xml.setAttribute('xsi:schemaLocation', 'http://www.liquibase.org/xml/ns/dbchangelog \n http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-latest.xsd \n http://www.liquibase.org/xml/ns/dbchangelog-ext http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-ext.xsd \n http://www.liquibase.org/xml/ns/pro http://www.liquibase.org/xml/ns/pro/liquibase-pro-latest.xsd')

root.appendChild(xml)
  
chanegSet = root.createElement('changeSet ')
chanegSet.setAttribute('id', 'Geeks for Geeks')
chanegSet.setAttribute('author', 'Geeks for Geeks')
  
xml.appendChild(chanegSet)
  
xml_str = root.toprettyxml(indent ="\t") 
  
save_path_file = "gfg.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 