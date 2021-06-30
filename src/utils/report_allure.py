
import allure
import moment
import uuid
from allure_commons.types import AttachmentType, Severity


class ReportAllure:
    now = moment.now().strftime("%d-%m-%Y")

    def attach_response_file(self, data: str, attachment_type: str, severity_level: str = Severity.NORMAL, ):
        allure.attach(data, attachment_type=attachment_type)


class ReportAllureBuilder:

    def set_title(self, title: str):
        allure.title(title)
        return self

    def set_suite(self, suite_name: str):
        allure.suite(suite_name)
        return self

    def set_description(self, description: str):
        allure.description(description)
        return self

    def set_description(self, description: str):
        allure.description(description)
        return self
