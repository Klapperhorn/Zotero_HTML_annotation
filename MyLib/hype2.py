
Key_uncertain=['suggest\w*', 'possible', 'may', 'potentially', 'not adequately', 'should', 'will', 'probably', 'hypothesis', 'could', 'implicate\w*', 'perhaps', 'likely', 'might', 'perhaps', 'possibility', 'possible', 'possibly', 'potentially', 'probably', 'seem\w*', 'speculate\w*', 'whether', 'suspect\w*', 'suppose\w*', 'unsure', 'speculation', 'uncertainty']

Key_ignorance=['not understood', 'not been explored', 'not explored', 'not assessed' , 'did not demonstrate', 'little is known', 'unexplored', 'unknown', 'not known', 'unclear', 'not designed to', 'did not allow for', 'controversial', 'ha\w* not been determined', 'incomplete', 'open question', 'not fully', 'not comprehensively', 'not specifically', 'debated', 'contentious', 'unknown', 'further investigation', 'not intended to', 'not planned to', 'not yield', 'not distinguish\w*', 'not determined', 'not evaluated', 'not estimated', 'not measured', 'not investigated', 'has not been specified', 'has not been settled', 'has not been concluded', 'not been investigated', 'not been researched']


#hype according to the Miller et al. 2019
hypeAdj=["experienced","important","relevant","essential","novel","senior","notable","unique",
"trained","significant","key","emphasize","exhaustive","comprehenisve","fundamental","specialized",
"excellent","unwanted","appropriate","innovative","precise","strong","high","scarce","newer","useful",
"detailed","expert","critical","impactful","board-certified","high-volume","particular","qualified"]

hypeAdv=["very", "more", "particularly", "obviously", "well", "importantly", "even", "most highly", 
"especially", "greatly", "further", "markedly", "successfully", "much", "without question", "always", 
"objectively", "interestingly", "exactly", "specifically", "ever", "stricly", "certainly", "effectively", 
"easily", "steadily", "few", "entirely", "significantly", "unlike", "only", "all"]

hypeNoun=["strength", "importance", "robustness", "experience", "interest", "expert"]

hypeVer=["assure\w*", "not succeed", "strengthen\w*", "maximize\w*", "reinforce\w*", "empower\w*", "highlight\w*", "recognize\w*"]

# Miller_2022 hypewords
hype_words2022=['novel', 'critical', 'key', 'innovative', 'scientific', 'effective', 'successful', 'diverse', 'significant', 'advanced', 'robust', 'relevant', 'strong', 'unique', 'comprehensive', 'broad', 'essential', 'rigorous', 'promising', 'interdisciplinary', 'urgent', 'quality', 'first', 'unmet', 'outstanding', 'efficient', 'substantial', 'multidisciplinary', 'crucial', 'strategic', 'unprecedented', 'fundamental', 'timely', 'scalable', 'largest', 'powerful', 'extensive', 'top', 'international', 'exciting', 'devastating', 'senior', 'ideal', 'sustainable', 'accessible', 'rich', 'accurate', 'exceptional', 'emerging', 'vast', 'intellectual', 'productive', 'meaningful', 'compelling', 'transformative', 'efficacious', 'foundational', 'synergistic', 'transdisciplinary', 'ready', 'easy', 'qualified', 'durable', 'actionable', 'elusive', 'impactful', 'deeper', 'vital', 'tremendous', 'greatest', 'latest', 'enormous', 'sophisticated', 'pivotal', 'imperative', 'reproducible', 'generalizable', 'experienced', 'longstanding', 'unparalleled', 'user-friendly', 'attractive', 'talented', 'invaluable', 'remarkable', 'safer', 'skilled', 'massive', 'seamless', 'unanswered', 'notable', 'vibrant', 'huge', 'intriguing', 'alarming', 'creative', 'motivated', 'paramount', 'renowned', 'surprising', 'indispensable', 'myriad', 'tailored', 'ample', 'fastest', 'cohesive', 'premier', 'immense', 'ambitious', 'overwhelming', 'dismal', 'revolutionary', 'confident', 'dedicated', 'biggest', 'dire', 'nuanced', 'intuitive', 'tangible', 'incredible', 'daunting', 'collegial', 'interprofessional', 'deployable', 'expansive', 'groundbreaking', 'prestigious', 'stellar', 'stark', 'desperate', 'careful', 'systematic', 'interesting', 'immediate', 'ultimate', 'considerable', 'detailed', 'important', 'major']

