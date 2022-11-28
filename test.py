import unittest

from TwitterAPI2_0_parser import frame_from_json

class TestSum(unittest.TestCase):
    def test_frame_from_json_handles_json(self):
        valid_json = """{
            "data": [
                {
                    "referenced_tweets": [],
                    "text": "foo"
                }
            ]
        }"""
        self.assertEqual(frame_from_json(valid_json).empty, False)

    def test_frame_from_json_handles_invalid_json(self):
        invalid_json = """{
            "query": "foo"
        }"""
        self.assertEqual(frame_from_json(invalid_json).empty, False)

if __name__ == '__main__':
    unittest.main()