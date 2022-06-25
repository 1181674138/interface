import requests
import json


class RequestsUtil:

    # session = requests.session()

    def __init__(self):
        self.session = requests.session()

    def send_requests(self, method, url, param_type, data, **kwargs):

        method = method.upper()
        param_type = param_type.upper()

        if method == 'GET':
            response = self.session.request(method=method, url=url, params=data, **kwargs)

        elif method == 'POST':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)

        elif method == 'DELETE':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)

        elif method == 'PUT':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)

        else:
            return '不在请求范围内'

        return response

    def close_session(self):
        self.session.close()
