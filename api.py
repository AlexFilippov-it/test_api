import pytest


@pytest.mark.parametrize("code", [200])
def test_url_status(base_url, code, request_method):
    target = base_url
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.parametrize("encoding", ['utf-8'])
def test_url_encoding(base_url, encoding, request_encoding):
    target = base_url
    response_encod = request_encoding(url=target)
    assert response_encod.encoding == encoding
