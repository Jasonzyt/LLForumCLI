import json
import requests
from xf import Config, Resource, Version


def from_json(data, arr=False, **kwargs):
    if 'errors' in data:
        raise Exception('[{}] {}: {}'.format(
            data['errors'][0]['code'],
            data['errors'][0]['message'],
            json.dumps(data['errors'][0]['params'])))
    result = []
    for key, value in kwargs.items():
        if key in data:
            if arr is True and isinstance(data[key], list):
                result.append([kwargs[key](x) for x in data[key]])
            else:
                result.append(kwargs[key](data[key]))
        else:
            result.append(None)
    return result


class Client:
    def __init__(self, api_url=None, api_key=None):
        self.api_url = api_url if api_url else Config.API_URL
        self.api_key = api_key if api_key else Config.API_TOKEN
        self.session = requests.Session()
        self.session.headers.update({'XF-Api-Key': self.api_key})

    def get_resource(self, resource_id: int) -> Resource:
        url = self.api_url + '/resources/' + resource_id
        response = self.session.get(url)
        return from_json(response.json(), resource=Resource)[0]

    def get_resource_versions(self, resource_id: int):
        url = self.api_url + '/resources/' + str(resource_id) + '/versions'
        response = self.session.get(url)
        return from_json(response.json(), arr=True, versions=Version)[0]
