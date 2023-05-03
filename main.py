import requests
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read('settings.ini')

YAtoken = config["Yandex"]["token"]

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_path(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.put(f'{upload_url}?path={disk_file_path}', headers=headers)
        return response.status_code


ya = YandexDisk(token=YAtoken)

class TestRestApi:
    def test_response(self):
            assert ya._get_path('auto_test') == 201
            print("папка создана")
            assert ya._get_path('auto_test') == 409
            print("папка уже существует")


