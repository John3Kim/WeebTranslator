# This will allow us to translate from English to Japanese
from google.cloud import translate # Translation API
from wanakana.hiragana import is_hiragana # detects presence of hiragana
from wanakana.kanji import is_kanji # detects presence of kanji
import tinysegmenter # Tokenizes Japanese text
from pykakasi import kakasi #

# Uses the Google Translate API to retrieve the translated 
# text
def translate_text(text:str, target:str) -> str:
    translate_client = translate.Client()
    result = translate_client.translate(text,target_language=target)
    return(result['translatedText'])

# Tokenizes Japanese Text for processing
def tokenize_filter_ja(text:str) -> str:
    segment = tinysegmenter.TinySegmenter()
    # Tokenize the japanese text and filter out all instances of hiragana
    remove_hiragana = list(filter(lambda txt_filter: not(is_hiragana(txt_filter)), segment.tokenize(text)))
    lst_process = []
    #rem_kanji = list(filter(lambda txt_filter: not(is_kanji(txt_filter)), segment.tokenize(rem_hiragana)))
    for elem in remove_hiragana:
        # Enclosing them into square brackets makes google translate translate each word individually
        # Want to reduce the number of API calls to Google Translate API
        lst_process.append('[' +elem+']')

    return(' '.join(lst_process))

# This function creates a dictionary that contains 
# English words and their corresponding Japanese translation
def translation_dictionary(string_en:str, string_ja:str)-> dict:
    # take the text from two lists and then make them into a dictionary
    eng_to_ja_dict = {}
    list_vals_to_del = []

    #Convert the two lists into dictionaries
    # Gotta remove the square brackets first
    string_en = string_en.replace('[','').replace(']','')
    string_ja = string_ja.replace('[','').replace(']','')

    lst_en = string_en.split(' ')
    lst_ja = string_ja.split(' ')


    #Make sure that the lists are equal in length
    if len(lst_en) > len(lst_ja):
        length_lst = len(lst_en) - len(lst_ja)
        for i in range(length_lst):
            lst_ja.append('')

    elif len(lst_en) < len(lst_ja):
        length_lst = len(lst_ja) - len(lst_en)
        for i in range(length_lst):
            lst_en.append('')

    #Make a dictionary that will have English to Japanese translation
    for i in range(len(lst_en)):
        eng_to_ja_dict[lst_en[i]] = romanize_text(lst_ja[i])

    #Get rid of null values
    for k,v in eng_to_ja_dict.items():
        if v == '':
            list_vals_to_del.append(k)

    for i in list_vals_to_del:
        del(eng_to_ja_dict[i])

    return(eng_to_ja_dict)

def replace_en_with_ja(text_en:str, en_ja_dict:dict) -> str:
    preset_words = {"I":"watashi","you":"anata","he":"kare","she":"kanojo","we":"watashi-tachi"} 
    en_ja_dict.update(preset_words) 

    text_en_list = text_en.split(' ') 
 
    process_replacement = list(map(lambda x: en_ja_dict[x] if x in en_ja_dict.keys() else x, text_en_list))

    ret_string_process_replacement = ' '.join(process_replacement) 

    return(ret_string_process_replacement)

def romanize_text(text_ja:str) -> str:
    kkasi = kakasi()
    kkasi.setMode("H","a")
    kkasi.setMode("K","a")
    kkasi.setMode("J","a")
    kkasi.setMode("r","Hepburn")
    kkasi.setMode("s", True)
    kkasi.setMode("C", True)
    convert_char = kkasi.getConverter()
    return(convert_char.do(text_ja).lower().replace(' ',''))

def run(text:str)-> str:
    #original_eng_text = text
    ja_text = tokenize_filter_ja(translate_text(text,"ja"))
    en_text = translate_text(ja_text,"en").lower()
    make_dic = translation_dictionary(en_text,ja_text)
    return replace_en_with_ja(text, make_dic)

#print(run("Give me some good takoyaki"))
#translate("Hello","ja")
#replace_en_with_ja("I love you", dic) 
