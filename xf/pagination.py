class Pagination:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        self.current_page = raw_data.get('current_page', None)
        self.last_page = raw_data.get('last_page', None)
        self.per_page = raw_data.get('per_page', None)
        self.shown = raw_data.get('shown', None)
        self.total = raw_data.get('total', None)
