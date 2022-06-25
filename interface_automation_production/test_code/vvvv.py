import ast
import json
from string import Template
aa =[{'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': '46e3a4a86b41e884e9ff7d7e39370b3bb318554260eac3abf38dff359bb8b5e78d98be5eecc893914360170b8d992f51c825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'contain': None, 'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['add_time', 'created_at', 'ebike_no']}}, {'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': 'c10363237f8e01ed34db47667d049ccbb318554260eac3abf38dff359bb8b5e720a85f14a7d2b321c37935b9758aa03cc825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['id']}}]
bb = str(aa)
# print(type(bb))
# print(bb)
# print(bb.replace("[",'').replace("]",'').replace("\\",'').split(','))
# print(list(bb))
# print(''.join(list(bb)), type(''.join(list(bb))))
res = bb.strip('[').strip(']').split(',')
# print(type(res))
# print(bb)
# a = ast.literal_eval(bb)
# print(a, type(a))
# print(a[1])

n = json.dumps(aa)
m = json.loads(n)
print(n, type(n))
print(m, type(m))