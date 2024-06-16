import uuid

from pystyle import Colors

from helpers.colors import ColorHelper
from utils.tls_session import TlsSession

class Booster:
    def __init__(self, token: str) -> None:
        self.token = token
        self.tls_instance = TlsSession(token)
        self.session = self.tls_instance.build_tls_session()

    def _process_response(self, module: str, status_code: int) -> None:
        if status_code in [200, 201, 204]:
            print(f"{ColorHelper.color(f'[+]', Colors.green_to_white)} " +
                  f"Successfully {module}ed the server ({status_code})")
        else:
            print(f"{ColorHelper.color(f'[-]', Colors.red_to_white)} " + 
                  f"Failed to {module} the server ({status_code})")

    def _get_boost_slots(self) -> list:
        response = self.session.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots")
        return response.json()
    
    def join_server(self, invite_code: str) -> None:
        response = self.session.post(
            f"https://discord.com/api/v9/invites/{invite_code}", 
            json={"session_id": uuid.uuid4().hex }
        )
        self._process_response("join", response.status_code)
    
    def boost_server(self, server_id: str, boost_count: int) -> None:
        slots = self._get_boost_slots()
        for i in range(int(boost_count)):
            response = self.session.put(
                f"https://discord.com/api/v9/guilds/{server_id}/premium/subscriptions",
                json={"user_premium_guild_subscription_slot_ids": [slots[i]['id']]}
            )
            self._process_response("boost", response.status_code)