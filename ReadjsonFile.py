import json

#Read json

myjsonfile = open(r'C:\Users\LENOVO\Desktop\Json_File\Employee.json', 'r')
jsondata = myjsonfile.read()
#print(jsondata)
#print(type(jsondata))

#parse
object = json.loads(jsondata)
#print(object)
#print(type(object))

#print(object['firstName'])
list = (object['address'])
#print(list.get('state'))


for index in list.values():
    print(index)



