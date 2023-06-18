from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    #hash1 genre:totalPlays
    hash1 = {}
    #hash2 genre: [id,play]
    hash2 = {}
    for i in range(len(genres)):
        genre,play = genres[i], plays[i]
        
        if genre in hash1:
            hash1[genre] += plays[i]
        else:
            hash1[genre] = plays[i]
        
        if  genre in hash2:
            hash2[genre].append([play,i])
        else:
            hash2[genre] = [[play,i]]
            
    hash1 = dict(sorted(hash1.items(), key = lambda x: x[1], reverse = True))
    for key in hash1:
        temp = sorted(hash2[key],key = lambda x: (x[0],-int(x[1])), reverse = True)
        if len(temp) > 1:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            answer.append(temp[0][1])

    
    return answer