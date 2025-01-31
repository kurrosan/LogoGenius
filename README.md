### Service for Creating Logos and Advertising Materials Using the Stochastic Method of Stable Diffusion and Large Language Models

[About the Project](#about-the-project) | [Code Execution](#code-execution) | [Sample Song Text](#sample-song-text) | [How the Code Works](#how-the-code-works) | [Program Results](#program-results)

---

## About the Project<a id="about-the-project"></a>
In today's world, visual content plays a crucial role in marketing and branding. High-quality logos and advertising materials are essential components of any successful marketing strategy. However, the creation process often requires significant time, financial investment, and the expertise of professional designers, making it inaccessible to many, particularly small and medium-sized businesses.

This project presents a web application developed with Django, utilizing various libraries to streamline several tasks, including image processing, HTTP requests, and text translation. The primary functionalities of the application include:

- **Image Uploading and Processing:**
  1. Uploading images from specified URLs using the requests library.
  2. Processing and saving images using the Pillow library.
  3. Encoding images in base64 format for seamless data exchange via JSON.

- **Web Interface:**
  1. Built on Django, featuring functionalities for handling HTTP requests and rendering HTML templates.
  2. Implementation of an API to provide JSON responses containing translated text and encoded images.

## Code Execution<a id="code-execution"></a>
**Key Libraries:**
- **requests:** For HTTP requests.
- **Pillow (PIL):** For image processing.
- **base64:** For encoding images.
- **Django:** Web framework for application development.

**Installation:**
```bash
pip install requests pillow django
pip install flask
pip install g4f -U --quiet browser-cookie3 --quiet aiohttp_socks --quiet nest-asyncio
pip install gp4
```

## How the Code Works<a id="how-the-code-works"></a>
**Main Steps:**
1. **Image Uploading:**
   - Utilizes the requests library to download images from specified URLs.
   - Opens images with Pillow, converting them into image objects.

2. **Image Processing:**
   - Saves downloaded images locally in PNG format.
   - Reads and encodes saved images in base64 for further use.

3. **Prompt Processing:**
   - Handles user requests using ChatGPT and translates them into English.

4. **Returning JSON Response:**
   - Generates a JSON response containing translated text and base64-encoded images.
   - Sends the response to clients using JsonResponse from Django.

![Image](https://github.com/kurrosan/LogoGenius/assets/120035199/ba7e3144-4524-4961-b78b-99fac446e0eb)
## Program Results<a id="program-results"></a>
![image](https://github.com/kurrosan/LogoGenius/assets/120035199/89c08568-6d3a-44dd-9971-13a6daf94f29)
![image](https://github.com/kurrosan/LogoGenius/assets/120035199/dc9ff013-c436-4994-a294-c88b88a0c258)



---
