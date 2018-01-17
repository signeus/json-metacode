import json
from pprint import pprint


def openJson(urlFile = 'example.json'):
    with open(urlFile) as json_data:
        myJson = json.load(json_data)
        json_data.close()
        return myJson

def prettyPrintJson(myJson):
    pprint(myJson)

def findParser(dictionary, father = "dict"):
    for k, v in dictionary.items():
        if isinstance(v, dict):
            print("var " + k + ": NSDictionary")
            #applyTemplate(father, v, k)
            print("" + str(father) + ".setValue(" + str(k) + ", forKey: \"" + str(k) + "\")")
            for result in findParser(v, k):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in findParser(d, k):
                    yield result
        else:
            #applyTemplate(father, v, k, True)
            print("" + str(father) + ".setValue(\"" + str(v) + "\", forKey: \"" + str(k) + "\")")

def applyTemplate(fatherNode, value, key, varValLiteral = False):
    variable = str(key)
    if varValLiteral:
        variable = "\"" + str(value) + "\""

    return str(fatherNode) + ".setValue(" + variable + ", forKey: \"" + str(key) + "\")"


def main():
    myOtherJson = openJson("newexample.json")
    print(list(findParser(myOtherJson)))

if __name__ == "__main__":
    main()

#Print example : dict.setValue("value", forKey: "key")