"""Test app.py file.

Yields:
    _type_: _description_
"""

import pytest

from app import app


#replace part of code ie flask
@pytest.fixture
def client():
    """Mock flask app.

    Yields:
        _type_: _description_
    """
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        #test client flask mock
        yield client


def test_get_beer(client):
    """Get list beer in reserve.

    Args:
        client (_type_): _description_
    """
    resp = client.get("/list")
    assert (
        b'[{"beer":"Paix Dieux","quantity":2,"typeBeer":"triple"},'
        b'{"beer":"Chimay","quantity":1,"typeBeer":"triple"}]\n' in resp.data
    )


def test_get_with_name_beer_not_exist(client):
    """Get beer does not exist in reserve.

    Args:
        client (_type_): _description_
    """
    resp = client.get("/list?beer_choose=Bellenaert")
    assert b'{"error":"Don\'t have beer \'Bellenaert\'"}\n' in resp.data


def test_get_with_name_beer_exist(client):
    """Get beer exist in reserve.

    Args:
        client (_type_): _description_
    """
    resp = client.get("/list?beer_choose=Paix Dieux")
    assert b'[{"beer":"Paix Dieux","quantity":2,"typeBeer":"triple"}]\n' in resp.data


def test_post_add_new_beer(client):
    """Add new beer.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/addBeer", json={"beer": "Bellenaert", "quantity": 1, "typeBeer": "blonde"})
    assert b"{\"Add beer\":\"Add this beer : 'Bellenaert', quantity : '1'\"}\n" in resp.data


def test_post_add_beer(client):
    """Add quantity in beer in reserve.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/addBeer", json={"beer": "Chimay", "quantity": 1, "typeBeer": "triple"})
    assert b"{\"Add quantity\":\"Add quantity for this beer : 'Chimay', new quantity : '2'\"}\n" in resp.data


def test_post_add_new_type_beer(client):
    """Add new type beer in reserve.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/addBeer", json={"beer": "Chimay", "quantity": 1, "typeBeer": "blonde"})
    assert b"{\"Add beer\":\"Add this beer : 'Chimay', quantity : '1'\"}\n" in resp.data


def test_post_drink_beer_existing_just_quantity(client):
    """Want drink beer existing with just quantity.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/drinkBeer", json={"beer": "Chimay", "quantity": 2, "typeBeer": "triple"})
    assert b'{"warning":"There will be no more beer \'Chimay\' in reserve after this one !!!"}\n' in resp.data


def test_post_drink_beer_existing_good_quantity(client):
    """Want drink beer existing with good quantity.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/drinkBeer", json={"beer": "Paix Dieux", "quantity": 1, "typeBeer": "triple"})
    assert b'{"Beer drink":"New quantiy for beer \'Paix Dieux\' in reserve : 1"}\n' in resp.data


def test_post_drink_beer_not_existing_good_quantity(client):
    """Want drink beer not exist with good quantity.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/drinkBeer", json={"beer": "Paix Dieux", "quantity": 5, "typeBeer": "triple"})
    assert b'{"error":"Don\'t have enough beer \'Paix Dieux\' in reserve, 3 beer(s) missing ..."}\n' in resp.data


def test_post_drink_beer_not_beer(client):
    """Want drink beer not exist.

    Args:
        client (_type_): _description_
    """
    resp = client.post("/drinkBeer", json={"beer": "DK", "quantity": 5, "typeBeer": "triple"})
    assert b'{"error":"Don\'t have beer \'DK\' in the reserve ...."}\n' in resp.data
