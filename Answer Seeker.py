# pandas as pd is already imported


df = pd.read_csv("./answers.csv")

# Write your code below
df['num_words'] = df['value'].str.split(' ').str.len()
df['num_exclamation'] = df['value'].str.count('!')
df['num_question'] = df['value'].str.count(r'\?')
df['num_dot'] = df['value'].str.count(r'\.')
df['num_symbols'] = df['num_exclamation'] + df['num_question'] + df['num_dot']
df['upper_chars'] = df['value'].str.count(r'[A-Z]')
