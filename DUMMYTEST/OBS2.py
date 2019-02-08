from xml.dom.minidom import parseString
import json
class myTest:

    def bar(somejson, key):
        def val(node):
            # Searches for the next Element Node containing Value
            e = node.nextSibling
            while e and e.nodeType != e.ELEMENT_NODE:
                e = e.nextSibling
            return (e.getElementsByTagName('string')[0].firstChild.nodeValue if e
                    else None)
        # parse the JSON as XML
        foo_dom = parseString(xmlrpclib.dumps((json.loads(somejson),)))
        # and then search all the name tags which are P1's
        # and use the val user function to get the value
        return [val(node) for node in foo_dom.getElementsByTagName('name')
                if node.firstChild.nodeValue in key]
    def method(self):
        with open('ObservationJSON.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            return data

test = myTest()
data = test.method()
test.bar(data, 'P1')