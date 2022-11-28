import unittest

from TwitterAPI2_0_parser import append_valid_to_master_frame, frame_from_json

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

    def test_append_valid_to_master_frame(self):
        invalid_json = """{
            "query": "foo"
        }"""
        append_valid_to_master_frame(invalid_json, "x")

if __name__ == '__main__':
    unittest.main()