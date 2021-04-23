import unittest
import json

"""When Python runs a file as a top-level script its name is set to __main__.
However, when running a script with the -m flag, imports are resolved using __package__ variable.
By running this script from its outer directory and using the -m flag
(like python -m outer.tests.script_name) and setting the __package__
to outer.tests, the double-dot import works.
"""
__package__ = "code.tests"

from ..powertools import main

PROPUBLICA_API_KEY = "55x8VRxY10PA8kBJICoD1Uv3HzYfkfCP7TyuGtzK"
GOVTRACK_API_KEY = "XXQfHeGLDpb69qz9ZdtcL1ao8grxHaf7cXCXdVXY"


def is_json(data: str) -> bool:
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


class TestRequests(unittest.TestCase):
    def test_Datatable(self):
        response = main.generate_datatable_JSON(PROPUBLICA_API_KEY, "police")[0]
        self.assertEqual(response.status_code, 200)

    def test_bill_data(self):
        response = main.generate_bill_data(PROPUBLICA_API_KEY, "hr1628")[0]
        self.assertEqual(response.status_code, 200)

    def test_bill_fulltext(self):
        response = main.generate_bill_fulltext(PROPUBLICA_API_KEY, "hr", "1628")[0]
        self.assertEqual(response.status_code, 200)

    def test_members_by_state(self):
        response = main.get_members_by_state(PROPUBLICA_API_KEY, "NY")[0]
        self.assertEqual(response.status_code, 200)

    def test_member_by_id(self):
        response = main.get_member_by_id(PROPUBLICA_API_KEY, "K000388")[0]
        self.assertEqual(response.status_code, 200)


class TestValidJSON(unittest.TestCase):
    def test_generate_datatable_JSON(self):
        data = main.generate_datatable_JSON(PROPUBLICA_API_KEY, "police")[1]
        self.assertTrue(is_json(data))


if __name__ == "__main__":
    unittest.main()
