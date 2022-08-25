from xf import Category, User


class Resource:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        self.alt_support_url = raw_data.get('alt_support_url', None)
        self.can_download = raw_data.get('can_download', None)
        self.can_edit = raw_data.get('can_edit', None)
        self.can_edit_icon = raw_data.get('can_edit_icon', None)
        self.can_edit_tags = raw_data.get('can_edit_tags', None)
        self.can_hard_delete = raw_data.get('can_hard_delete', None)
        self.can_soft_delete = raw_data.get('can_soft_delete', None)
        self.can_view_description_attachments = raw_data.get('can_view_description_attachments', None)
        self.category = Category(raw_data.get('Category', None))
        self.currency = raw_data.get('currency', None)
        self.custom_fields = raw_data.get('custom_fields', None)
        self.download_count = raw_data.get('download_count', None)
        self.external_url = raw_data.get('external_url', None)
        self.icon_url = raw_data.get('icon_url', None)
        self.is_watching = raw_data.get('is_watching', None)
        self.last_update = raw_data.get('last_update', None)
        self.prefix = raw_data.get('prefix', None)
        self.prefix_id = raw_data.get('prefix_id', None)
        self.price = raw_data.get('price', None)
        self.rating_avg = raw_data.get('rating_avg', None)
        self.rating_count = raw_data.get('rating_count', None)
        self.rating_weighted = raw_data.get('rating_weighted', None)
        self.resource_category_id = raw_data.get('resource_category_id', None)
        self.resource_date = raw_data.get('resource_date', None)
        self.resource_id = raw_data.get('resource_id', None)
        self.resource_state = raw_data.get('resource_state', None)
        self.resource_type = raw_data.get('resource_type', None)
        self.tag_line = raw_data.get('tag_line', None)
        self.tags = raw_data.get('tags', None)
        self.title = raw_data.get('title', None)
        self.user = User(raw_data.get('User', None))
        self.user_id = raw_data.get('user_id', None)
        self.username = raw_data.get('username', None)
        self.version = raw_data.get('version', None)
        self.view_count = raw_data.get('view_count', None)
        self.view_url = raw_data.get('view_url', None)


class Version:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        self.can_download = raw_data.get('can_download', None)
        self.can_hard_delete = raw_data.get('can_hard_delete', None)
        self.can_soft_delete = raw_data.get('can_soft_delete', None)
        self.download_count = raw_data.get('download_count', None)
        self.files = [File(file) for file in raw_data.get('files', None)]
        self.rating_avg = raw_data.get('rating_avg', None)
        self.rating_count = raw_data.get('rating_count', None)
        self.release_date = raw_data.get('release_date', None)
        self.resource_id = raw_data.get('resource_id', None)
        self.resource_version_id = raw_data.get('resource_version_id', None)
        self.version_state = raw_data.get('version_state', None)
        self.version_string = raw_data.get('version_string', None)
        self.view_url = raw_data.get('view_url', None)


class File:
    def __init__(self, raw_data: dict):
        self.raw = raw_data
        self.id = raw_data.get('id', None)
        self.filename = raw_data.get('filename', None)
        self.file_size = raw_data.get('file_size', None)
        self.download_url = raw_data.get('download_url', None)
