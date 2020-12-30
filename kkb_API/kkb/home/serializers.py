from rest_framework import serializers
from .models import Article

class ArticleSerializers(serializers.ModelSerializer):

    image =serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model =Article
        # fields =['id','title','author','content','email']
        fields ='__all__'
