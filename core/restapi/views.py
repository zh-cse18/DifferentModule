
from rest_framework import generics
from rest_framework.response import Response

from .models import MobileInfo
from .serializers import MobileInfoSerializer
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


import logging
# from django.http import HttpResponse
#
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'console': {
#             'format': '%(name)-12s %(levelname)-8s %(message)s'
#         },
#         'file': {
#             'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#         }
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'console'
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'formatter': 'file',
#             'filename': '/tmp/debug.log'
#         }
#     },
#     'loggers': {
#         '': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'file']
#         }
#     }
# })


class MobileInfoApiView(generics.ListAPIView):
    queryset = MobileInfo.objects.all()
    serializer_class = MobileInfoSerializer


class MobileInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MobileInfo.objects.all()
    serializer_class = MobileInfoSerializer


class MobileInfoNewView(generics.ListCreateAPIView):
    queryset = MobileInfo.objects.all().order_by('-id')[:1]
    serializer_class = MobileInfoSerializer


class Mobileinfo(APIView):
    def get(self, request):
        datainfo = MobileInfo.objects.all()
        serializer = MobileInfoSerializer(datainfo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileInfoSerializer(data=request.data,many=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = MobileInfo.objects.all()
        data.delete()
        return Response(status=status.HTTP_200_OK)
   # logging.info("some message")


class Mobileinfosingle(APIView):
    def get(self, request, pid):
        data = MobileInfo.objects.get(id=pid)
        serializer = MobileInfoSerializer(data)
        return Response(serializer.data)

    def delete(self, request, pid):
        data = MobileInfo.objects.get(id=pid)
        data.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pid):
        datainfo = MobileInfo.objects.get(id=pid)
        serializer = MobileInfoSerializer(datainfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataViewSet(ModelViewSet):
    serializer_class = MobileInfoSerializer
    queryset = MobileInfo.objects.all()


