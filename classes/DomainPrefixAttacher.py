class DomainPrefixAttacher:
    def __init__(self, domain, prefixes):
        self.domain = domain
        self.prefixes = prefixes

    def attach_prefixes(self):
        return [f"{prefix}@{self.domain}" for prefix in self.prefixes]