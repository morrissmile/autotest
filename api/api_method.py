import requests
import json

class api:
    @staticmethod
    def get(url, headers=None, params=None):
        request = requests.get(url, headers=headers, params=params)
        response = request.json()
        if request.status_code == 200:
            print(response)
            response_json = request.json()
            return response_json
        else:
            print(f'Request failed with status code: {request.status_code}')


    @staticmethod
    def post(url, headers=None, bodys=None):
        request = requests.get(url, headers=headers, json=bodys)
        response = request.json()
        if request.status_code == 200:
            print(response)
            response_json = request.json()
            return response_json
        else:
            print(f'Request failed with status code: {request.status_code}')

    @staticmethod
    def format_api_response_json(response):
        json_data = json.dumps(response.json(), indent=4, ensure_ascii=False)
        if response.status_code != 200:
            return json_data + '\n\nstatus:' + str(response.status_code)
        return json_data
