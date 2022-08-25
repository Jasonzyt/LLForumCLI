class Breadcrumb:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        self.node_id = raw_data.get('node_id', None)
        self.title = raw_data.get('title', None)
        self.node_type_id = raw_data.get('node_type_id', None)
