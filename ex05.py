# #Write a script that parse sometext.txt and saves to json file word count statistics
# example:
# {
#     "on": 342,
#     "dog": 234,
#     ...
# }
import json

with open("sometext.txt", encoding="utf8") as text_file:
    text_file = text_file.read()

def count_words():
    '''split the text_file to make it list of the strings'''
    text_file_list = text_file.split()
    '''remove unnecessary characters from the beginning and the end of each string in the list'''
    json_dict = {}
    for word in text_file_list:
        if not word.isalpha():
            #print(characters_in_word)
            word = word.strip('"",”;!?.“_‘?').replace("’","'").replace("—"," ").replace("à","a")
            if word not in json_dict:
                json_dict[word]=1
            else:
                json_dict[word] += 1
        else:
            if word not in json_dict:
                json_dict[word]=1
            else:
                json_dict[word] += 1
    #open json file
    json_dict = json.dumps(json_dict, indent=1)
    with open ("word_count.json","w") as word_count:
        word_count.write(json_dict)

    return json_dict

print(count_words())