from rest_framework import generics, mixins, permissions

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductMixinAPIView(
    # generics.GenericAPIView, 
    # mixins.ListModelMixin, 
    # mixins.RetrieveModelMixin,
    # mixins.CreateModelMixin
    # ):
    # queryset = Product.objects.all()
    # serializer_class =  ProductSerializer

    # def get(self, request, *args, **kwargs):
    #     print(args, kwargs)
    #     pk = kwargs.get('pk')
    #     if pk is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    # def perform_create(self, serializer):
    #     print(serializer.validated_data)
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = "Auto generate content mixins"
    #     serializer.save(content=content)