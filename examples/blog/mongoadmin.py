from nosqladmin.mongodb import MongoAdmin

class PostAdmin(MongoAdmin):
    collection_name = "example_blog.post"