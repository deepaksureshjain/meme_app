from django.shortcuts import render
from django.views import View
from . models import Meme, Count
from django.http import JsonResponse
from PIL import Image
from .models import img
import json
import io
from django.core.files.images import ImageFile
import base64


# Create your views here.


class MemeApi(View):
    def get(self, request):
        memes = list(Meme.objects.values())
        if memes.__len__ != 0:
            print(type(memes), memes)
            return JsonResponse(memes, safe=False)

    def post(self, request):

        image = request.FILES
        i = (io.BytesIO(image['image'].read()))
        img = Image.open(i)
        img.show()
        return JsonResponse({"hello": "received"})
