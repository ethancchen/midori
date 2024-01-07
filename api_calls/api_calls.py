import openai
import streamlit as st
import re
import pandas as pd


def calculate_scores(llm_response: pd.Series, feature_weights: list) -> float:
    curr_score = 0
    if llm_response["relevance"] == True:
        # for now, exclude industry, ten_R, and area_focus
        for fw in feature_weights:
            curr_score += llm_response[fw] * feature_weights[fw]
    return curr_score

def get_completion(prompt, engine = 'text-davinci-003'):
    response = openai.Completion.create(
        engine = engine,
        prompt = prompt,
        max_tokens = 2500,
        n = 1  
    )
    return response.choices[0].text


def generate_ans(text):
    prompt=f"""
        I have provided you with one problem statement and one potential solution. 
        Please answer the following 8 questions and return an answer to each on one line each. Do not include the bullet numbers. There should be only 9 lines in your response as there are only 9 questions. 

            0. If the Solution is relevant to the problem described ? answer yes or no. 
            1. Which Industry does the solution apply to? choose from Manufacturing , Apparel, Construction,  Other.  
            2. Which 10R principle or principles from Cramer 2017 does the solution utilitize? or "Not Known"
            3. Which environmental area does the solution focus on? answer in one or two words or write N/A
            4. Does the solution quantify its environmental impact? answer as yes or no or "Not Known"
            5. Does the solution require heavy initital or operating investment? answer as yes or no or "Not Known"
            6. Does the solution provide monetary benefits including but not limited to additonal reveneue generation or reduced costs? answer as yes or no or "Not Known"
            7. Is the solution scalable? answer as yes or no or "Not Known"
            8. What is the aproximate payback period of the investment? answer as a single number or "Not Known"

        ```{text}```
        """
        

    # ans = """ Yes
    # Manufacturing
    # Reuse, Recycling
    # N/A
    # Not Known
    # Not Known
    # Not Known
    # Yes
    # Not Known"""
    ans = get_completion(prompt)
    st.write(ans)

    # Split the string into a list of lines
    lines = ans.splitlines()
    # lines = [x.strip() for x in ans.splitlines()]

    

    # Create a DataFrame with a single row and multiple columns
    df = pd.DataFrame([lines], columns=["relevance", "industry", "ten_R", "area_focus", "applicable", "heavy_investment", "monetary_benefits", "scalable", "payback_period"])

    # Print the DataFrame
    st.write(df.head())

    return df




def generate_ans_df(df):
    # st.write(df.head())
    ans_df = pd.DataFrame(columns=["relevance", "industry", "ten_R", "area_focus", "applicable", "heavy_investment", "monetary_benefits", "scalable", "payback_period"])

    # st.write(ans_df.head())

    for index, row in df.iterrows():
        problem_value = row['Problem ']
        solution_value = row['Solution']

        input_string = "Problem : " + problem_value + "\n" + "Solution : " + solution_value

        ans = generate_ans(input_string)

        # Assuming ans is a DataFrame with the same columns as ans_df
        ans_df = pd.concat([ans_df, ans], ignore_index=True)

    return ans_df





def get_data_single(input_string):

    st.write("in function")
    openai.api_key = st.session_state["api_key"]


    # st.write(input_string)

    df = generate_ans(input_string)
    st.write("raw answer")
    st.write(df)


    value_mapping = {"Yes": 1, "No": -1, "Not Known": 0}
    df_numeric = df.replace(value_mapping)
    st.write(df_numeric.head())

    feature_weights = {"applicable": 0.2, 
                    "heavy_investment": 0.2,
                    "monetary_benefits": 0.2,
                    "scalable": 0.2,
                    "payback_period": 0.2}
    assert(sum(feature_weights.values()) == 1)

    df_numeric["scores"] = df_numeric.apply(lambda row: calculate_scores(row, feature_weights), axis = 1)

    st.write("with score")
    st.write(df_numeric.head())
    

    #rank pairs
    # x = 0.25 # filter to get only top x% of ranks
    # num_top_pairs = int(x * len(df_numeric))
    # df_numeric.sort_values(by="scores", ascending=False).head(num_top_pairs).head()


def get_data(df):

    st.write("in function")
    openai.api_key = st.session_state["api_key"]


    # st.write(input_string)

    df = generate_ans_df(df)


    st.write(df)


    value_mapping = {"Yes": 1, "No": -1, "Not Known": 0}
    df_numeric = df.replace(value_mapping)
    feature_weights = {"applicable": 0.2, 
                    "heavy_investment": 0.2,
                    "monetary_benefits": 0.2,
                    "scalable": 0.2,
                    "payback_period": 0.2}
    assert(sum(feature_weights.values()) == 1)

    df_numeric["scores"] = df_numeric.apply(lambda row: calculate_scores(row, feature_weights), axis = 1)


    st.write(df_numeric.head())


    #rank pairs
    x = 0.25 # filter to get only top x% of ranks
    num_top_pairs = int(x * len(df_numeric))
    df_numeric.sort_values(by="scores", ascending=False).head(num_top_pairs).head()

    st.write(df_numeric.head())



    