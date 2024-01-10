from cohere import Client
from os import getenv, environ

if "CO_API_KEY" not in environ:
    raise EnvironmentError("Please include a valid Cohere API Key as the environment variable 'CO_API_KEY'.")

api_key = getenv("CO_API_KEY")
print(api_key)
co_bot = Client(api_key=api_key)
# co_bot = Client()

def get_response_text(model: str, message: str):
    response = co_bot.generate(
        model=model,
        prompt=message,
    )
    return response.text

mdl = "command"
msg = "Where do the tallest penguins live?"

print(get_response_text(mdl, msg))
