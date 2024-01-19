import unittest

from improved_json import JsonType, ImprovedJsonType, code, loads


class TestTypeCheck(unittest.TestCase):
    """
    Test improved_json's json type checking
    """

    def test_correct(self):
        loads("1", int)
        loads('""', str)

    def test_incorrect(self):
        with self.assertRaises(TypeError):
            loads("1", str)
        with self.assertRaises(TypeError):
            loads('""', int)

    def test_custom(self):
        loads("[1,1]", ImprovedJsonType)
        for type_ in (JsonType, ImprovedJsonType):
            loads("1", type_)
            loads("[1,1]", type_)
            loads('{"s":2}', type_)

    def test_custom_incorrect(self):
        for pf in (code.PATH_PREFIX, code.BYTES_PREFIX_TXT, code.BYTES_PREFIX_ENC):
            p_str = f'"{pf}/"'
            with self.assertRaises(TypeError):
                loads(p_str, JsonType)
            with self.assertRaises(TypeError):
                loads(f"[{p_str}]", JsonType)
            with self.assertRaises(TypeError):
                loads(f"{{{p_str}:2}}", JsonType)


if __name__ == "__main__":
    unittest.main()
