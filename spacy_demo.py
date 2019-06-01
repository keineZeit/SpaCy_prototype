import spacy

nlp = spacy.load("en_core_web_sm")

sents = ''
with open('./data/bailii_test_case.txt') as f:
    sents += str(f.readlines())
sents = unicode(sents)

doc = nlp(sents)
result_list = []
for ent in doc.ents:
    result_list.append(ent.text + ', ' + ent.label_)
    #print(ent.text, ent.start_char, ent.end_char, ent.label_)
result_list = list(dict.fromkeys(result_list))

result_file = open('./data/bailii_test_case_result.txt', 'w+')
for sent in result_list:
    result_file.write(sent + '\n')
result_file.close()
