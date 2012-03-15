class BaseNosqlAdmin(object):
    
    def collection_name(self):
        """ This needs to be a string that represents the modelname"""
        raise NotImplemented
    
    search_fields = []
    list_fields = []
    form_template = {}
    
    def has_view_permission(self, request):
        return True

    def has_edit_permission(self, request):
        return True
        
    def has_delete_permission(self, request):
        return True
        
    def has_create_permission(self, request):
        return True
        
