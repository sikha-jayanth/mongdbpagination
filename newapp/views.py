from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import BooksSerializer
from drfexample.settings import db
from rest_framework import status
import json

# Create your views here.


# class BookCreateView(CreateAPIView):
#     serializer_class=BooksSerializer
#     permission_classes=[AllowAny]

class BooksList(APIView):
    """
    # List all snippets, or create a new snippet.
    # """
    def get(self, request, format=None):
        output=[]
        # for q in db.books.find():
        #     output.append({'title' : q['title'], 'language' : q['language'],'author':q['author']})
        # print(output)
        # resp=json.dumps(output)
        for q in db.books.find():
            # output.append({'title' : q['title'], 'language' : q['language'],'author':q['author']})
            output.append(q)
        serializer = BooksSerializer(output,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            db.books.insert_one(serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookPaginateCursor(APIView):
    def get(self, request, format=None):
        output=[]
        skips=2
        page_size=5
        cursor = db.books.find().skip(skips).limit(page_size)
            # for q in db.books.find():
            # # output.append({'title' : q['title'], 'language' : q['language'],'author':q['author']})
            #     output.append(q)
        output=[x for x in cursor]
        serializer = BooksSerializer(output,many=True)
        return Response(serializer.data)

class BookPaginateId(APIView):
    def get(self, request, format=None,last_id=None):
        output=[]
        page_size=int(request.GET.get('size'))
        if last_id is None:
            # When it is first page
            cursor = db.books.find().limit(page_size)
        else:
            cursor = db.books.find({'_id': {'$gt': last_id}}).limit(page_size)
        output=[x for x in cursor]
        serializer = BooksSerializer(output,many=True)
        last_id = output[-1]['_id']

        return Response(serializer.data)
        
            
        

