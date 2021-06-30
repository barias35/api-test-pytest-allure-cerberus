import allure
from allure_commons.types import AttachmentType
from lxml import etree

from services import XmlService
from services.post_service import PostService
from src.models import User, Post
from src.models.user import get_user_schema

from src.services import UserService, PostService

from assertpy.assertpy import assert_that
from cerberus import Validator


def test_get_users():
    users = []
    data = UserService.get_users()
    for json_obj in data:
        users.append(User(**json_obj))

    assert_that(users).is_not_equal_to([])
    assert_that(users[0].id).is_equal_to(1)


def test_new_post_can_be_added():
    response = PostService.add_new_post()
    valid_json = bool(response)
    if valid_json:
        post_object = Post(**response)
        print(post_object)
        assert_that(post_object.title).is_equal_to("QA")
    else:
        assert False, "Unexpected Response! - " + response.text


def test_post_can_be_deleted():
    response = PostService.delete_post(1)
    assert_that(response.status_code).is_equal_to(200)


def test_read_one_operation_has_expected_schema():

    v = Validator(get_user_schema())
    user_object = UserService.get_users()[0]
    is_valid = v.validate(user_object)

    assert_that(is_valid, description=v.errors).is_true().snapshot()


def test_xml_response_can_be_readed():
    response_xml = XmlService.get_xml_response()
    tree = etree.fromstring(bytes(response_xml.text, encoding='utf-8'))

    custom_param_node = tree.xpath("//response/queryString/*")[0]

    # assert_that(custom_param_node.text).is_equal_to("test")
    assert_that(custom_param_node.tag).is_equal_to("param")
