def getLinksfromPDF(page):
    links=[]
    if '/Annots' in page.keys():
        annotations=page['/Annots']
        for a in annotations:
            a=a.get_object()
            if '/A' in a:
                A=a['/A']
                if '/URI' in A.keys():
                    link=(A['/URI'])
                    links.append(link)
    return links

def getDate(pdf_reader):
    import pandas as pd
    mod_date=None
    metaData=pdf_reader.metadata
    if '/ModDate' in metaData.keys():
        #print(metaData.keys())
        mod_date=metaData['/ModDate'][2:10]
        dtformat = "%Y%m%d"
        mod_date=pd.to_datetime(mod_date,format=dtformat)
        #print(creation_date)
    return mod_date



def attach_single_letters(text):
    import re  
    # existing problem: when a pdf has different fonts, the white space is sometimes not identified correctly and words are wrongly split, like "experienc e" --> therefore remove this whitespace but not when there is a or I (single-letter-words). However - it is unclear if the letter is correctly attached to the foregoing or next word...
    
    #in English there are single letter words: a & I. Begin of sentence A house --> relevant characters are [^aAI]. But the problem is notsolved for double letter words.. therefore it is remained... --> actio ns will stay the way
    
    text=re.sub("(?<=\s[^aAI]) (?=[^aAI]\s)","",text) # 1. merge single letters that are not a or I ( to connect o f )
    text=re.sub("(?<=\w\w) (?=[^aAI]\W)(?!\w\w)","",text) # word followed by a single letter that is not a or I and not followed by a word.
    text=re.sub("(?<=\W[^aAI\.]) (?=\w\w)","", text) # Spacer after a single letter that is not a or I or . and followed by a word.
    
    return text

def End_of_line_improve(text):
    import re  
    # remove new space characters - but leave it together if followed by bulletpoints that are converted to "-".
    text=re.sub("[\u2022\u2023\u25E6\u2219\u2043●] ","- ",text)
    text=re.sub("\n(?!\-)"," ",text)
    
    text=attach_single_letters(text)
    
    text=re.sub("(?<=[a-z](\.|\?|\!|\)))(?=[A-Z])"," ",text)     #insert space when: "small-letter DOT capital-letter" (this leaves e.g. A.I. as it is but adds space when needed from line-break)
    text=re.sub("\.{4,} \d*", " ", text) #remove the "...." + pagenumner" from table of contents. 
    text=re.sub("\s+", " ", text) #remove double Space
    
    
    text=text.strip()
    return text
    
def extract_text_with_pyPDF(filepath,MaxPages=20):
    import pandas as pd
    import re
    
    
    if filepath.endswith(".pdf") ==False:
        pages,links,mod_date=[],[],[]
        
        return pd.Series([pages,links,mod_date])
    
    pages,links,mod_date=[],[],None
    from pypdf import PdfReader
    
    
    pdf_reader = PdfReader(filepath)
    mod_date=getDate(pdf_reader)
    
    S_pages=pdf_reader.pages

    
    if len(S_pages)>MaxPages:
        f=filepath.split("\\")[-1]
        #print(f"{f} has more than {MaxPages} pages: {len(S_pages)}. Only processing {MaxPages} pages.")
        S_pages=S_pages[:MaxPages]
    
          
    for i, page in enumerate(S_pages):
        raw_text = ""
        try:
            text = page.extract_text()
            if text:
          
                text=End_of_line_improve(text)
                raw_text += text
                pages.append(raw_text)
        except Exception as error:
            print("text-problems with: ", filepath)
            print("\n", error)
            
    for i, page in enumerate(S_pages):
        links=getLinksfromPDF(page)

    return pd.Series([pages,links,mod_date])
