import g4f
from g4f.Provider import Bing, RetryProvider
from g4f.client import Client
import nest_asyncio
from g4f.cookies import set_cookies

set_cookies(".bing.com", {
    "_U": "cookie value"
})
set_cookies(".google.com", {
    "__Secure-1PSID": "cookie value"
})
nest_asyncio.apply()

client = Client(
    provider=RetryProvider([
        g4f.Provider.Bing
    ])
)
chat_history = [{"role": "user", "content": 'Respond in English.'}]


def send_request(message):
    global chat_history
    chat_history.append({"role": "user", "content": message + " Add to the prompt"})

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
    except Exception as err:
        print("All providers are not responding, please try later.")
        return "Error: No response from providers."

    response_content = response.choices[0].message["content"]
    chat_history.append({"role": "assistant", "content": response_content})
    return response_content