#manually added hype terms
manual_hype_words=['envious', 'fundamentally', 'futurist\\w*', 'happy', 'reshape\\w*', 'transformed', 'diligent', 'succeed\\w*', 'extinct\\w*', 'disrupt\\w*', 'in a world']

Key_hypes=list(set(hypeAdj+hypeAdv+hypeNoun+hypeVer+hype_words2022+manual_hype_words))


# modal words from Ann Mische
predictive="can", "could", "may", "might", "will", "would"

imperative="have to", "let\w?", "must", "need\w{0,2}", "ought\w*", "should", "shouldn't" "has to"

subjunctive="aim\w{0,3}", "ask\w* for", "belief\w*", "believe" "doubt\w*", "expect\w*", "fear\w?", "hope\w*", "urge\w?", "want\w*", "wish\w*", "would(?:...) like to"

# manually added modal words

promise="promis\w*", "overpromis\w*", "commit\w*", "pledg\w*","swear\w*", "vow\w*", "assur\w*", "guarant\w*", "coven\w*", "oath", "undertake", "declar\w*", "affirm\w*", "troth", "bond", "dedicate"

overpromise="overstat\w*", "inflat\w*", "overcommit\w*","overextend\w*", "hyperbolize", "hype", "oversell\w*", "aggrandiz\w*", "promis. too much", "unrealistic assurance", "overassur\w*", "empty promis\w*", "untenable"

promise=promise+overpromise

modal_words=list(set(predictive+imperative+subjunctive))

ChatGPT_Terms="GPT\W?\d?, ChatGPT3, ChatGPT, OpenAI, Chat-GPT, conversational AI\w*, chat interface\w?, virtual assistant\w?, human-computer, Chatbot\w?, chat-bot\w?"

AI_Terms="AI, A\.I, coginitive computing, self-learning, supervised learning, explainable AI, algorithmic, AI ethic\w?, facial recognition, recommender system\w?, autonomous system\w?, neural network\w?, data analys\w*, predictive analysis, algorithm\w*, big data, deep learning, artificial, digital, information, generative, machine learning"

NLP_Terms="LLM\w?, L\.L\.M, Large Language Model\w?, computational linguistics, speech synthesis, bias\w{0,2}, text mining, turing test, turing machine\w?, natural language processing, nlp, voice recognition"
ICT_Terms="API, automat\w*, robot\w?, computer\w*, technolog\w*, techno\S*, technic, technique, code\w*, coding, coded, automatically, virtual\S*, internet, user experience\w?, augment, tool\w*, model\w*, network, application\w?, online, software, generate\w*, cyber, upload\w*, machine\w*, computing, system\w*, quantum, architecture"

tech_words=ChatGPT_Terms.split(", ")+AI_Terms.split(", ")+NLP_Terms.split(", ")+ICT_Terms.split(", ")


# what makes us human. valuate tech for human"

human=["human\S*", "emotion\w*", "play","game\w*", "empathy","kid\w*", "love", "body", "bodies", "flesh", "humanity", "humanism", "aging", "Jesus", "student\w*", "woman", "women", "female\w?","male\w?", "friendship", "god\w*", "humanoid\w*", "child", "religion\w*", "arcane", "baby", "corpse", "mood", "blood","well-being","employee\w*","identity","empathy", "friend\w*","teacher\w*", "joy", "life", "death", "brain\S*", "conscious\w*", "agency", "feeling\w*", "toughtful", "laugh\w*" "hug\w*" ,"imagine\w*", "creative", "mind\w*", "purpose\w*", "storytelling", "narrative\w*", "culture\w*", "moral\w*", "offspring", "artist\w*","music", "dream\w*", "poem", "poetry", "immersion", "sharing", "caring", "care\w*", "infant\w*", "history", "heart", "meaningful", "personal"]

fraud=["fraud\w*", "decept\w*", "dishonest\w*","corrupt\w*", "embezzlement\w*", "scam\w*", "swindle", "forgery\w*", "misappropriation", "misappropriate\w*","identity theft\w*", "Ponzi scheme\w*", "extortion", "falsification\w*", "phishing", "blackmail\w*", "pyramid scheme\w*", "data breach\w*", "manipulation\w*", "cybercrime\w*", "plagiarism\w*", "fabriaction\w*", "ghostwrit\w*", "exam fraud", "collusion", "essay mill\w*", "paper mill\w*", "ghost", "authorship", "plagiarize\w*", "diploma", "violation\w*", "impropriety", "ethic\w*", "fake\S*", "qualification\w*", "imposter\S*","deepfake\w*", "appropriate", "inappropriate", "\w*accurate", "cheat\w*", "fool", "peer-review"] 

