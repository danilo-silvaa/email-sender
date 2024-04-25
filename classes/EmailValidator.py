import re

class EmailValidator:
    @staticmethod
    def check(email):
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return bool(email_pattern.match(email))