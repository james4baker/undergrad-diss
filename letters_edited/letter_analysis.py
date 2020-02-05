import os
import json
import csv

def create_file_paths():
        files = os.listdir()
        p = 0
        for x in files:
                if x == 'letter_analysis.py':
                        del files[p]
                else:
                        pass
                p+=1
        print(files)
        #print( os.listdir() )
        return files
        
def get_texts():
        pathList = create_file_paths()
        fullText = []
        for path in pathList:
                fullText += get_text(path)
        #print(fullText)
        return fullText

def get_text(path):
        fileText = []
        file = open(path, 'r');
        for line in file:
                fileText += line
        file.close()        
        return fileText

def analyse_letters(clean_text,ngram):
        n_gram_dict = {}
        i = 0
        while i < (len(clean_text)-(ngram-1)):
                new_n_gram = clean_text[i:(i+(ngram-1)+1)]
                #print(new_n_gram)
                if new_n_gram in n_gram_dict:
                        n_gram_dict[new_n_gram] += 1
                else:
                        n_gram_dict[new_n_gram] = 1
                i += 1
        return n_gram_dict

def cleaner_text(dirty_text):
        clean_text = ''
        for i in dirty_text:
                 if ord(i) >= 65 and ord(i) <= 90:
                        clean_text += i.lower()
                 elif ord(i) >= 97 and ord(i) <= 122:
                        clean_text += i
                 else:
                        pass
        print(clean_text)
        return clean_text

def save_ngram_freq_dicts(list_of_dicts):
        new_file = open('ngram_analysis.txt', 'w')
        for x in list_of_dicts:
                new_file.write( str(x) )
                new_file.write('\n')
        new_file.close()

def save_ngram_freq_csv(list_of_dicts):
        with open('ngram_analysis_csv.csv', 'w') as ngram_csv:
                for n_dict in list_of_dicts:
                        writer = csv.writer(ngram_csv)
                        writer.writerow(n_dict.keys())
                        writer.writerow(n_dict.values())
                        
def main(ngram):
        list_of_dicts = []
        print('1')
        unCleanedText = get_texts()
        print(unCleanedText)
        print('4')
        clean_text = cleaner_text(unCleanedText)
        print('5')
        n = 1
        while n < ngram+1:
                my_new_dict = analyse_letters(clean_text,n)
                #print(my_new_dict)
                list_of_dicts.append(my_new_dict)
                n+=1
        print('6')
        save_ngram_freq_csv(list_of_dicts)
        save_ngram_freq_dicts(list_of_dicts)
        
main(7)
input()
	
