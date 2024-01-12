from openai import OpenAI


def get_completion(prompt, engine="text-davinci-003"):
    client = OpenAI()
    response = client.completions.create(model=engine, prompt=prompt, max_tokens=3000, n=1)
    return response.choices[0].text


def generate_ans(text):
    prompt = f"""

    ```{text}```

    Generate a concise and informative lean canvas based on the following problem statement and potential solution. Provide responses within the specified character limits and formats.
    make sure that you provide answer to each of these prompts on a new line

    Specific prompts:

    Problem summary: Summarize the problem in under 450 characters.
    Solution summary: Summarize the solution in under 200 characters.
    Unique value proposition: What's the unique value proposition for the provided solution? Answer in 1 sentence under 450 characters.
    Key metrics: What are the key metrics for the provided solution? Answer in paragraph form under 200 characters.
    Unfair advantages: What are some unfair advantages that other companies may have that could affect the effectiveness of the solution? Answer in paragraph form under 200 characters.
    Channels: How can one provide this solution to customers? Answer in paragraph form under 200 characters.
    Customer segments: Who are the target customers? Answer in one sentence under 450 characters.
    Cost structure: What is the cost structure for this solution? Answer in one sentence under 470 characters.
    Revenue streams: What are different types of revenue streams for this solution? Answer in paragraph form under 470 characters.

    """  # noqa: E501
    return get_completion(prompt)


def get_data(text):
    """
    Strips spacing and returns the generated answer, with indices from 0 to 9 representing
    problem_summary, solution_summary, uniq_val_prop, key_metrics,
    unfair_advtg, channels, customer_seg, cost_struct, revenue_streams.
    """
    lines = [line.strip() for line in generate_ans(text).splitlines() if line.strip()]
    return lines[:9]
