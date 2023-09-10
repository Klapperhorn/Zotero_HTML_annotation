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
hype_words=["important","relevant","essential","novel","fundamentally","notable","unique","transformed","in a world","significant","emphasize","exhaustive","comprehenisve","fundamental","specialized",
"excellent","unwanted","innovative","impactful","particularly","importantly","most highly","especially", "greatly","markedly", "successfully","interestingly", "exactly", "certainly", "effectively","significantly","importance","assure", "note succeed","maximize","empower", "highlight", "recognize","disrupt","extinct, futurist, disrupt", "happy", "diligent", "careful", "envious","reshape"]

Key_hypes=list(set(hypeAdj+hypeAdv+hypeNoun+hypeVer+hype_words))


# modal words from Ann Mische
predictive="can", "could", "may", "might", "will", "would"

imperative="have to", "let", "must", "need", "ought", "should"

subjunctive="aim", "ask for", "believe", "doubt", "expect", "fear", "hope", "urge", "want", "wish", "would like to"

modal_words=list(set(predictive+imperative+subjunctive))

ChatGPT_Terms="ChatGPT3, ChatGPT, OpenAI, Chat-GPT, conversational AI, chat interface, virtual assistant, human-computer, GPT3, GPT-3, GPT4, GPT-4, GPT-2, GPT2, GPT, Chatbot, chat-bot"
AI_Terms="AI, A.I., coginitive computing, self-learning, supervised learning, explainable AI, algorithmic, AI ethics, facial recognition, recommender system, autonomous systems, neural networks, data analysis, predictive analysis, algorithm, big data, deep learning, artificial, digital, information, generative, machine learning"
NLP_Terms="LLM, L.L.M, Large Language Models, computational linguistics, speech synthesis, bias, text mining, turing test, turing machine, natural language processing, nlp, voice recognition"
ICT_Terms="API, automat, computer, technology, techno-, technic, internet, technologies, user experience, augment, tool, model, network, application, online, software, generate, cyber, upload"

tech_words=ChatGPT_Terms+AI_Terms+NLP_Terms+ICT_Terms
tech_words=tech_words.split(", ")+Key_ignorance


# what makes us human. valuate tech for human"
human=["human", "emotion", "play","game", "empathy","kids", "love", "body", "flesh", "humanity", "humanism", "aging", "Jesus", "student", "woman", "friendship", "god", "humanoid", "child", "religion", "arcane", "baby", "corpse", "mood", "blood","well-being","employee","identity","empathy", "friend","teacher", "joy", "life", "death", "brain", "conscious", "agency", "feeling", "toughtful", "laugh" "hug" ,"imagine", "creative", "mind", "religion", "purpose", "storytelling", "narrative", "culture", "moral", "offspring", "artist","music", "dream", "poem", "poetry", "immersion", "sharing", "caring", "care", "infant", "history", "heart", "meaningful", "personal"]

commercial=["company", "organization", "capitalism", "replace", "employ", "employee", "commerc", "capital", "obsolete", "obsole"]

fraud=["fraud", "decept", "dishonest","corrupt", "embezzlement", "scam", "swindle", "forgery", "misappropriation", "misappropriate","identity theft", "Ponzi scheme", "extortion", "falsification", "phishing", "blackmail", "pyramid scheme", "data breach", "manipulation", "cybercrime", "plagiarism", "fabriaction", "ghostwriting", "ghostwrit", "exam fraud", "collusion", "essay mills", "paper mills", "ghost", "authorship", "plagiarized", "diploma", "violation", "impropriety", "ethics", "fake", "qualification", "imposter","deepfake", "appropriate", "inappropriate", "accurate", "cheat", "fool"] 


