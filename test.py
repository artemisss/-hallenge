import unittest
import main

test_case_data = [
    {
        "value": "@id:22",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "=",
            "value": "22",
        },
    },
    {
        "value": "@id:>30",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": ">",
            "value": "30",
        },
    },
    {
        "value": "@id:>=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": ">=",
            "value": "100",
        },
    },
    {
        "value": "@id:<30",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "<",
            "value": "30",
        },
    },
    {
        "value": "@id:<=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "<=",
            "value": "100",
        },
    },
    {
        "value": "@id:!=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "!=",
            "value": "100",
        },
    },
    {
        "value": "#office",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "=",
            "value": None,
        },
    },
    {
        "value": "#office:1010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "=",
            "value": "1010",
        },
    },
    {
        "value": "#office:>101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": ">",
            "value": "101010",
        },
    },
    {
        "value": "#office:>=101011",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": ">=",
            "value": "101011",
        },
    },
    {
        "value": "#office:<101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "<",
            "value": "101010",
        },
    },
    {
        "value": "#office:<=101011",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "<=",
            "value": "101011",
        },
    },
    {
        "value": "#office:!=101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "!=",
            "value": "101010",
        },
    },
]


class ParserTestCase(unittest.TestCase):
    def test_parser(self):
        for t in test_case_data:
            result = main.Parser(t['value'])
            self.assertEqual(t['expected'], result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
