from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post
from .serializers import PostSerializer

@api_view(['GET'])

def hello(req):
    return Response(data="Hello world")

@api_view(['GET'])
def GetAllPosts(req):
    posts = Post.objects.all().order_by('-date')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def  getPost(req, slug):
    post = Post.objects.get(slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])

def CreatePost(req):
    data = req.data
    serializer = PostSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['POST'])

def CreatePost(req):
    data = req.data
    serializer = PostSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['PATCH'])

def UpdatePost(req):
    data = req.data
    obj = Post.objects.get(id=data["id"])
    serializer = PostSerializer(obj, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['DELETE'])

def CreatePost(req):
    data = req.data
    obj = Post.objects.get(id=data["id"])
    obj.delete()
    
    return Response({'message': "Post deleted"})