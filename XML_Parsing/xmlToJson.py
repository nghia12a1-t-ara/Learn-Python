# Program to convert an xml
# file to json file
  
# import json module and xmltodict
# module provided by python
import json
import xmltodict
import os

os.chdir('D:\Python\XML_Parsing')

# open the input xml file and read
# data in form of python dictionary 
# using xmltodict module
with open("test1.xml") as xml_file:
      
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
      
    # generate the object using json.dumps() 
    # corresponding to json data
      
    json_data = json.dumps(data_dict, indent = 4)
      
    # Write the json data to output 
    # json file
    with open("data.json", "a") as json_file:
        json.dump(json_data, json_file, indent = 4)
        json_file.close()
