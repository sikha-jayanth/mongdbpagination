from rest_framework import serializers
from  drfexample.settings import db

class BooksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    language = serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)

    # def create(self, validated_data):
    #     # title=validated_data['title']
    #     # language=validated_data['language']
    #     # author=validated_data['author']
    #     return db.books.insert_one(validated_data)



    
