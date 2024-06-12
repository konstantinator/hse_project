import torch
import torch.nn as nn
import spacy
import fasttext

# Загрузка модели spacy и FastText
nlp = spacy.load("ru_core_news_sm")
ft = fasttext.load_model('models/cc.ru.300.bin')


class LSTMClassifier(nn.Module):
    def __init__(self, embedding_dim, hidden_dim, output_dim, n_layers, bidirectional, dropout):
        super().__init__()

        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=n_layers,
                            bidirectional=bidirectional, dropout=dropout, batch_first=True)
        self.fc = nn.Linear(hidden_dim * 2 if bidirectional else hidden_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, text, text_lengths):
        packed_embedded = nn.utils.rnn.pack_padded_sequence(text, text_lengths.cpu(), batch_first=True,
                                                            enforce_sorted=False)
        packed_output, (hidden, cell) = self.lstm(packed_embedded)
        output, output_lengths = nn.utils.rnn.pad_packed_sequence(packed_output, batch_first=True)

        if self.lstm.bidirectional:
            hidden = self.dropout(torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1))
        else:
            hidden = self.dropout(hidden[-1, :, :])

        return self.fc(hidden)  # Возвращаем логиты для каждого класса


# Загрузка обученной модели
model_path = 'lstm_model.pth'
model = LSTMClassifier(embedding_dim=300, hidden_dim=256, output_dim=9, n_layers=2, bidirectional=True, dropout=0.5)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()


def tokenize_and_transform(text):
    tokens = [token.text for token in nlp(text)]
    vectors = [torch.tensor(ft.get_word_vector(token)) for token in tokens]
    return torch.stack(vectors)


def classify_text_lstm(text):
    # Токенизация и преобразование векторов
    tokens = tokenize_and_transform(text)
    lengths = torch.tensor([len(tokens)])
    tokens = tokens.unsqueeze(0)

    with torch.no_grad():
        predictions = model(tokens, lengths)
        _, predicted_label = torch.max(predictions, 1)

    return predicted_label.item()