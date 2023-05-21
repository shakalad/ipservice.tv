from django.contrib.admin.widgets import ForeignKeyRawIdWidget


class SearchableForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    def __init__(self, rel, admin_site, attrs=None, using=None):
        super(SearchableForeignKeyRawIdWidget, self).__init__(rel, admin_site, attrs, using)

    def render(self, name, value, attrs=None, renderer=None):
        self.rel.limit_choices_to = {'name__icontains': value}
        output = super().render(name, value, attrs)
        self.rel.limit_choices_to = {}
        return output
