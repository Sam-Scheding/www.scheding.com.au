from django.conf import settings

class TitleMixin(object):

    page_title = 'Title Not Set'
    active_tab = 'dashboard'

    def title(self):
        return self.page_title

    def project_name(self):
        return settings.PROJECT_NAME

    def active_tab(self):
        return self.active_tab
