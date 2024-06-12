from text_preprocessing import preprocess
from run_bot import enc_full, dec, lr


def predict_lr(example):
    title_body = example
    title_body = preprocess(title_body)
    X_pred = enc_full.transform([title_body])
    return dec[lr.predict(X_pred)[0]]

def predict_rf(example):
    title_body = example
    title_body = preprocess(title_body)
    X_pred = enc_full.transform([title_body])
    return dec[lr.predict(X_pred)[0]] # тут линейная регрессия

def predict_proba(example):
    title_body = example
    title_body = preprocess(title_body)
    X_pred = enc_full.transform([title_body])
    probs = lr.predict_proba(X_pred)[0]
    return [(dec[i], probs[i]) for i in range(9)]

def format_predictions(predictions):
    predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
    formatted_predictions = [f"{category}: {probability:.2f}" for category, probability in predictions]
    return ',\n'.join(formatted_predictions)

def predict(example):
    title_body = example
    title_body = preprocess(title_body)
    X_pred = enc_full.transform([title_body])
    return dec[lr.predict(X_pred)[0]]