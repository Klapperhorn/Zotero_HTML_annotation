Key_uncertain=['suggests', 'possible', 'may', 'potentially', 'not adequately', 'should', 'will', 
'probably', 'hypothesis', 'could', 'implicate', 'perhaps', 'likely', 'might', 'perhaps', 
'possibility', 'possible', 'possibly', 'potentially', 'probably', 'seem', 'speculate', 
'whether', 'suspect', 'suppose', 'unsure', 'speculation', 'uncertainty']

Key_ignorance=['not understood', 'not been explored', 'not explored', 'not assessed' , 
'did not demonstrate', 'little is known', 'unexplored', 'unknown', 'not known', 'unclear', 
'not designed to', 'did not allow for', 'controversial', 'has not been determined', 
'have not been determined', 'incomplete', 'open question', 'not fully', 'not comprehensively', 
'not specifically', 'debated', 'contentious', 'unknown', 'further investigation', 'not intended to', 
'not planned to', 'not yield', 'not distinguish', 'not determined', 'not evaluated', 'not estimated', 
'not measured', 'not investigated', 'has not been specified', 'has not been settled', 'has not been concluded', 
'not been investigated', 'not been researched']

#hype according to the Miller et al.
hypeAdj=["experienced","important","relevant","essential","novel","senior","notable","unique",
"trained","significant","key","emphasize","exhaustive","comprehenisve","fundamental","specialized",
"excellent","unwanted","appropriate","innovative"," precise","strong","high","scarce","newer","useful",
"detailed","expert","critical","impactful","board-certified","high-volume","particular","qualified"]

hypeAdv=["very", "more", "particularly", "obviously", "well", "importantly", "even", "most highly", 
"especially", "greatly", "further", "markedly", "successfully", "much", "without question", "always", 
"objectively", "interestingly", "exactly", "specifically", "ever", "stricly", "certainly", "effectively", 
"easily", "steadily", "few", "entirely", "significantly", "unlike", "only", "all"]

hypeNoun=["strength", "importance", "robustness", "experience", "interest", "expert"]
hypeVer=["assure", "note succeed", "strengthen", "maximize", "reinforce", "empower", "highlight", "recognize"]

#manually added hype terms
hype_selection=["important","relevant","essential","novel","fundamentally","notable","unique","transformed","in a world","significant","emphasize","exhaustive","comprehenisve","fundamental","specialized",
"excellent","unwanted","innovative","impactful","particularly","importantly","most highly","especially", "greatly","markedly", "successfully","interestingly", "exactly", "certainly", "effectively","significantly","importance","assure", "note succeed","maximize", "reinforce","empower", "highlight", "recognize","disrupt","extinct"]

# However, as it is interesting :D
Key_However=["however","but", "nevertheless","even so", "nonetheless", "still","though","yet","notwithstanding"]

#Combined Hypeterms
Key_hypes=list(set(hypeAdj+hypeAdv+hypeNoun+hypeVer+hype_selection))

def keyWords():

    d={"uncertainty": Key_uncertain,"ignorance": Key_ignorance, "hype": Key_hypes, "however": Key_However} 
    return d

def hype_word(sentence,keys=Key_hypes):
    exp=[]

    for key in keys:
        if key in sentence.lower(): ## To include capitalized strings, I added .lower() in the search
            #uncertainD[key].extend([parag])
            exp.append(key)
            #print(key, sentence)
    if len(exp) >0:
        return exp


def hype_sentence(sentence,keys=Key_hypes):
    exp=[]

    for key in keys:
        if key in sentence.lower(): ## To include capitalized strings, I added .lower() in the search
            #uncertainD[key].extend([parag])
            exp.append(sentence)
            #print(key, sentence)
    exp=list(set(exp))
    if len(exp) >0:
        return exp

