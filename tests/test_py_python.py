import unittest

from tests.basetest import BaseTest
from tplmap.plugins.languages.python import Python


class PythonTests(unittest.TestCase, BaseTest):

    expected_data = {
        "language": "python",
        "engine": "python",
        "evaluate": "python",
        "execute": True,
        "read": True,
        "write": True,
        "prefix": "",
        "suffix": "",
        "render": """str(%(code)s)""",
        "header": """'%(header)s'+""",
        "trailer": """+'%(trailer)s'""",
        "bind_shell": True,
        "reverse_shell": True,
    }

    expected_data_blind = {
        "language": "python",
        "engine": "python",
        "blind": True,
        "execute_blind": True,
        "evaluate_blind": "python",
        "write": True,
        "prefix": "",
        "suffix": "",
        "bind_shell": True,
        "reverse_shell": True,
    }

    url = "http://localhost:15001/reflect/eval?inj=*&tpl=%s"
    url_blind = "http://localhost:15001/blind/eval?inj=*&tpl=%s"
    plugin = Python

    blind_tests = [
        (0, 0, "%s", {}),
    ]

    reflection_tests = [
        (0, 0, "%s", {}),
    ]
