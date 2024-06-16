import unittest
from unittest.mock import Mock

from src.utils.tls_session import TlsSession

print("\nRunning tests for tls_session.py:")

class TestTlsSession(unittest.TestCase):
    def setUp(self):
        self.token = "token"
        self.session = TlsSession(self.token)

    def test_initialization(self):
        self.assertEqual(self.session.token, self.token)
        self.assertIsNotNone(self.session.session)

    def test_get_x_super_properties(self):
        expected_properties = (
            "eyJvcyI6ICJXaW5kb3dzIiwgImJyb3dzZXIiOiAiRmlyZWZveCIsICJkZXZpY2UiOiAiIiwgInN5c3RlbV9sb2NhbGUiOiAicGwiLCAiYnJvd3Nlcl91c2VyX2FnZW50IjogIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwgImJyb3dzZXJfdmVyc2lvbiI6ICIxMjcuMCIsICJvc192ZXJzaW9uIjogIjEwIiwgInJlZmVycmVyIjogImh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwgInJlZmVycmluZ19kb21haW4iOiAid3d3Lmdvb2dsZS5jb20iLCAic2VhcmNoX2VuZ2luZSI6ICJnb29nbGUiLCAicmVmZXJyZXJfY3VycmVudCI6ICIiLCAicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjogIiIsICJyZWxlYXNlX2NoYW5uZWwiOiAic3RhYmxlIiwgImNsaWVudF9idWlsZF9udW1iZXIiOiAzMDE5MjAsICJjbGllbnRfZXZlbnRfc291cmNlIjogbnVsbCwgImRlc2lnbl9pZCI6IDB9"
        )
        result = self.session._get_x_super_properties()
        self.assertEqual(result, expected_properties)

    def test_get_headers(self):
        expected_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
            "Accept": "*/*",
            "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk5NTUwMTk1MjU3NjI1ODE1OSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDU5MzMxMzYwMTU1NzYyNzcwIiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==",
            "X-Discord-Locale": "pl",
            "X-Discord-Timezone": "Europe/Warsaw",
            "X-Debug-Options": "bugReporterEnabled",
            "Alt-Used": "discord.com",
            "Connection": "keep-alive",
            "Cookie": "__dcfduid=8c867a40e92111ee9b6e9b635f5abb28; __sdcfduid=8c867a41e92111ee9b6e9b635f5abb280c3b19eac0fffbce219fb56262a67a18d3a04ccfe6f01acc4cec4b12512e13ae; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jun+15+2024+17%3A46%3A29+GMT%2B02",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Authorization": self.token,
            "X-Super-Properties": self.session._get_x_super_properties(),
        }
        result = self.session._get_headers()
        self.assertEqual(result, expected_headers)

    def test_build_tls_session(self):
        result = self.session.build_tls_session()
        self.assertEqual(result.client_identifier, "firefox_120")
        self.assertTrue(result.random_tls_extension_order)

if __name__ == "__main__":
    unittest.main()