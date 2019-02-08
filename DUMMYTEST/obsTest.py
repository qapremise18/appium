import json
from nested_lookup import *
class myTest:

    def recursiveitems(self, dictionary):
        type("type>>",type(dictionary))
        for key, value in dictionary.items():
            if type(value) is dict:
                yield (key, value)
                yield from myTest.recursiveitems(value)
            else:
                yield (key, value)

    def test(self):
        with open('testJSON.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            #     pprint(data)
            for key, value in self.recursiveitems(data_file):
                 print(key, value)

    def myprint(self, d):
        with open('testJSON.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            print("1>>", type(data))
            for k, v in d.items():
                print("1>>",type(k))
                print("2>>", type(v))
                if isinstance(v, dict):
                    self.myprint(v)
                    print("HAHH")
                else:
                     print("{0} : {1}".format(k, v))
                     print("Hee")

    def method(self):
        with open('ObservationJSON.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            return data

    def findkeys(self, node, kv):
        print("!@@@@@@@test")
        if isinstance(node, list):
            for i in node:
                for x in self.findkeys(i, kv):
                    yield x
        elif isinstance(node, dict):
            if kv in node:
                yield node[kv]
            for j in node.values():
                for x in self.findkeys(j, kv):
                    yield x
test = myTest()
data = test.method()
print(type(data))
# test.myprint(data)
# print (list(test.findkeys(data, 'id')))
keys = get_all_keys(data)
val = get_occurrence_of_key(data,"observationId")
print(val)
