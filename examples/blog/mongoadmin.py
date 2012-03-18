from nosqladmin.mongodb import MongoAdmin

class PostAdmin(MongoAdmin):
    collection_name = "example_blog.post"
    
    def has_add_permission(self, request):
        return True