climate=["sustainab\w*","emission\w?", "carbon\w*", "climate", "global warming", "greenhouse", "methane","pollut\w*", "renewable", "energy.","fossil.", "mitigation", "COP26", "sea level", "extreme weather", "carbon footprint", "deforestation","ressource\w?"]

## environmental brainfuck
exclude_pre=["learning","teaching","testing","HPC","technological","computer","computing","enclosed","office365","exercise",\
             "administrative","facility"," an", "complex","different","professional","work","digital","consolidated",\
             "dynamic","organisation","rich","cloud","research","computational","educational","vr","working","virtual",\
             "open-minded","communication","controlled","safe","inspiring","university","academic","physical","\W","personal",\
             "protected","ICT","experimental","my own","living","patient\'s","unregulated","practice", "built","new", "in existing","this"]
environment_brainfuck=["(?<!"+" )(?<!".join(exclude_pre)+" )environmenta?l?"]


# include the environmental brainfuck?
#climate+=environment_brainfuck

exclude_pre=["artificial", "computational", "ArtificiaI","national"]
intelligence="(?<!"+" )(?<!".join(exclude_pre)+" )intelligenc?e?t?"

exclude_pre=["machine.","machine","machinal","deep.", "deep","reinforcement","reinforcement."]

learning="(?<!"+" )(?<!".join(exclude_pre)+")learn\w*"

learning=[intelligence,learning, "educat\w*"]



capitalism=["profit", "business", "corporat\w*", "compan\w*", "industr\w*", "market\w*", "shareholder\w*", "stakeholder\w*", "revenue", "invest\w{0,3}","investment\w?","competit\w*", "capital\w*", "growth", "market shrare", "supply chain", "consum\w*", "brand", "sales", "advertis\w*", "trad\w*", "merchandise", "productiv\w*", "economic\w*","monopoly", "conglomerate", "CEO", "wall street", "stock market", "IPO", "dividend", "business model", "Corporate social responsibility", "free market", "capital accumulation", "private sector", "invest\w*", "entrepreneur\w*", "financial\w*", "asset\w*", "marx", "schumpeter", "property", "profit", "supply and demand", "enterprise", "laissez-faire", "invisible hand", "wealth creation", "inequality", "liberalism", "growth", "venture capitalism", "startup\w?", "innovation", "disrupt\w*", "angel investor", "pitch", "funding", "prototype", "incubator", "tech hub", "silicon valley", "tech giant"]

replacement=["employee\w?", "employ\w*", "workforce", "labor\w*", "automat\w*", "robot\w*","tak\w* over",  "job\w?", "displace", "outsourc\w*", "job security", "unemploy\w*", "wage", "salery", "human resource\w?", "labor market\w?", "skill gap", "redundanc\w*", "retrain\w*", "reskill\w*", "replac\w*", "career", "employment contract", "labor right\w?", "union\w*", "downsiz\w*","layoff","lifelong learning", "digital literacy", "technological proficiency", "professional development"]

edu=["educat\w*", "academ\w*", "learn\w*", "teach\w*", "\w*school\w*", "universit\w*", "colleg\w*", "classroom\w?", "student\w*", "curriculum", "degree", "scholar", "lecture", "stud\w*", "homework", "exams?", "examination", "graduat\w*", "pedagog\w*", "higher education", "educational system", "academic discipline", "humanities","engineering", "campus", "professor\w*", "thesis\w*", "dissertation\w?", "librar\w*", "assess\w*", "examin\w*", "test", "quiz", "assessment criteria", "grading", "grade\w?", "multiple-choice", "proctor", "midterm", "retake", "resit", "lecture\w?", "assignment\w?","learning environment", "teaching envirionment"]

anthropomorphism=["bonding","friend","emotion","alienat\w*","lonely","love","intimacy", "feeling", "relatable","sympathy","sympathetic","fall in love","loving","passion","companion", "camaraderie","relationship","understanding","loyal","car\w*","isolation", "anthropo\w*", "personificat\w*", "humanization", "human-like", "humanizing", "personify", "human characteristics", "treati?n?g? as human","human traits?", "human-centric", "human analogies", "authentic", "human element"]

