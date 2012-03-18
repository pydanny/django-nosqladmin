from django.views.generic import ListView

import pymongo

from nosqladmin.mixins import NosqlAdminViewMixin

# TODO Move this to settings or something...
CONNECTION = pymongo.Connection("localhost", 27017)

class IndexView(NosqlAdminViewMixin, ListView):

    template_name = "nosqladmin/index.html"
    queryset = []
    
    def get_queryset(self):
        return self.get_nosqladmins()

class CollectionListView(NosqlAdminViewMixin, ListView):
    
    template_name = "nosqladmin/collection_list.html"
    
    def get_queryset(self):
        self.set_nosqladmin()        
        db = getattr(CONNECTION, self.get_db_name())
        collection = getattr(db, self.get_collection_name())
        return collection.find()
        
    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)            
        context['collection_name'] = self.collection_name
        return context