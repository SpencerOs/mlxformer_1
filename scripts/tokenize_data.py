import sentencepiece as spm
import os

def train_tokenizer(input_file, model_prefix, vocab_size=32000):
    spm.SentencePieceTrainer.train(f'--input={input_file} --model_prefix={model_prefix} --vocab_size={vocab_size} --character_coverage=1.0')

def tokenize_text(model_file, text):
    sp = spm.SentencePieceProcessor(model_file=model_file)
    return sp.encode(text, out_type=int)

def main():
    input_file = os.path.join('..', 'data', 'processed_wiki_dump-23.txt')
    model_prefix = os.path.join('..', 'data', 'wiki_tokenizer')
    train_tokenizer(input_file, model_prefix)

    # Example usage of tokenizer
    with open(input_file, 'r', encoding='utf-8') as file:
        sample_text = file.read(1000) # Read first 1000 characters
        token_ids = tokenize_text(model_prefix+'.model', sample_text)
        print(token_ids)

if __name__ == "__main__":
    main()