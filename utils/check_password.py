import re


class CheckPassword:
    @staticmethod
    def check_password(password: str):
        pattern = r"^(?=.*[A-ZÖĞİƏÇŞÜ])(?=.*[a-zöğıiəçşü])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-zÖĞİƏÇŞÜöğıiəçşü0-9@$!%*?&.]{8,}$"
        if isinstance(password, str):
            if re.match(pattern, password):
                return True
            else:
                return False
        return False
