import json
import base64
import tls_client

from typing import Dict

class TlsSession:    
    def __init__(self, token: str):
        self.token = token
        self.session = None 
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
            "Accept": "*/*",
            "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "X-Discord-Locale": "pl",
            "X-Discord-Timezone": "Europe/Warsaw",
            "X-Debug-Options": "bugReporterEnabled",
            "Alt-Used": "discord.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
        self._setup_session()

    def _setup_session(self):
        self.session = self.build_tls_session()

    def _get_cookie(self) -> str:
        response = self.session.get("https://discord.com/api/v9/users/@me")
        return response.cookies.get_dict()

    def _get_x_super_properties(self) -> str:
        super_properties = {
            "os": "Windows",
            "browser": "Firefox",
            "device": "",
            "system_locale": "pl",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
            "browser_version": "127.0",
            "os_version": "10",
            "referrer": "https://www.google.com/",
            "referring_domain": "www.google.com",
            "search_engine": "google",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 301920,
            "client_event_source": None,
            "design_id": 0
        }

        super_properties_json = json.dumps(super_properties)
        super_properties_bytes = super_properties_json.encode('utf-8')

        encoded_super_properties = base64.b64encode(super_properties_bytes)
        return encoded_super_properties.decode('utf-8')

    def _get_headers(self) -> Dict[str, str]:
        headers = self.headers.copy()  
        headers["Authorization"] = self.token
        headers["X-Super-Properties"] = self._get_x_super_properties()
        return headers
    
    def build_tls_session(self) -> tls_client.Session:
        session = tls_client.Session(
            client_identifier="firefox_120", 
            random_tls_extension_order=True
        )
        session.headers = self._get_headers()
        return session