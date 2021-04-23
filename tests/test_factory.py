import sys

sys.path.append("..")
from src.reform import create_app

import sys
import pytest

test_config = {}


@pytest.fixture
def client():

    app = create_app(
        test_config={
            "TESTING": True,
        }
    )

    with app.test_client() as client:
        yield client


def test_about(client):
    rv = client.get("/")
    assert b"No" in rv.data
