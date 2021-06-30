import allure
import json

from urllib.parse import urljoin
from json import dumps

from allure_commons.types import AttachmentType

from src.clients.base_client import BaseClient
from src.configs import config as c
from src.utils.report_allure import ReportAllure

POST_URL = urljoin(c.BASE_URI, 'posts')

_headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json'
}

reporter = ReportAllure()


class PostService(BaseClient):

    @allure.step("Adding new post")
    def add_new_post(self):

        payload = dumps({
            'title': 'QA',
            'body': 'Prueba',
            'userId': 1})

        response = self.request.post(url=POST_URL, payload=payload, headers=_headers)
        reporter.attach_response_file(response.text, AttachmentType.JSON)
        if response.ok or response.status_code == 201:
            data = json.loads(response.text)
            return data

        return response

    @allure.step("Listing posts or Filtering")
    def get_posts(self, id=0):

        response = None

        if id > 0:
            response = self.request.get(url=POST_URL + '/{}'.format(id),
                                        headers=_headers)
        else:
            response = self.request.get(url=POST_URL, headers=_headers)

        reporter.attach_response_file(response.text, AttachmentType.JSON)
        if response.ok:
            return response.te

        return response

    @allure.step("Deleting an existing post")
    def delete_post(self, id: int):
        id_to_delete = POST_URL + '/{}'.format(str(id))
        response = self.request.delete(url=id_to_delete, headers=_headers)
        return response
