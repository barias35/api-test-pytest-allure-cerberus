import json
from urllib.parse import urljoin

import allure
from allure_commons.types import AttachmentType

from src.clients.base_client import BaseClient
from src.configs import config

from utils.report_allure import ReportAllure

reporter = ReportAllure()

USERS_URL = urljoin(config.BASE_URI, 'users')

_headers = {
    'Accept': 'application/json'
}


class UserService(BaseClient):

    @allure.step("Listing users")
    def get_users(self):
        response = self.request.get(USERS_URL, _headers)
        reporter.attach_response_file(response.text, AttachmentType.JSON)
        if response.ok:
            data = json.loads(response.text)
            return data
        return response