privacy=["privacy","protect\w*","personal","data sovereignty","confidential","secrecy","secrets?","privacy rights?","consent", "intrusion","surveillanc?e?","private","breach","intrusion","access","u?n?authorized","data mining", "invasion","data expoitation","consensual"]

discrimination=["n?o?n?discriminat\w*", "black box", "biase?s?", "racis\w*", "fairness", "racial profiling", "unfair", "data skew", "equity", "diversity", "black", "women", "female", "white", "stereotyp\w*", "justice", "gender", "inclusiv\w*", "accessib\w*", "non-neutral\w*"]

problem_words=['AI-controlled', 'abuse\\w*', 'abusing', 'avoid\\w*', 'accountability', 'addiction', 'afraid', 'alienat\\w*', 'anxiety', 'attack\\w*', 'bad', 'bias\\w*', 'bug\\w*', 'buggy', 'capitalis\\w*', 'catfishing', 'censorship', 'cheat\\w*', 'collapse', 'collaps\\w*complaint\\w*', 'complicate\\w*', 'concerns', 'copyright', 'corrupt\\w*', 'crash\\w*', 'criminal\\w*', 'crime\\w*', 'cyberattack\\w*', 'danger', 'dangerous', 'data breach\\w*', 'data loss\\w*', 'dehumaniz\\w*', 'dependen\\w*', 'digital divide', 'disappoint\\w*', 'discrimin\\w*', 'disinformation', 'displacement', 'distrust', 'doomsday', 'downfall', 'dystopia\\w*', 'dystopic', 'echo chamber\\w*', 'emission\\w*', 'environmental impact\\w*', 'enslave\\w*', 'equal\\w*', 'equity', 'enslaving', 'error\\w*', 'escapism', 'escape\\w*', 'extremism', 'fail\\w*', 'fake', 'filter bubble\\w*', 'footprint\\w*', 'fraud\\w*', 'frustation', 'glitch', 'hallucination\\w*', 'harassment', 'harm\\w*', 'hate speech\\w*', 'identity theft', 'illusion\\w*', 'impersonal', 'imprecise', 'inability', 'inaccura\\w*', 'incorrect', 'inadequate', 'incompatibility', 'inconsist\\w*', 'inefficientinefficiency', 'inequal\\w*', 'insensitive', 'integrity', 'irresponsible', 'killer', 'lack of', 'lag\\w*', 'lose', 'lostlosing', 'malfunction\\w*', 'malware', 'mental health', 'misinterpretat\\w*', 'misuse\\w*', 'make up', 'makes up', 'nightmare\\w*', 'obsolete', 'opression', 'orwel\\w*', 'over-hype\\w*', 'over-promis\\w*', 'overlord', 'overuse\\w*', 'panic\\w*', 'password compromise\\w*', 'phishing', 'plagiarism', 'polariz\\w*', 'power', 'predator', 'privacy', 'private', 'problem\\w*', 'radicalization', 'ransomware', 'replace\\w*', 'risk\\w*', 'security breach\\w*', 'sexting', 'singularity', 'skeptic', 'srcap', 'stalking', 'struggle', 'surveillance', 'thought control', 'threat\\w*', 'totalitar', 'trolling', 'uncertain\\w*', 'unemployment', 'unemploy\\w*', 'unfortunatly', 'unintended', 'unreliable', 'unreliability', 'victim\\w*', 'virus\\w*', 'vulnerable', 'vulnerability']


problems_and_ignorance=problem_words +Key_ignorance

# However, as it is interesting :D
Key_However=["however","but", "nevertheless","even so", "nonetheless", "still","though","yet","notwithstanding"]


## Modal words are excluded because they are found with the POS detection.
WordListDict={"predictive": predictive, "imperative":imperative, "subjunctive":subjunctive, "hype":hype_words, "tech": tech_words, "problem": problems_and_ignorance,"human":human, "fraud": fraud, "climate":climate, "capitalism": capitalism, "replacement":replacement,"edu":edu, "anthropomorphism": anthropomorphism, "learning": learning, "privacy":privacy,"promise": promise, "discrimination": discrimination}

#Combined Hypeterms

def keyWords():

    d={"uncertainty": Key_uncertain,"ignorance": Key_ignorance, "hype": Key_hypes, "however": Key_However} 
    return d

def hype_word(sentence,keys=fraud):
    import re
    keywords=list(set(keys))
    # \b hinders combined words like task from ask
    key_re = re.compile(r"(\b"+r'|\b'.join(keywords)+r")", re.IGNORECASE)
    exp=key_re.findall(sentence)
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

