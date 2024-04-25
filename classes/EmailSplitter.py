class EmailSplitter:
    @staticmethod
    def split_email(email):
        parts = email.split('@')
        if len(parts) == 2:
            return parts[0], parts[1]
        else:
            return None, None