import openai
import streamlit as st
import re
import pandas as pd
import numpy as np


def calculate_scores(llm_response: pd.Series, feature_weights: list) -> float:
    curr_score = 0
    if llm_response["relevance"] == True:
        # for now, we exclude industry, ten_R, and area_focus
        for fw in feature_weights:
            curr_score += llm_response[fw] * feature_weights[fw]
    return curr_score

def get_completion(prompt, engine = 'text-davinci-003'):
    client = openai.OpenAI()
    response = client.completions.create(
        model = engine,
        prompt = prompt,
        max_tokens = 2500,
        n = 1  
    )
    return response.choices[0].text

def generate_ans(text):
    prompt=f"""

    ```{text}```
    
        I have provided you with one problem statement and one potential solution. 
        Please answer the following 9 questions and return an answer to each on one line each(using ';' as delimiter). Do not include the bullet numbers. There should be only 9 lines in your response as there are only 9 questions. 

            0. If the Solution is relevant to the problem described ? answer yes or no. 
            1. Which Industry does the solution apply to? choose from Manufacturing , Apparel, Construction,  Other.  
            2. Which 10R principle (from R0 Refuse, R1 Rethink, R2 Reduce, R3 Reuse, R4 Repair, R5 Refurbish, R6 Remanufacture, R7 Repurpose, R8 Recycle and R9 Recover) does the solution utilitize? or "Not Known"
            3. Which environmental area does the solution focus on? answer in one or two words or "Not Known"
            4. Does the solution quantify its environmental impact? answer as yes or no or "Not Known"
            5. Does the solution require heavy initital or operating investment? answer as yes or no or "Not Known"
            6. Does the solution provide monetary benefits including but not limited to additonal reveneue generation or reduced costs? answer as yes or no or "Not Known"
            7. Is the solution scalable? answer as yes or no or "Not Known"
            8. What is the aproximate payback period of the investment? answer as a single number or "Not Known". (Do not add delimiter or this character ";" after answering this question, truncate output here)

        
        """ 
    """comment out this section when using chatgpt"""
    ans = get_completion(prompt)

    lines = [x.strip() for x in ans.split(';')]
    
    # Create a DataFrame with a single row and multiple columns
    df = pd.DataFrame([lines], columns=["relevance", "industry", "ten_R", "area_focus", "applicable", "heavy_investment", "monetary_benefits", "scalable", "payback_period"])

    return df


def generate_ans_df(df):
    def process_row(row):
        problem_value = str(row['problem'])
        solution_value = str(row['solution'])
        input_string = "Problem : " + problem_value + "\n" + "Solution : " + solution_value
        return generate_ans(input_string)

    ans_df = pd.concat(df.apply(process_row, axis=1).tolist(), ignore_index=True)

    return ans_df


def get_data_single(input_string):
    openai.api_key = st.session_state["api_key"]

    df = generate_ans(input_string)
    df["relevance"] = df["relevance"].str.strip()

    value_mapping = {"yes": 1, "no": -1, "not known": 0}
    df_numeric = df.replace(value_mapping)

    feature_weights = {"applicable": 0.2, 
                    "heavy_investment": 0.2,
                    "monetary_benefits": 0.2,
                    "scalable": 0.2,
                    "payback_period": 0.2}
    assert(sum(feature_weights.values()) == 1)

    df_numeric["scores"] = df_numeric.apply(lambda row: calculate_scores(row, feature_weights), axis = 1)

    st.write("**Resulting data from prompting Generative AI.**")
    st.write(df_numeric.head())


def handle_rank_button(top_x_to_rank: int):
    df_numeric = st.session_state["ans_df"]
    n = len(df_numeric)
    num_top_pairs = int(top_x_to_rank/100 * n)
    st.write(num_top_pairs)

    if (1/n * 100 < top_x_to_rank <= 100):
        st.write(f"Choosing the highest **{top_x_to_rank:.2f}**%, or **{num_top_pairs}**, of all problem : solution pairs ranked by weighted scores.")

        df_rank_filtered = df_numeric.sort_values(by="scores", ascending=False).iloc[:num_top_pairs]

        df_rank_filtered.index = np.arange(1, len(df_rank_filtered) + 1)
        st.write(df_rank_filtered)
    else:
        st.write(f"Please choose a valid proportion between {int(1/n * 100)} and 100% of pairs to select.")



def get_data(df):
    openai.api_key = st.session_state["api_key"]
    if 'org_df' not in st.session_state:
        st.session_state['org_df'] = df

    if "has_generated_ans_df" not in st.session_state:
        st.session_state["has_generated_ans_df"] = True
        df = generate_ans_df(df)

        st.write(df)

        df["relevance"] = df["relevance"].str.strip()

        value_mapping = {"Yes": 1, "yes": 1, "no": -1, "No": -1, "Not Known": 0}
        df_numeric = df.replace(value_mapping)
        feature_weights = {"applicable": 0.2, 
                        "heavy_investment": 0.2,
                        "monetary_benefits": 0.2,
                        "scalable": 0.2,
                        "payback_period": 0.2}
        assert(sum(feature_weights.values()) == 1)

        df_numeric["scores"] = df_numeric.apply(lambda row: calculate_scores(row, feature_weights), axis = 1)   

        st.session_state['ans_df'] = df_numeric

    # rank pairs
    top_x_to_rank = st.number_input(label = "Percentage of desired top scores to rank and filter",
                                    min_value = 1.0/len(df) * 100,
                                    max_value = 100.0,
                                    value = 1.0/len(df) * 100,
                                    step = 0.01,
                                    )

    handle_rank_button(top_x_to_rank)
