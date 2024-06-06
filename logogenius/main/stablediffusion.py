import requests
from PIL import Image, PngImagePlugin
import io
import base64
payload = {
  "cfg_scale": 15,
  "denoising_strength": 0.7,
  "width": 512,
  "height": 512,
  "prompt": "Create a logo for a company specializing in joke development. The logo should be fun and creative, reflecting the playful and witty nature of the company. Use bright colors and elements symbolizing humor and laughter, such as smiles, emoticons, or comic symbols. The logo should be modern and eye-catching, suitable for both digital and print media.",
  "steps": 1,
  "negative": "No neon colors, avoid dark or gothic themes, no realistic photos or images, no floral patterns or elements, exclude animals or mascots, no intricate or overly detailed designs, avoid cartoonish or comic styles, no harsh or vivid colors, exclude metallic or glossy effects, no use of aggressive or sharp shapes, no cluttered designs, no irrelevant text or symbols.",
  "sampler": "ddim",
  "seed": 42,
  "batch_size": 1,
  "n_iter": 1,
  "clip_guidance_scale": 1000,
  "color_palette": ["#000000", "#FFFFFF", "#FF0000"],
  "style": "minimalist"
}

response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
print(response)
r = response.json()

for i in r['images']:
  image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
  png_payload = {
    "image": "data:image/png;base64," + i
  }
  response2 = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/png-info', json=png_payload)

  pnginfo = PngImagePlugin.PngInfo()
  pnginfo.add_text("parameters", response2.json().get("info"))
  image.save('output.png', pnginfo=pnginfo)
