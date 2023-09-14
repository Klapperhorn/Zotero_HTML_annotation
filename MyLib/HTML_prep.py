
def find_date(url, date):
    import pandas as pd
    from htmldate import find_date
    from numpy import nan
    if type(date)!=pd.Timestamp:
        try:
            date=pd.to_datetime(find_date(url))
        except:
            date=nan
    return date

def extract_Image_from_Html(img,target_folder="images",filename="test"):

    filetypes=["png","jpg","jpeg","pdf","svg"]
    
    if img[:4]=="data":
        
        filetype,img=img.split(",",1)
        filetype=filetype.split(";")
        filetype=filetype[0].replace("data:image/","").replace("svg+xml","svg")
        if filetype in filetypes:
            print(filetype)                
            import base64
            img=base64.b64decode(img)
            print(filename)
            with open(f"{target_folder}/{filename}.{filetype}", "wb") as fh:
                fh.write(img)
                
            print("image generated.")
        else:
            print(filetype)
        return 
    


def removeIMGs(Content,write_img=False, targetFolder="images",IMG_filename="test"):
    tags=Content.findAll('img')
    
    for count, match in enumerate(tags):
        try:
            img=match["src"]
            filename=IMG_filename+"_"+str(count)
        
            if write_img==True:
                extract_Image_from_Html(img,target_folder=targetFolder,filename=filename) 
        
            match['src']=f'deleted: {filename}'
        except:
            match=" <img deleted /> "
       # print(f"image removed: {filename}")
    
    return Content



def open_html_file(FilePath):
     if FilePath.endswith(".html"):  
        try:
            with open(FilePath,"r", encoding='utf-8') as f:
                text= f.read()
                return text
        except:
            print("error opening the html file. File does not exist?")
            return
       
    

def remove_cookiebanner(soup):
    # removie cookie shit (from surf):
    import re
    for div in soup("div", {"class" : re.compile("cookie\w*")}):
        div.decompose()
    for div in soup("div", {"aria-label" : re.compile("cookie\w*")}):
        div.decompose()        
    return soup
        
        
def return_content_soup(text):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, "html5lib") #'html.parser')
    
    soup= remove_cookiebanner(soup)
    
    Title=soup.title.text
    TextIndicators=soup("p")+soup("h5")+soup("h4")+soup("h3")+soup("h2")+soup("h1")
    All_divs=[p.parent for p in TextIndicators if p.parent.name in ["div","main","section","article","center","td"]]
    All_divs=list(dict.fromkeys(All_divs))
    
    try:
        IMG_filename="".join(x for x in Title.strip().replace(" ","_") if x.isalnum() or x=="_")[:100]
        All_divs=[removeIMGs(div,write_img=False,IMG_filename=IMG_filename) for div in All_divs]        
    except:
        print(f"error removing images: {FilePath}")
    
    return All_divs, Title

def get_HTML_elements_from_soup(All_divs):
    h1,h2,h3,linkName,linkUrl=[],[],[],[],[]
    for div in All_divs:
        if div("h1")!=None:
            h1+=[i.text for j in div("h1") for i in j]
        if div("h2")!=None:
            h2+=[i.text for j in div("h3") for i in j]
        if div("h3")!=None:
            h3+=[i.text for j in div("h3") for i in j]
        if div("a")!=None:
            linkName+=[i.text for j in div("a") for i in j]
            linkUrl+=[i.get('href') for i in div("a")]
    return h1,h2,h3,linkName,linkUrl




def End_of_line_improve(text):
    import re  
    # remove new line characters - but leave it together if followed by bulletpoints that are converted to "-".
    text=re.sub("[\u2022\u2023\u25E6\u2219\u2043●]","- ",text)
    text=re.sub("\n(?!\-)"," ",text)
    
    # no single letter attaching for HTML. only for pdf
    
    text=re.sub("(?<=[a-z](\.|\?|\!|\)))(?=[A-Z])"," ",text)     #insert space when: "small-letter DOT capital-letter" (this leaves e.g. A.I. as it is but adds space when needed from line-break)
    text=re.sub("\.{4,} \d*", " ", text) #remove the "...." + pagenumner" from table of contents. 
    text=re.sub("\s+", " ", text) #remove double Space
    
    
    text=text.strip()
    return text

