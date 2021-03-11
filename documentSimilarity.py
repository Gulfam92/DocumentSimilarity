punctuations = {".",",","!","'"}
stopwords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}


def filter_sent(s):
    new_sent = set()
    s = s.strip()
    words = s.split(" ")
    for w in words:
        w = w.lower()
        tmp = ""
        for ch in w:
            if ch not in punctuations:
                tmp += ch
        if tmp not in stopwords:
            new_sent.add(tmp)
    return new_sent


def check_similarity(a,b):
    #jaccard
    ab_intersec = a.intersection(b)
    ab_union = a.union(b)
    # score = len(a_b)/(len(a)+len(b))
    score = len(ab_intersec)/len(ab_union)
    return score


if __name__=="__main__":
    # s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    # s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    # s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
    
    s1 = input("Enter first sentence:  ")
    s2 = input("Enter second sentence:  ")
    s3 = input("enter third sentence:  ")
    p1 = filter_sent(s1)
    p2 = filter_sent(s2)
    p3 = filter_sent(s3)
    
    score1 = check_similarity(p1,p2)
    score2 = check_similarity(p1,p3)
    print(score1)
    print(score2)
    
    
                    