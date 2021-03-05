from color_check.website import app
from color_check.controllers.get_color_code import get_color_code


def test_get_color_code():
    assert get_color_code("red") == "#ff0000"

# our very first functional test
# instead of checking if a function() does it's job alone, this will check
# the entire response from the flask app, including the http status code.


def test_index():
    with app.test_client() as test_client:
        # mimic a browser: 'GET /', as if you visit the site
        response = test_client.get('/')

        # check that the HTTP response is a success
        assert response.status_code == 200

        # Store the contents of the html response in a local variable.
        # This should be a string with the same content as the file index.html
        html_content = response.data.decode()

        assert "<html>" in html_content


# check that there is a route at "/colors" which accepts a POST request
def test_colors():
    with app.test_client() as test_client:
        response = test_client.post('/color')
        assert response.status_code == 200
