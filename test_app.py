from app import app, entries

import pytest

# Use Flask's test client for testing


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


def test_add_entry(client):
    # Test adding an entry
    response = client.post(
        "/add_entry", data={"content": "Test Entry Content"}
    )  # noqa: E501

    # Check if the response is a redirect to the index page
    assert response.status_code == 302
    assert response.headers["Location"] == "/"

    # Check if the entry was added to the database
    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"


# this is a comment used to test the pull request
def test_add_entry_with_happiness(client):
    response = client.post(
        "/add_entry", data={"content": "Test Entry Content", "happiness": "😃"}
    )

    assert response.status_code == 302
    assert response.headers["Location"] == "/"

    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"
    assert entry.happiness == "😃"