problem_words=['AI-controlled',
 'abuse',
 'abusing',
 "avoid",
 'accountability',
 'addiction',
 'afraid',
 'alienat',
 'anxgiety',
 'attack',
 'bad',
 'bias',
 'bug',
 'buggy',
 'capitalis',
 'catfishing',
 'censorship',
 'cheat',
 'collapse',
 'complaint',
 'complicated',
 'concerns',
 'copyright',
 'corrupt',
 'crash',
 "criminal",
 "crime",
 'cyberattack',
 'danger',
 'dangerous',
 'data breach',
 'data loss',
 'dehumaniz',
 'dependen',
 'digital divide',
 'disappoint',
 'discrimin',
 'disinformation',
 'displacement',
 'distrust',
 'doomsday',
 'downfall',
 'dystopia',
 'dystopic',
 'echo chamber',
 'emissions',
 "environmental impact",
 'enslave',
 "equal",
 "equity",
 'enslaving',              
 'error',
 'escapism',
 'escape',
 'extremism',
 'fail',
 'fake',
 'filter bubble',
 'footprint',
 'fraud',
 'frustation',
 'glitch',
 "hallucination",
 'harassment',
 'harm',
 'hate speech',
 'identity theft',
 'illusion',
 'impersonal',
 'imprecise',
 'inability',
 'inaccura',
 "incorrect",
 'inadequate',
 'incompatibility',
 'inconsist',
 'inefficient',
 'inequal',
 'insensitive',
 'integrity',
 'irresponsible',
 'killer',
 'lack of',
 'lag',
 'lose',
 'losing',
 'malfunction',
 'malware',
 'mental health',
 'misinterpretat',
 'misuse',
 "make up",
 "makes up",
 'nightmare',
 'obsolete',
 'opression',
 'orwel',
 'over-hype',
 'over-promising',
 'overlord',
 'overuse',
 'panic',
 'password compromise',
 'phishing',
 'plagiarism',
 'polariz',
 'power',
 'predator',
 'privacy',
 'private',
 'problem',
 'radicalization',
 'ransomware',
 'replace',
 'risk',
 'security breach',
 'sexting',
 'singularity',
 'skeptic',
 'srcap',
 'stalking',
 'struggle',
 'surveillance',
 'thought control',
 'threat',
 'totalitar',
 'trolling',
 'uncertain',
 'unemployment',
 'unemployed',
 'unfortunatly',
 'unintended',
 'unreliable',
 'unreliability',
 'victim',
 'virus',
 'vulnerable',
 'vulnerability']


#problem_words=problem_words.split(", ")

# However, as it is interesting :D
Key_However=["however","but", "nevertheless","even so", "nonetheless", "still","though","yet","notwithstanding"]



WordListDict={"predictive": predictive, "imperative":imperative, "subjunctive":subjunctive, "hype":hype_words, "modal":modal_words, "tech": tech_words, "problem": problem_words,"human":human, "fraud": fraud}

#Combined Hypeterms

def keyWords():

    d={"uncertainty": Key_uncertain,"ignorance": Key_ignorance, "hype": Key_hypes, "however": Key_However} 
    return d

def hype_word(sentence,keys=Key_hypes):
    exp=[]
    keys=list(set(keys))
    for key in keys:
        if " "+key.lower() in sentence.lower(): ## To include capitalized strings, I added .lower() in the search
            #uncertainD[key].extend([parag])
            exp.append(key)
            #print(key, sentence)
    if len(exp) >0:
        return exp


def hype_sentence(sentence,keys=Key_hypes):
    exp=[]
    keys=list(set(keys))
    for key in keys:
        if key.lower() in sentence.lower(): ## To include capitalized strings, I added .lower() in the search
            #uncertainD[key].extend([parag])
            exp.append(sentence)
            #print(key, sentence)
    exp=list(set(exp))
    if len(exp) >0:
        return exp
    
def keyword_return(sentence,keys=Key_hypes):
    exp=[]
    keys=list(set(keys))
    for key in keys:
        if key in sentence: ## To include capitalized strings, I added .lower() in the search
            #uncertainD[key].extend([parag])
            exp.append(key)
            #print(key, sentence)
    exp=list(set(exp))
    if len(exp) >0:
        return exp

