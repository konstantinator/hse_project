df_source = pd.read_csv('final_dataset.csv' )
df_source_new = df_source[(df_source['topic']!='Россия') & (df_source['topic']!='Мир')]
res = []
for topic in df_source_new['topic'].unique():
    res.append(df_source_new[df_source_new['topic']==topic].sample(100))
df_base = pd.concat(res)
df_base = df_base.reset_index(drop=True)
vectors = enc_full.transform(df_base['title'] + ' ' + df_base['text']).toarray()

def get_sim_text(example):
    simili = cosine_similarity(vectors, enc_full.transform([example]).toarray())
    arg = simili.argmax()
    samp = df_base.iloc[arg,:]
    return f'Title: {samp.title} \n Body: {samp.text} \n class: {samp.topic}'

patterns = r'[^a-zA-Zа-яА-Я0-9ёЁ]'
morph = MorphAnalyzer()

def preprocess(text):
    return ' '.join([morph.normal_forms(i)[0] for i in re.sub(patterns, ' ', text.lower()).split() if i not in stopwords_ru])

def predict(example):
    title_body = example
    title_body = preprocess(title_body)
    X_pred = enc_full.transform([title_body])
    return dec[lr.predict(X_pred)[0]]