import requests

from lib.apiwrapper import *


class TestNegative:
    def test_post_empty_form_http_status(self):
        assert post_for_result().status_code == 400

    def test_post_form_n_equals_0_http_status(self):
        assert post_for_result(0).status_code == 400

    def test_post_form_n_equals_9_http_status(self):
        assert post_for_result(9).status_code == 400

    def test_post_form_n_equals_minus1_http_status(self):
        assert post_for_result(-1).status_code == 400

    def test_post_form_without_n_http_status(self):
        response = requests.post(BASE_URL, data={})
        assert post_for_result(-1).status_code == 400

    def test_post_form_n_is_float_http_status(self):
        assert post_for_result(5.8).status_code == 400

    def test_post_form_n_is_string_http_status(self):
        assert post_for_result("some").status_code == 400

    def test_post_form_non_exist_endpoint_http_status(self):
        response = requests.post(f'{BASE_URL}okyjhpyhiojyhj')
        assert response.status_code == 404

    def test_path_request_http_status(self):
        response = requests.patch(BASE_URL)
        assert response.status_code == 405

    def test_put_request_http_status(self):
        response = requests.put(BASE_URL)
        assert response.status_code == 405

    def test_delete_request_http_status(self):
        response = requests.delete(BASE_URL)
        assert response.status_code == 405


class TestClass:
    def test_get_form_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_http_status(self):
        assert post_for_result(5).status_code == 200

    def test_post_form_n_equals_3(self):
        expected = ' '.join(str(x) for x in ["((()))", "(()())", "(())()", "()(())", "()()()"])
        assert post_for_result(3).text == expected

    def test_post_form_n_equals_1(self):
        expected = ' '.join(str(x) for x in ["()"])
        assert post_for_result(1).text == expected

    def test_post_form_n_equals_2(self):
        expected = ' '.join(str(x) for x in ["(())", "()()"])
        assert post_for_result(2).text == expected

    def test_post_form_n_equals_8(self):
        expected_result_size = 1430
        assert len(post_for_result(8).text.split(' ')) == expected_result_size

    def test_post_form_n_equals_6(self):
        expected_result_size = 132
        assert len(post_for_result(6).text.split(' ')) == expected_result_size

    def test_post_form_n_equals_7(self):
        expected_result_size = 429
        assert len(post_for_result(7).text.split(' ')) == expected_result_size

    def test_post_form_with_jwt_http_status(self):
        response = requests.post(BASE_URL, data={"number": 6}, headers={
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM'})
        assert response.status_code == 200

    def test_post_form_with_jwt_correct_result(self):
        response = requests.post(BASE_URL, data={"number": 6}, headers={
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM'})
        expected_result_size = 132
        assert len(response.text.split(' ')) == expected_result_size

    def test_post_form_with_extra_fields_http_status_without_error(self):
        response = requests.post(BASE_URL, data={"number": 6, "some": 9897078})
        assert response.status_code == 200

    def test_post_form_with_extra_fields_return_correct_result(self):
        response = requests.post(BASE_URL, data={"number": 6, "some": 9897078})
        expected_result_size = 132
        assert len(response.text.split(' ')) == expected_result_size

    def test_get_form_content_type(self):
        assert get_form().headers['Content-type'] == "text/html; charset=utf-8"
