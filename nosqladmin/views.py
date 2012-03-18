from django.views.generic import ListView

from nosqladmin.mixins import NosqlAdminViewMixin

class IndexView(NosqlAdminViewMixin, ListView):

    template_name = "nosqladmin/index.html"
    queryset = []
    
    def get_queryset(self):
        return self.get_nosqladmins()