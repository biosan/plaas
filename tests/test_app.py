import falcon
from falcon import testing

import pytest

from plaas.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_generated_plot_img(client):
    # TODO: Improve testing by separating request test from plot generation test.
    #       Generate the image inside test funcition using MatPlotLib and compare it
    #       with API response. This will make this test more robust and will allow
    #       random sequences of data to be tested easly.
    query = {
        'title': 'Title',
        'data': [1, 5, 1.7, 1.1, 1.234, 12]
    }
    #query_str = to_query_str(query)

    # Simple (and hopefully temporary) workaround
    resp_img = bytearray(open('tests/plot-1-5-1.7-1.1-1.234-12.png', 'rb').read())

    response = client.simulate_get('/plot', params = query)
    result_doc = response.content

    assert result_doc == resp_img
    assert response.status == falcon.HTTP_OK