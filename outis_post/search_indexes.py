# -*- encoding: utf-8 -*

from models import OutisPost
from haystack import indexes

class OutisPostIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    attraction = indexes.CharField(model_attr='attraction')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return OutisPost

    def index_queryset(self, using=None):
            return self.get_model().objects.all()
