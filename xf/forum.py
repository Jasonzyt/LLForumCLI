from xf.breadcrumb import Breadcrumb


class Forum:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        if raw_data['breadcrumbs'] is not None:
            self.breadcrumbs = [Breadcrumb(x) for x in raw_data['breadcrumbs']]
        else:
            self.breadcrumbs = None
        self.description = raw_data.get('description', None)
        self.display_in_list = raw_data.get('display_in_list', None)
        self.display_order = raw_data.get('display_order', None)
        self.node_id = raw_data.get('node_id', None)
        self.node_name = raw_data.get('node_name', None)
        self.node_type_id = raw_data.get('node_type_id', None)
        self.parent_node_id = raw_data.get('parent_node_id', None)
        self.title = raw_data.get('title', None)
        self.type_data = raw_data.get('type_data', None)
        self.view_url = raw_data.get('view_url', None)
