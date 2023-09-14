import pandas as pd

def current_time():
    
    from datetime import datetime
    print("Current Time =", datetime.now().strftime("%H:%M:%S"))
    return


#https://github.com/rehanraza24/Twitter-Text-Sentiment-Analysis-/blob/main/Text%20Preprocessing%20using%20SPACY.ipynb



def cont_to_exp(x):
    from MyLib.cont_to_exp import contractions
    if type(x) is str:
        for key in contractions:
            value = contractions[key]
            x = x.replace(key, value)
        return x
    else:
        return x


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
    if isinstance(text,str):
        text=text.lower()
        text=cont_to_exp(text)
        text=re.sub('[^A-Z a-z 0-9äöüÄÖÜß]+','', text) # Remove all Punctiations or Special Charactors 
    return text


def Tokenize(text,nlp):
    
    import pandas as pd
    if type(text)!=str:
        return pd.Series([None,None, None])  
    
    NLP= nlp(text)
    
    tokens=[token.lemma_ for token in NLP if token.is_alpha==True]
    NoStopwords=[token.lemma_ for token in NLP if token.is_stop==False and token.is_alpha==True]
    modal_verb=[token.lemma_ for token in NLP if token.tag_=="MD"]
    
    return pd.Series([tokens,NoStopwords,modal_verb])   

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



def langDetect(text,language=None):
    if language not in [None,""]:
        return language
    else:
        try:
            from langdetect import detect
            language=detect(text)
        except:
            language="no_language_features"
        if language not in ["es","en","nl"]: ## only spanish detection works (mixing de, it & nl) --> rest is NL
            #print(language, "nl", end=" - ")
            language="nl"    
        return language



def GoogleTrans(text,source_language=None, target_language="en"):
    
    if isinstance(text,list):
        print("first explode the column!")
        return None
    
    # first check if source==target (if it is english) --> return without translation!
    if isinstance(text,str) and source_language!=target_language:
        
        if source_language==None:
            source_language=langDetect(text,source_language)
        
        from deep_translator import GoogleTranslator
        
        try:                
            translator=GoogleTranslator(source=source_language, target=target_language)
            text_translated = translator.translate(text) # or source="nl"
        except:
            print("problem with: ", text)
        return pd.Series([text_translated,source_language])
    else:
        return pd.Series([text,source_language])




def load_nlp(target_language="en"):
    import spacy
    
    if target_language=="en":
        import spacy_transformers
        nlp = spacy.load("en_core_web_trf")
        #nlp = spacy.load('en_core_web_sm')
        
    if target_language=="de":
        spacy.cli.download("de_core_news_sm")
        nlp = spacy.load("de_core_news_sm")   
    return nlp



def classify_metaphors(row, column="sentences",pipe=None ,stop_words=[]):
    
    if len(stop_words)==0:
        from nltk.corpus import stopwords
        stop_words= list(set(stopwords.words('english')))
   
    if pipe==None:
        from transformers import pipeline
        pipe = pipeline("token-classification", model="CreativeLang/metaphor_detection_roberta_seq")
    
    #print(".", end=" ")
    text = row[column]
    result = pipe(text)
    metaphor_token = [i['word'].lstrip("Ġ") for i in result if i['entity'] == 'LABEL_1']
    metaphor_token = [w for w in metaphor_token if not w.lower() in stop_words]
    #no_metaphor_token = [i['word'] for i in result if i['entity'] == 'LABEL_0']
    return metaphor_token


def roberta_sentiment(row, column="sentences",pipe=None):
    
    if pipe==None:
        pipe = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest", max_length=512, truncation=True)
    
    text = row[column]
    result = pipe(text)
    sentiment=[i["label"] for i in result][0]
    return sentiment

def check_return_nan(df):
    url=df[df.sentences.isna()]["url"]
    print("nan_sentence:", url)
    df.dropna(subset="sentences",inplace=True)
    return df

def NLP_Pipeline(df, text_column="text", sentence_wise=True, language="en", sentiment=False, metaphors=False):
    from tqdm import tqdm
    tqdm.pandas()
    
    if isinstance(df[text_column],list):
        print(f"explode by {text_column}")
        df=df.explode(text_column)
  
    current_time()

    if sentence_wise==True:
        print("len: ",len(df))
        print("splitting to sentences.")
        
        from nltk.tokenize import sent_tokenize
        
        df["sentences"]=df[text_column].dropna().apply(sent_tokenize)
        df=df.explode("sentences")
        
        print("len: ",len(df))
        df['S_counter'] = df.groupby('key').cumcount()        
        df["key_S"]=df.apply(lambda x: str(x.key)+"_"+str(x.S_counter), axis=1)
    
    
    text_column="sentences"
    nlp=load_nlp(language)    
    print("Token & Lemmatizing & stopword removal & modal_word.") 
    
    df[["Lemmata","NoStopwords","modal_words"]]=df[text_column].progress_apply(Tokenize, nlp=nlp)
    
    current_time()
   
    df["pure_text"]=df[text_column].apply(pureText)
   # df["letters_count"]=df[text_column].dropna().apply(lambda x: len(x))
   # df["word_count"]=df[text_column].dropna().apply(lambda x: len(x.split()))
    
    df=check_return_nan(df)
        
    
    if sentiment==True:
        
        from transformers import pipeline
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
        sentiment_pipe = pipeline("sentiment-analysis", model=model, max_length=512, truncation=True)
        
        print("Stopwording done. Next: sentiment.")                              
        df["sentiment"] = df.progress_apply(roberta_sentiment, axis=1,column=text_column,pipe=sentiment_pipe)
        
    if metaphors==True:
        
        print("Now - metaphors.")  
        from nltk.corpus import stopwords
        stop_words= list(set(stopwords.words('english')))
        
        from transformers import pipeline
        metaphor_pipe = pipeline("token-classification", model="CreativeLang/metaphor_detection_roberta_seq")
        
        df["metaphors"] = df.progress_apply(classify_metaphors, axis=1,column=text_column,stop_words=stop_words,pipe=metaphor_pipe)
        df["metaphors_n"] = df.metaphors.apply(lambda x: len(x))
        

    return df


