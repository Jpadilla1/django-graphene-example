from graphene import relay, ObjectType, Field
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.fields import DjangoConnectionField, ConnectionOrListField
from graphene.contrib.django.types import DjangoNode

from .models import Post
from comments.models import Comment


class CommentNode(DjangoNode):
    class Meta:
        model = Comment
        filter_fields = {
            'author': ['exact', 'icontains', 'istartswith']
        }


class PostNode(DjangoNode):

    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'author': ['exact', 'icontains', 'istartswith']
        }
        filter_order_by = ['title', 'author']

    comments = DjangoConnectionField(CommentNode)



class Query(ObjectType):
    post = relay.NodeField(PostNode)
    posts = DjangoFilterConnectionField(PostNode)
    viewer = Field('self')

    class Meta:
        abstract = True


    def resolve_viewer(self, *args, **kwargs):
        return self
