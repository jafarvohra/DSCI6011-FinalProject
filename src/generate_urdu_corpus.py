import pandas as pd 
df = pd.read_csv('../UTRSet-Real/train/gt.txt', sep='\t', header=None)
df.columns = ["file_path", "digital_urdu"]
df.to_csv("/Volumes/Research/UNH/untitled folder/DSCI6011-FinalProject/data/urdu_corpus_2.csv", index=False)
df.to_excel("/Volumes/Research/UNH/untitled folder/DSCI6011-FinalProject/data/urdu_corpus_2.xlsx", index=False)