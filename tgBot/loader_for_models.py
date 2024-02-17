import joblib

def load_models():
    lr = joblib.load('models/lr.pkl')
    stopwords_ru = joblib.load('models/sw.pkl')
    enc_full = joblib.load('models/enc_full.pkl')
    dec = joblib.load('models/dec.pkl')
    return lr, stopwords_ru, enc_full, dec