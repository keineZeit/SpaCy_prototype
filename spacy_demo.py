import spacy

nlp = spacy.load("en_core_web_sm")

sents = ''
with open('./data/bailii_test_case.txt') as f:
    sents += str(f.readlines())
sents = unicode(sents)

doc = nlp(sents)
result_file = open('./data/bailii_test_case_result.txt', 'w+')
for ent in doc.ents:
    result_file.write(ent.text + ', ' + ent.label_ + '\n')
    #print(ent.text, ent.start_char, ent.end_char, ent.label_)
result_file.close()


