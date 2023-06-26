# Introduction
This is a very basic tool to allow building error-free URIs/deeplinks for apps that the product and operation teams can use.

# Prerequisites
- Python3 or above installed on the machine. If not already installed you can install Python3 from here (https://www.python.org/downloads/)
- PIP for installing Python dependencies - https://pypi.org/project/PyYAML/
- Yaml for Python - https://pypi.org/project/PyYAML/

# How to use the tools?
_Before you use the tool, please make sure that you understand the format of the URI - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#exampleuri_

The different parameters of the URI can be input from a YAML file. Format of the  file is as follows:
```
scheme: <scheme> --  eg. https or appScheme
authority: <authority> -- eg. upiPayment
path: <path> -- eg. this/is/my/path/ (Note: There  should not be any '/' at the  start of the path) **[Optional]**
params: **[Optional]**
  param1: myParam1
  param2: https://www.google.com
  backgroundColor: '#ffffff' - Note: the color code needs to be within single quotes.
```
**Note**: There is a sample yaml file present  in the repository.

To get the desired URI, run the following command:
```
python uri_builder.py sample_yaml.yml
```
If you want to run the script using a specific version of Python, use the binary of that specific python version. eg. for using Python3, use
```
python3 uri_builder.py sample_yaml.yml
```



