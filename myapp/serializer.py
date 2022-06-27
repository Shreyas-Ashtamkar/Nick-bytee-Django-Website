from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = homepage_movies
		fields = ['logo', 'title', 'description', 'links', 'type1', 'type2',
                    'rating', 'quality', 'age', 'new']
