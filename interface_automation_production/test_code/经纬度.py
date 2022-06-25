import os
import random
import yaml
import json
import jinja2
import pystache
import re
from string import Template

lng = random.uniform(120.06, 120.07)
lat = random.uniform(30.28, 30.29)
b = {lng, lat}
print(b)

a = {"a": "123"}

with open(os.path.dirname(os.getcwd()) + "./token.yml", ) as f:

    token = yaml.load(stream=f, Loader=yaml.FullLoader)
    print(token)
    template = Template(token)
    temp = template.safe_substitute({'header': '123'})
    te = yaml.safe_load(temp)
    print(template)
    print(temp)
    print(te)
