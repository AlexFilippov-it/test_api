import pytest
import cerberus
import requests


@pytest.mark.parametrize("code", [200])
def test_url_status(base_url, code, request_method):
    target = base_url
    response = request_method(url=target)
    assert response.status_code == code


def test_api_json_schema(base_url):
    res = requests.get(base_url)

    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"},
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
