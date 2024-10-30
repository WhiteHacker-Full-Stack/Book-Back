from .serializers import BookSerializer
from .models import Book
from rest_framework import generics

class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPI(generics.RetrieveAPIView):
    # lookup_field = "id"
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPI(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteAPI(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer