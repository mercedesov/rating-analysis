
import pytest
from reports.average_rating import average_rating_report

def test_average_rating_report():
    data = [
        {'name': 'iphone', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'macbook', 'brand': 'apple', 'price': '1299', 'rating': '4.8'},
        {'name': 'galaxy', 'brand': 'samsung', 'price': '1199', 'rating': '4.7'}
    ]
    result = average_rating_report(data)
    assert result[0][0] == 'apple'
    assert isinstance(result, list)
    assert all(isinstance(i, tuple) for i in result)
