import requests
from PIL import Image, PngImagePlugin
import io
import base64
from django.shortcuts import render
from django.http import JsonResponse
from .ghatgpt import send_request
from googletrans import Translator

def index(request):
    if request.method == 'POST':
        logo_restrictions = request.POST.get('logoRestrictions')
        logo_name = request.POST.get('logoName')

        # Translate the inputs to English
        translator = Translator()
        logo_restrictions_en = translator.translate(logo_restrictions, src='ru', dest='en').text
        logo_name_en = translator.translate(logo_name, src='ru', dest='en').text

        prompt_message = logo_name_en
        negative_message = f"No neon colors, avoid dark or gothic themes, no realistic photos or images, no floral patterns or elements, exclude animals or mascots, no intricate or overly detailed designs, avoid cartoonish or comic styles, no harsh or vivid colors, exclude metallic or glossy effects, no use of aggressive or sharp shapes, no cluttered designs, no irrelevant text or symbols. {logo_restrictions_en}"


        payload = {
            "cfg_scale": 15,
            "denoising_strength": 0.7,
            "width": 512,
            "height": 512,
            "prompt": prompt_message,
            "steps": 150,
            "negative": negative_message,
            "sampler": "ddim",
            "seed": 42,
            "batch_size": 1,
            "n_iter": 1,
            "clip_guidance_scale": 1000,
            "color_palette": ["#000000", "#FFFFFF", "#FF0000"],
            "style": "minimalist"
        }

        response = requests.post(url='http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
        r = response.json()

        image_data = None
        for i in r['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
            png_payload = {
                "image": "data:image/png;base64," + i
            }
            response2 = requests.post(url='http://127.0.0.1:7860/sdapi/v1/png-info', json=png_payload)
            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))
            with io.BytesIO() as output:
                image.save(output, format="PNG", pnginfo=pnginfo)
                image_data = base64.b64encode(output.getvalue()).decode()

        return JsonResponse({
            'logoRestrictions': logo_restrictions,
            'logoName': logo_name,
            'image_data': image_data
        })
    return render(request, 'index.html')
