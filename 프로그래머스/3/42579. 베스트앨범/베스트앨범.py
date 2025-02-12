def solution(genres, plays):
    import heapq
    
    genre_plays = {}
    genre_songs = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in genre_plays:
            genre_plays[g] = p
            genre_songs[g] = [(-p, i)]
        else:
            genre_plays[g] += p
            heapq.heappush(genre_songs[g], (-p, i))
    
    playlist = []
    for g in sorted(genre_plays.keys(), key=lambda g: -genre_plays[g]):
        for _ in range(min(2, len(genre_songs[g]))):
            playlist.append(heapq.heappop(genre_songs[g])[1])
    
    return playlist