def solution(genres, plays):
    sum_genre_plays = {}
    genre_ids = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in sum_genre_plays:
            sum_genre_plays[g] = p
            
            genre_ids[g] = [i]
            
        else:
            sum_genre_plays[g] += p
            
            if len(genre_ids[g]) == 1:
                if plays[genre_ids[g][0]] < p:
                    genre_ids[g].insert(0, i)
                else:
                    genre_ids[g].append(i)
            elif len(genre_ids[g]) == 2:
                if plays[genre_ids[g][0]] < p:
                    genre_ids[g] = [i, genre_ids[g][0]]
                elif plays[genre_ids[g][1]] < p:
                    genre_ids[g] = [genre_ids[g][0], i]
    
    result = []
    genre_keys = list(sum_genre_plays.keys())
    genre_keys.sort(key=lambda g: sum_genre_plays[g], reverse=True)
    for g in genre_keys:
        result.extend(genre_ids[g])
    return result