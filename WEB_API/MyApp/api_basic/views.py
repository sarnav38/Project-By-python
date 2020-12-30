from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



#1. Create your views here.
# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Article.objects.all()
#         serializer = ArticleSerializers(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializers(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializers(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

#  or

# 4. View set
# class ArticleViewSet(viewsets.ViewSet):
   # def list(self,request):
   #     articles = Article.objects.all()
   #     serializers = ArticleSerializers(articles,many=True)
   #     return Response(serializers.data)
   #
   # def create(self, request):
   #     serializer = ArticleSerializers(data=request.data)
   #
   #     if serializer.is_valid():
   #         serializer.save()
   #         return Response(serializer.data,status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   #
   # def retrieve(self, request, pk=None):
   #     queryset = Article.objects.all()
   #     user = get_object_or_404(queryset, pk=pk)
   #     serializer = ArticleSerializers(user)
   #     return Response(serializer.data)
   #
   # def update(self,request,pk=None):
   #     articles = Article.objects.all()
   #     serializer = ArticleSerializers(data=request.data)
   #     if serializer.is_valid():
   #         serializer.save()
   #         return Response(serializer.data)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   # or use generic viewset
# class ArticleViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()
# or use modelviewset
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()

# 3. Generic view and use of authentication for android use token authentication
class GenericAPIView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Article.objects.all()

    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication,BasicAuthentication]  # cannot see get req without login
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializers

    def get(self, request,id =None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self,request,id = None):
        return self.update(request,id)

    def delete(self,request):
        return self.destroy(request,id)




# 2. // Class based views
class ArticleAPIView(APIView):

    def get(self, request, format=None):
        snippets = Article.objects.all()
        serializer = ArticleSerializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


