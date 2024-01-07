import openai


openai.api_key = "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"



def get_completion(prompt, engine = 'text-davinci-003'):
    response = openai.Completion.create(
        engine = engine,
        prompt = prompt,
        max_tokens = 2500,
        n = 1  
    )
    return response.choices[0].text


    input_text = """

Problem : The construction industry is indubitably one of the significant contributors to global waste, contributing approximately 1.3 billion tons of waste annually, exerting significant pressure on our landfills and natural resources. Traditional construction methods entail single-use designs that require frequent demolitions, leading to resource depletion and wastage.   
Solution : Herein, we propose an innovative approach to mitigate this problem: Modular Construction. This method embraces recycling and reuse, taking a significant stride towards a circular economy.   Modular construction involves utilizing engineered components in a manufacturing facility that are later assembled on-site. These components are designed for easy disassembling, enabling them to be reused in diverse projects, thus significantly reducing waste and conserving resources.  Not only does this method decrease construction waste by up to 90%, but it also decreases construction time by 30-50%, optimizing both environmental and financial efficiency. This reduction in time corresponds to substantial financial savings for businesses. Moreover, the modular approach allows greater flexibility, adapting to changing needs over time.  We believe, by adopting modular construction, the industry can transit from a 'take, make and dispose' model to a more sustainable 'reduce, reuse, and recycle' model, driving the industry towards a more circular and sustainable future. The feasibility of this concept is already being proven in markets around the globe, indicating its potential for scalability and real-world application.

"""

def generate_ans(text):
    prompt=f"""
        I have provided you with one problem statement and one potential solution. 
        Please answer the following 8 questions and return an answer to each on a new line.

            0. If the Solution is relevant to the problem described ? answer yes or no. 

            if the answer is yes, proceed to answwering the following qqustions.  

            1. Which Industry does the solution apply to? choose from Manufacturing , Apparel, Construction,  Other.  
            2. Which 10R principle or principles from Cramer 2017 does the solution utilitize? or "Not Known"
            3. Which environmental area does the solution focus on? answer in one or two words
            4. Does the solution quantify its environmental impact? answer as yes or no or "Not Known"
            5. Does the solution require heavy initital or operating investment? answer as yes or no or "Not Known"
            6. Does the solution provide monetary benefits including but not limited to additonal reveneue generation or reduced costs? answer as yes or no or "Not Known"
            7. Is the solution scalable? answer as yes or no or "Not Known"
            8. What is the aproximate payback period of the investment? answer as a single number or "Not Known"

        ```{text}```
        """
    ans = get_completion(prompt)

    return ans

ans = generate_ans(input_text)

print(ans)