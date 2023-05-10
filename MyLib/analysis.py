from datetime import datetime
Today=datetime.now().strftime('%Y-%m-%d')

def make_wordcloud(flat_list,filename,Mostcommon=100,bg="white"):
    from collections import Counter
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    
    a_counter = Counter(flat_list)
    most_common = a_counter.most_common(Mostcommon)
    wordcloud=WordCloud(background_color=bg, width=1200, height=1200).generate_from_frequencies(dict(most_common))
    
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    
    
    
    if filename!="":
        plt.savefig(Today+"_"+filename+".pdf",dpi=300)
        
    plt.show()