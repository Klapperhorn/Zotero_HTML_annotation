import pandas as pd

#https://github.com/rehanraza24/Twitter-Text-Sentiment-Analysis-/blob/main/Text%20Preprocessing%20using%20SPACY.ipynb


# Contaction to Expansion > can't TO can not ,you'll TO you will
contractions = { 
"ain't": "am not / are not / is not / has not / have not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is / how does",
"i'd": "I had / I would",
"i'd've": "I would have",
"i'll": "I shall / I will",
"i'll've": "I shall have / I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}





def WordlistFilter(Lemmata, by):
    x=False
    
    if type(Lemmata)!=list:
        Lemmata=Lemmata.split()
        
    # As soon as the function finds a Word from the word list, x turns to True
    if len(Lemmata)>0:
        for i in Lemmata:
            if type(i)==str:
                if i.lower() in by:
                    x= True
    return x
    


def filter_paragraphs(p_list, by="ai, chatGPT"):
    
    if type(by)==str:
        by=by.split(",")
    by=[i.strip().lower() for i in by]
    
    if type(p_list)==str:
        p_list=[p_list]
 
    
    if p_list!=None:
        AI_Content=[]
        for text in p_list:
            AI_Content_Binary=WordlistFilter(text, by)
            if AI_Content_Binary==True:
                AI_Content.append(text)
        return AI_Content


def cont_to_exp(x):
    if type(x) is str:
        for key in contractions:
            value = contractions[key]
            x = x.replace(key, value)
        return x
    else:
        return x


def TweetCleaner(text):
    import preprocessor as p
    import re
    
    text=" ".join([word for word in text.split() if word[0]!="@" if word[:4]!="http"])
    text=text.replace("&amp","&")
    text=text.lstrip("RT ")
    text=re.sub(r'https?://[^\s<>"]+|www\.[^\s<>"]+','', text) # remove websites
    
    # https://github.com/s/preprocessor
    text=p.clean(text)

    return text

def pureText(text):
    import re
    text=text.lower()
    text=cont_to_exp(text)
    text=re.sub('[^A-Z a-z 0-9äöüÄÖÜß]+','', text) # Remove all Punctiations or Special Charactors 
    return text


def Tokenizer(text,nlp):
    if type(text)!=str:
        return
    NLP= nlp(text)
    tokens=[token.lemma_ for token in NLP if token.is_alpha==True]
    #NoStopwords=[token.lemma_ for token in NLP if token.is_stop==False and token.is_alpha==True]
    return  tokens


def NoStopwords(text,nlp):
    if type(text)!=str:
        return
    NLP= nlp(text)
    #tokens=[token.lemma_ for token in NLP if token.is_alpha==True]
    NoStopwords=[token.lemma_ for token in NLP if token.is_stop==False and token.is_alpha==True]
    return  NoStopwords

def Sentiment(text,nlp):
    try:
        if type(text)!=str:
            return
        doc = nlp(text)
        polarity=doc._.blob.polarity

        subjectivity=doc._.blob.subjectivity
        print(polarity,subjectivity)
    except:
        print("sentiment not working", end=".")
            
        polarity=0
        subjectivity=0
        
    return pd.Series([polarity, subjectivity])

    

def langDetect(language,text):
    
    if language not in [None,""]:
        return language
    
    #from spacytextblob.spacytextblob import SpacyTextBlob
    else:
        try:
            from langdetect import detect
            language=detect(text)
        except:
            language="no_language_features"

        return language



def GoogleTrans(text,source_language, target_language):
    
    # first check if source==target --> return without translation!
    if type(text)==str and source_language!=target_language:
        
        from deep_translator import GoogleTranslator
        try:

            ### language detection problems (mixing de, it & nl) --> therefore always NL!
            if source_language!="es": ## only spanish detection works.
                source_language="nl"
            
            result = GoogleTranslator(source=source_language, target=target_language).translate(text) # or source="nl"
            print(result[:4],end=". ")
        except:
            print("problem with: ", text)
        return text
    else:
        return text


def current_time():
    from datetime import datetime
    print("Current Time =", datetime.now().strftime("%H:%M:%S"))
    return


def load_nlp(target_language="en"):
    import spacy
    if target_language=="en":
        nlp = spacy.load('en_core_web_sm')
        
    if target_language=="de":
        spacy.cli.download("de_core_news_sm")
        nlp = spacy.load("de_core_news_sm")   
    return nlp

def NLP_Pipeline(df, text_column="text", target_language=None, sentiment=False):
    current_time()
    
    
    print("Lenght: ", len(df))
    df["text_clean"]=df[text_column].apply(TweetCleaner)
    
    print("cleaning done.")
    
    df["letters_count"]=df["text_clean"].apply(lambda x: len(x))
    df["word_count"]=df["text_clean"].apply(lambda x: len(x.split()))
    
    current_time()
    print("next: language.")

    
    if target_language!=None:
        if "language" not in df.columns:
            df["language"]=None
            
    # only language detect if there is no language.
         
        df["source_language"]=df.apply(lambda x: langDetect(x["language"],x["text_clean"]),axis=1)
        df.drop(columns=["language"],inplace=True)
        print("language detection done.")
        current_time()
                        
                                     
        print("Next: Translating...")
        df["text_clean"]=df.apply(lambda x: GoogleTrans(x[text_column],x["source_language"],target_language),axis=1)
        df["text_clean"]=df["text_clean"].apply(TweetCleaner)
        current_time()
    
    df["pure_text"]=df.text_clean.apply(pureText)
    
    print("pure english text done. Next: Token & Lemmatizing.")
    current_time()
    
                                     
    nlp=load_nlp(target_language)
                      
    df["Lemmata"]=df.pure_text.apply(Tokenizer, nlp=nlp)                                
    print("Token & Lemmatizing done. Next: Remove Stopwords.")
                                     
    df["NoStopwords"]=df.pure_text.apply(NoStopwords, nlp=nlp)
    current_time()
    
    if sentiment==True:
        print("Stopwording done. Next: sentiment.")
                                     
        df[["polarity","subjectivity"]]=df.text_clean.apply(Sentiment, nlp=nlp)
        current_time()
    
    return df


