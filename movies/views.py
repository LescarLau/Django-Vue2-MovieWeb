from django.shortcuts import render
from .models import Movie
from django.http import Http404, JsonResponse

from .serializers import MovieListSerializer,MovieDetailSerializer,MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets


# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#     # movie = Movie.objects.all().values_list()
#     # data = list(movie)
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = MovieListSerializer(movie,many=True)
#         # return JsonResponse(serializer.data,safe=False)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     # 使用POST方法来提交添加一个数据
#     elif request.method == 'POST':
#         serializer = MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 使用APIView来完成增删改查
# class MovieDetail(APIView):
#     def get(self,request,pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             raise Http404
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             raise Http404
#         serializer = MovieDetailSerializer(movie,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             raise Http404
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class MovieDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
# 使用generics中定义的方法，简化对于电影列表和详情信息的一些列增删改查的操作
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)
    
    # def put(self,request,*args,**kwargs):
    #     return self.partial_update(request,*args,**kwargs)

    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


# 通过上面对于网站接口的操作可以得出，主要是对http://127.0.0.1:8000/api/movies/的操作，使用视图集将两个类进一步简化

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

