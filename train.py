from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)

import pandas as pd
from sklearn.model_selection import train_test_split
import torch

# ---------------- LOAD DATA ----------------

df = pd.read_csv("training_data.csv")

# Convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

print(df.head())

# ---------------- TRAIN TEST SPLIT ----------------

train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['text'],
    df['label'],
    test_size=0.2,
    random_state=42
)

# ---------------- TOKENIZER ----------------

tokenizer = DistilBertTokenizer.from_pretrained(
    'distilbert-base-uncased'
)

train_encodings = tokenizer(
    list(train_texts),
    truncation=True,
    padding=True
)

val_encodings = tokenizer(
    list(val_texts),
    truncation=True,
    padding=True
)

# ---------------- DATASET CLASS ----------------

class SpamDataset(torch.utils.data.Dataset):

    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):

        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }

        item['labels'] = torch.tensor(self.labels[idx])

        return item

    def __len__(self):
        return len(self.labels)

# ---------------- CREATE DATASETS ----------------

train_dataset = SpamDataset(
    train_encodings,
    list(train_labels)
)

val_dataset = SpamDataset(
    val_encodings,
    list(val_labels)
)

# ---------------- LOAD MODEL ----------------

model = DistilBertForSequenceClassification.from_pretrained(
    'distilbert-base-uncased',
    num_labels=2
)
# ---------------- TRAINING ARGUMENTS ----------------

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=10,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=5
)

# ---------------- TRAINER ----------------

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# ---------------- TRAIN ----------------

trainer.train()

# ---------------- SAVE MODEL ----------------

model.save_pretrained("./spam_model")
tokenizer.save_pretrained("./spam_model")

print("Model retrained and saved successfully.")