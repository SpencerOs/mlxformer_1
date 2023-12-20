import random
import sentencepiece as spm

def tokenize_data(file_path, spm_model_path, output_path):
    sp = spm.SentencePieceProcessor(model_file=spm_model_path)
    tokenized_data = []

    with open(file_path, 'r', encoding='utf-8') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            tokens = sp.encode(line.strip(), out_type=int)
            outfile.write(' '.join(map(str, tokens)) + '\n')

def load_tokenized_data(file_path):
    tokenized_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            token_ids = [int(token) for token in line.strip().split()]
            tokenized_data.append(token_ids)
    return tokenized_data
    
def split_data(data, train_ratio=0.8):
    split_index = int(train_ratio * len(data))
    return data[:split_index], data[split_index:]

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


def main():
    raw_data_file = '../data/processed_wiki_dump-23.txt'
    spm_model_path = '../data/wiki_tokenizer.model'
    tokenized_file = '../data/tokenized_data.txt'
    train_file = '../data/train_data.txt'
    validation_file = '../data/validation_data.txt'

    tokenize_data(raw_data_file, spm_model_path, tokenized_file)
    tokenized_data = load_tokenized_data(tokenized_file)
    train_data, validation_data = split_data(tokenized_data)

    save_data(train_data, train_file)
    save_data(validation_data, validation_file)

if __name__ == '__main__':
    main()