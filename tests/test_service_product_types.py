import pytest
import requests_mock
from commercetools import types
from requests.exceptions import HTTPError


def product_types_get(client):
    product_type = client.product_types.create(types.ProductTypeDraft(key="test-product-type"))

    assert product_type.id
    assert product_type.key == "test-product-type"

    product_type = client.product_types.get_by_id(product_type.id)
    assert product_type.id
    assert product_type.key == "test-product-type"

    with pytest.raises(HTTPError) as e:
        client.product_types.get_by_id("invalid")

    product_type = client.product_types.get_by_key(product_type.key)
    assert product_type


def test_product_type_query(client):
    client.product_types.create(types.ProductTypeDraft(key="test-product-type1"))
    client.product_types.create(types.ProductTypeDraft(key="test-product-type2"))

    # single sort query
    result = client.product_types.query(sort="id asc")
    assert len(result.results) == 2
    assert result.total == 2

    # multiple sort queries
    result = client.product_types.query(sort=["id asc", "name asc"])
    assert len(result.results) == 2
    assert result.total == 2


@pytest.mark.skip(reason="find out why this one fails")
def test_product_update(client):
    product_type = client.product_types.create(types.ProductTypeDraft(
        key="test-product-type",
        name="Test Product Type"))

    assert product_type.id
    assert product_type.name == "Test Product Type"

    product_type = client.product_types.update_by_id(
        id=product_type.id,
        version=product_type.version,
        actions=[
            types.ProductTypeChangeNameAction(name="Renamed Product Type")
        ],
    )
    assert product_type.name == "Renamed Product Type"

    product_type = client.product_types.update_by_key(
        key="test-product-type",
        version=product_type.version,
        actions=[
            types.ProductTypeChangeNameAction(name="Renamed productType")
        ],
    )
    assert product_type.name == "Renamed productType"
