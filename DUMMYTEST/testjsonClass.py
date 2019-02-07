import json
from pprint import pprint
from apicore.ApiCoreUtil import ApiCoreUtil
from nested_lookup import get_all_keys

# def testJson():
# with open('D:\PythonWS\Premise\DUMMYTEST\testJSON.json') as f:
#     data = json.load(f)
#     pprint(data)

# with open('testJSON.json', encoding='utf-8') as data_file:
#     data = json.loads(data_file.read())
#     pprint(data)
#     # print("XXXXXXXXXXXXXXXXXXXxx")
#     # data2 = json.dumps(data_file.read())
#     # pprint(data2)
#     # app = ApiCoreUtil()
#     # app.find123("submissionId", data)
#     for (k, v) in data.items():
#         print("Key: " + k)
#         print("Value: " + str(v))
#         print("type data",type(data))
#         print("type data", type(k))
#         print("type data", type(v))
#         if k == v:
#             print("test")
#         elif isinstance(v, dict):
#                 print("Key: " + k)
#                 print("Value: " + str(v))
#         elif isinstance(v, list):
#                 print("Key: " + k)
#                 print("Value: " + str(v))
#         # for d in v:
#         #     for result in self.find123(key, d):
#         #         yield result
#
# # testJson()

def recursive_items(dictionary):
        for key, value in dictionary.items():
            if type(value) is dict:
                yield (key, value)
                yield from recursive_items(value)
            else:
                yield (key, value)

def test() :
    with open('testJSON.json', encoding='utf-8') as data_file:
#     data = json.loads(data_file.read())
#     pprint(data)
# a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}
    for key, value in recursive_items(data_file):
        print(key, value)


test()