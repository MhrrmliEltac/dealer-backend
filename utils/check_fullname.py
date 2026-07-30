import re


class CheckFullname:
    @staticmethod
    def check_fullname(fullname: str):
        pattern = r"^[A-Za-zƏəÖöÜüÇçŞşĞğİıI]+(?:[ '-][A-Za-zƏəÖöÜüÇçŞşĞğİıI]+)+$"
        match = re.match(pattern, fullname)
        if match:
            return True
        return False
