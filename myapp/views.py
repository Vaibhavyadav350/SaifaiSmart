# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer
from .mongo_connector import client  # Import the Product model
from .renderers import JSONRendererWithTemplate
from django.shortcuts import render
#GET
class ProductListGet(APIView):
    renderer_classes = [JSONRendererWithTemplate]  # Use the custom renderer
    def get(self, request):
        db = client['Mart']
        collection = db['Grocery']
        name_query = request.query_params.get('category', None)  # Get the 'name' query parameter
        query = {}  # Empty query by default
        if name_query:
            query['category'] = name_query  # Add 'name' query to the MongoDB query
        
        documents = collection.find(query)
        

        data = []
        for doc in documents:
            doc['_id'] = str(doc['_id'])
            doc['name'] = str(doc.get('name', ''))
            doc['category'] = str(doc.get('category', ''))
            doc['price'] = str(doc.get('price', ''))
            doc['description'] = str(doc.get('description', ''))
            data.append(doc)

        serializer = DocumentSerializer(data, many=True)
        return Response(serializer.data)
# POST
class ProductListPost(APIView):
    def post(self, request):
        db = client['Mart']
        collection = db['Grocery']
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = {k: v for k, v in serializer.validated_data.items() if k != '_id'}
            result = collection.insert_one(validated_data)
            inserted_id = str(result.inserted_id)
            serializer.validated_data['_id'] = inserted_id
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def default_view(request):
    # Your default view logic here
    return render(request, 'default_template.html')