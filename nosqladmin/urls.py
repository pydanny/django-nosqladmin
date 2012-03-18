from django.conf.urls.defaults import patterns, url
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from nosqladmin import views

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name="nosqladmin_index"
    ),
    url(
        regex=r'^(?P<collection_name>[\._\-\w]+)/$',
        view=views.CollectionListView.as_view(),
        name="nosqladmin_collection_list"
    ),
)
"""    
    url(
        regex=r'^?P<collection_name>[_\-\w]+)/(?P<id>[\w]{24})/$',
        view=views.CollectionDetailView.as_view(),
        name="collection_detail"
    ),
    url(
        regex=r'^(?P<collection_name>[_\-\w]+)/(?P<id>[\w]{24})/edit/$',
        view=views.CollectionEditFormView.as_view(),
        name="collection_detail_edit_form"
    ),    
    url(
        regex=r'^(?P<collection_name>[_\-\w]+)/add/$',
        view=views.CollectionAddFormView.as_view(),
        name="collection_detail_add_form"
    ),
    url(
        regex=r'^(?P<collection_name>[_\-\w]+)/(?P<id>[\w]{24})/delete/$',
        view=views.CollectionDeleteView.as_view(),
        name="collection_delete"
    )

)
"""    