from pystyle import Colorate, Colors, Center

class ColorHelper:
    @staticmethod 
    def color(text: str, color: Colors = Colors.cyan_to_green) -> str:
        return Colorate.Horizontal(color, text, 1)