def get_text_from_soup_simple_split(All_divs):
    all_text=[]

    for i in All_divs:
        # get text from each div container
        text=i.get_text(separator=u' ')
        #leave out words longer than 100 characters to avoid undetected embedded images and other shit.
        if text!=None:
            text=" ".join([y.replace("\n"," ").strip() for y in text.split(" ") if len(y)<100])
            all_text+=[End_of_line_improve(text)]
    return all_text

def get_text_from_soup_with_nltk(All_divs):
    from nltk.tokenize import sent_tokenize
    all_text=[]
    
    for paragraph in All_divs:
        paragraph_out=""
        # get text from each div container
        text=paragraph.get_text(separator=u' ')
        
        if text!=None:
            #leave out words longer than 100 characters to avoid undetected embedded images and other shit.
            text=" ".join([y for y in text.split(" ") if len(y)<100])
            
            text=End_of_line_improve(text)
            
            # dont know if this is needed.
            paragraph_out=" ".join(sent_tokenize(text)) # sentences in paragraph
            
            #this keeps divs == paragraphs together
        all_text.append(paragraph_out)
    return all_text


def get_text_from_html(text):
    try:
        text=" ".join([y for y in i.split(" ") if len(y)<100]) # remove words longer than 1000 char to avoid images.
        text=End_of_line_improve(text)              
        text=sent_tokenize(text)
        
        print("--> text from reading as a text file.")
        return text
    except:
        print("also no text from html file")
        return []




###OLD: 

def FileInfo(FilePath):
    import pandas as pd
    Title,h1,h2,h3,text,linkName,linkUrl=None,None,None,None,None,None,None

    if FilePath.endswith(".html"):
           
        try:
            #print(FilePath)

            with open(FilePath,"r", encoding='utf-8') as f:
                text= f.read()
            
        except:
            print("error opening the html file. File does not exist?")
            return
        
        
        try:
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(text, "html5lib") #'html.parser')       
            Title=soup.title.text
            #soup=HTML_prep.removeIMGs(soup,IMG_filename=Title.replace(" ","_"))
            
            TextIndicators=soup("p")+soup("h5")+soup("h4")+soup("h3")+soup("h2")+soup("h1")

            All_divs=[p.parent for p in TextIndicators if p.parent.name in ["div","main","section","article","center","td"]]
     
            All_divs=list(dict.fromkeys(All_divs))
            
            
            # Remove images
            try:
                IMG_filename="".join(x for x in Title.strip().replace(" ","_") if x.isalnum() or x=="_")[:100]
                All_divs=[removeIMGs(div,write_img=False,IMG_filename=IMG_filename) for div in All_divs]        
            except:
                print(f"error removing images: {FilePath}")
                
            h1=[item for sublist in [[i.text for i in div("h1")] for div in All_divs if div("h1")!=None] for item in sublist]
            h2=[item for sublist in [[i.text for i in div("h2")] for div in All_divs if div("h2")!=None] for item in sublist]
            h3=[item for sublist in [[i.text for i in div("h3")] for div in All_divs if div("h3")!=None] for item in sublist]

            # here only get all divs
            #text=[item for sublist in [[i.text for i in div("p")] for div in All_divs if div("p")!=None] for item in sublist]
            
            # here gets all human readable text parts --> includes headlines. the \n \n keeps distance to headlines
           
            linkName=[item for sublist in [[i.text for i in div("a")] for div in All_divs if div("a")!=None] for item in sublist]
            linkUrl=[item for sublist in [[i.get('href') for i in div("a")] for div in All_divs if div("a")!=None] for item in sublist]
            #i=i("p")+i("h5")+i("h4")+i("h3")+i("h2")+i("h1")
            text=[i.get_text(separator=u' ').replace(".",". ").replace("\n ",". ") for i in All_divs if i.get_text()!=None]

        except:
            print(f"error with: {FilePath}", end=". ")
            
            try:
                text=text.split("\n\n")
 
                print("--> text from reading as a text file.")
            except:
                print("also no text file")
                
        #leave out words longer than 100 characters to avoid undetected embedded images and other shit.
        text=[" ".join([y.replace("\n"," ").strip() for y in i.split(" ") if len(y)<100]) for i in text] 
       # text=["".join([y for y in i if len(y)<100]) for i in text]
    
    return pd.Series([Title,h1,h2,h3,text,linkName,linkUrl])
        