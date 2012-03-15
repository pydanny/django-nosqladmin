from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.importlib import import_module

from nosql import exceptions

class NosqlAdminViewMixin(object):

    def render_to_response(self, context, **response_kwargs):
        if hasattr(self, 'permission') and self.permission not in context:
            return HttpResponseForbidden("You do not have permissions to access this content.")

        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = context,
            **response_kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(MongonautViewMixin, self).get_context_data(**kwargs)
        context['NOSQLADMIN_JQUERY'] = getattr(settings, "NOSQLADMIN_JQUERY", "http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js")
        context['NOSQLADMIN_TWITTER_BOOTSTRAP'] = getattr(settings, "NOSQLADMIN_TWITTER_BOOTSTRAP", "http://twitter.github.com/bootstrap/assets/css/bootstrap.css")
        context['NOSQLADMIN_TWITTER_BOOTSTRAP_ALERT'] = getattr(settings, "NOSQLADMIN_TWITTER_BOOTSTRAP_ALERT", "http://twitter.github.com/bootstrap/assets/js/bootstrap-alert.js")
        return context
    
    def get_nosqladmins(self):
        """ Returns a list of all nosqladmin implementations for the site 
        """
        nosqladmins = []        
        for nosqladmin in settings.NOSQLADMINS:
            try:
                # TODO - change this to bring in class, not a module
                module = import_module(nosqladmin[0])
            except IndexError:
                raise exceptions.NosqlAdminModuleNotFound(str(nosqladmin))
            
            try:
                nosqladmins.append(module.__dict__[nosqladmin[1]])
            except KeyError:
                raise exceptions.NosqlAdminClassNotFound(str(nosqladmin))
        return nosqladmins
        
    
    def set_nosqladmin(self):
        """ Sets a number of commonly used attributes """        
        
        if hasattr(self, "nosqladmin"):
            # prevents us from calling this multiple times            
            return None        
        self.collection_name = self.kwargs.get('collection_name')
        
        for nosqladmin in self.get_nosqladmins():
            if self.collection_name == nosqladmin.collection_name:
                self.nosqladmin = nosqladmin()
                break
        
        # TODO change this to use 'finally' or 'else' or something
        if not hasattr(self, "nosqladmin"):
            raise NoNosqlAdminSpecified("No NosqlAdmin specified for {0}.{1}".format(self.app_label, self.document_name))
                
    def set_permissions_in_context(self, context={}):
        """ Provides permissions for mongoadmin for use in the context"""
        
        context['has_view_permission'] = self.nosqladmin.has_view_permission(self.request)
        context['has_edit_permission'] = self.nosqladmin.has_edit_permission(self.request)
        context['has_add_permission'] = self.nosqladmin.has_add_permission(self.request)
        context['has_delete_permission'] = self.nosqladmin.has_delete_permission(self.request)
        return context