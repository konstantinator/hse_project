with open('models/lr.pkl', 'rb') as f:
    lr = joblib.load(f)
with open('models/sw.pkl', 'rb') as f:
    stopwords_ru=joblib.load(f)
with open('models/enc_full.pkl', 'rb') as f:
    enc_full = joblib.load(f)
with open('models/dec.pkl', 'rb') as f:
    dec = joblib.load(f)