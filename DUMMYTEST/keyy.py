import json
class keyy:
    def method(self):
        with open('ObservationJSON.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            return data

    def extract_values(obj, key):
        """Pull all values of specified key from nested JSON."""
        arr = []
        print("HEEEEEEE")
        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results

    def key_finder(data, keys):

        def search_data(search_queue, dict_queue=[]):
            items = search_queue.pop(0)
            if isinstance(items, dict):
                items = items.values()
            for item in items:
                data_type = type(item)
                if data_type is dict or data_type is list:
                    search_queue.append(item)
                    if data_type is dict:
                        dict_queue.append(item)
            if search_queue:
                return search_data(search_queue, dict_queue)
            else:
                return find_keys(dict_queue)

        def find_keys(queue, match_keys=keys):
            matches = []
            for q in queue:
                for key, value in q.items():
                    if key in match_keys:
                        matches.append((key, value))
            return matches

        return search_data([data])

# test = keyy()
# data = test.method()
# print(type(data))
# print(data)
#
# dict_data = json.loads(str(data))  # json_data is the placeholder for your json
# keys_to_find = ['customer_count', 'utc_start_at', 'non_resource_bookable_capacity']
# results = keyy.key_finder(dict_data, keys_to_find)
#
# for result in results:
#     print('{}: {}'.format(result[0], result[1]))
#
# keys_to_find = ['observationId']
# results = keyy.key_finder(data, keys_to_find)
#
# for result in results:
#     print('{}: {}'.format(result[0], result[1]))

test = keyy()
data = test.method()
print(type(data))
print(data)
# names = keyy.extract_values('ObservationJSON.json', 'observationId')
for key , val in data.items() :
    # print(key,"===",val)
    # print(type(key),"===",type(val))
    if isinstance(val,dict) :
        if "observationId" in str(val) :
            print("In DIC ID")
    elif isinstance(val,list):
        if "observationId" in str(val) :
            print("In LIST ID")
            print(val)
            print(type(val))
            s = str(val)
            a = s.replace("'", "")
            print(a)
            print(a.count("observationId"))
            a = a.replace("[","").replace("{","").replace("]","").replace("}","")
            print(a)
            my = a.split(",")
            print(type(my))
            for x in my:
                z = x.split(":")
                print(z)
                print(type(z))
                if  "observationId" in str(z):
                    print("GGGGGGGG",z[1])


    # print(type(key))

