import pandas as pd


def prepare_dataset(enc_full):
    df_source = pd.read_csv('data/final_dataset.csv')
    df_source_new = df_source[(df_source['topic'] != 'Россия') & (df_source['topic'] != 'Мир')]
    res = []
    for topic in df_source_new['topic'].unique():
        res.append(df_source_new[df_source_new['topic'] == topic].sample(100))
    df_base = pd.concat(res)
    df_base = df_base.reset_index(drop=True)
    vectors = enc_full.transform(df_base['title'] + ' ' + df_base['text']).toarray()
    return df_base, vectors
