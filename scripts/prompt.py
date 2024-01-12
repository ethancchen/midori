# import openai
# from os import environ, getenv

from openai import OpenAI

# if "OPENAI_API_KEY" not in environ:
#     raise EnvironmentError("Please include a valid OpenAI API Key as the environment variable 'OPENAI_API_KEY'.")
#
# openai.api_key = getenv("OPENAI_API_KEY")


def get_response(prompt="hi", engine="text-davinci-003"):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",  # noqa: E501
            },
            {
                "role": "user",
                "content": "Compose a poem that explains the concept of recursion in programming.",
            },
        ],
    )

    return completion.choices[0].message


get_response()
