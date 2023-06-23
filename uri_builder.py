import yaml
import urllib
import urllib.parse
import sys

def assertForValidString(data, keyName):
    if keyName not in data:
        print(keyName, " is not present")
        raise Exception(keyName + " is not present")
    if data[keyName] is None:
        raise Exception(keyName + " is None")
    if len(data[keyName].strip()) == 0:
        raise Exception(keyName + " is not empty")

def checkIfStringPresent(data, keyName):
    if keyName not in data:
        return False
    if data[keyName] is None:
        return False
    if len(data[keyName].strip()) == 0:
        return False
    return True

def checkIfDictPresent(data, keyName):
    if keyName not in data:
        print("params not present as key")
        return False
    if type(data[keyName]) is not dict:
        print("params not present as key")
        return False
    return True

filename = sys.argv[1]

with open(filename, "r") as stream:
    try:
        data = yaml.safe_load(stream)
        assertForValidString(data, "scheme")
        assertForValidString(data, "authority")

        url = data["scheme"] + "://" + data["authority"] + "/"
        
        # Check if path is present
        pathPresent = checkIfStringPresent(data, "path")

        if pathPresent:
            url = url + data["path"] + "?"
        else:
            url = url + "?"

        # Check if params are present
        paramsPresent = checkIfDictPresent(data, "params")
        if paramsPresent:
            print(url + urllib.parse.urlencode(data["params"]))
        else:
            print(url)
        
    except yaml.YAMLError as exc:
        print(exc)
