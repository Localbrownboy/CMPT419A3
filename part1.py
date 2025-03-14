import polars as pl
import tiktoken
import random

# load data 
# this is a dataset of mathematical questions and solutions
df = pl.read_ndjson("data/train.jsonl")

# set up tokenizer 
tokenizer = tiktoken.encoding_for_model("gpt-4")  
max_tokens = 300_000  
current_token_count = 0
selected_rows = []

while current_token_count < max_tokens:
    # take sample 
    sampled_row = df.sample(n=1).to_dicts()[0]
    
    # get question and answer column 
    question = sampled_row["question"]  
    answer = sampled_row["generated_solution"]

    # tokenize and get length of tokens from question and answer 
    q_tokens = tokenizer.encode(question)
    a_tokens = tokenizer.encode(answer)
    token_count = len(q_tokens) + len(a_tokens)
    
    if current_token_count + token_count > max_tokens:
        break  # stop adding if we are hitting max 
    
    # add rows to the storage and increment count 
    selected_rows.append(sampled_row)
    current_token_count += token_count

# çreate df with the selectd rows / tuples 
result_df = pl.DataFrame(selected_rows)

print(len(result_df))


# only run the below to generate the sample for p3 --->> DONT RUN IT NOW THAT I"VE FILLED IN THE QA 
# result_df = result_df.with_columns(pl.lit(None).alias("quality_assessment"))
# sampled_df = result_df.sample(10)

# sampled_df.write_json("LLM_data_sample_10.json")