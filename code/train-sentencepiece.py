import sentencepiece as spm

spm.SentencePieceTrainer.train(input='segment-corpus.txt', model_prefix='kh-segment.model', vocab_size=1000, user_defined_symbols=['foo', 'bar'])
