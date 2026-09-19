from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from AWS CI/CD! version-2"


if __name__ == "__main__":
    test_home()
    print("All tests passed!")
