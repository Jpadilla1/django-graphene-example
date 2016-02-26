import graphene

from posts.schema import Query as PostQuery

class Query(PostQuery):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(name='Blog Schema')
schema.query = Query
