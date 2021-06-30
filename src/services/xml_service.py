from urllib.parse import urljoin

import allure
import requests
from allure_commons.types import AttachmentType

from src.clients.base_client import BaseClient
from src.utils.report_allure import ReportAllure

BASE_URL = "http://mockbin.com/"

REQUEST_URL = urljoin(BASE_URL, 'request?param=test')

_headers = {
    "content-type": "application/xml",
    "accept": "application/xml"
}

reporter = ReportAllure()


class XmlService(BaseClient):

    @allure.step("Listing data from a soap service")
    def get_xml_response(self):
        response = self.request.get(REQUEST_URL, headers=_headers)
        reporter.attach_response_file(response.text, attachment_type=AttachmentType.XML)
        if response.ok:
            return response
        else:
            return None
