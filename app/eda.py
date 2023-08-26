import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('abalone.csv')
    df.columns = df.columns.str.lower()
    df['sex'] = df['sex'].replace({'f': 'F'})
    df['age'] = df['rings'] + 1.5
    for c in ['diameter', 'whole weight', 'shell weight']:
        df[c] = df[c].fillna(df[c].median())
    df.to_csv('df.csv', index=False)

