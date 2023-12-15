import sentencepiece as spm
import sys

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# SentencePice segmentation
# Last updated: 24 Oct 2022

sp_model = sys.argv[1]
input_file = open(sys.argv[2], 'r')
sp = spm.SentencePieceProcessor(model_file=sp_model)

for line in input_file:
   sp_list = sp.encode(line.strip(), out_type=str)
## Using list comprehension for print out as normal sentence
   sp_text = ' '.join([str(sp_unit) for sp_unit in sp_list])
   print(sp_text)

input_file.close()

