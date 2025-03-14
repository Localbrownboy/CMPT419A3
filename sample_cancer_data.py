import polars as pl

# load data 
# this is a dataset of mathematical questions and solutions
df = pl.read_csv("data/breast_cancer.csv")

df = df.with_columns(pl.lit(None).alias("quality_assessment"))
df = df.sample(10)

# df.write_json("breast_cancer_sample_10.json") # DONT RUN THIS NOW PLS 