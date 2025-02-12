def solution(genres, plays):
    import heapq
    from collections import defaultdict
    
    genre_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_plays[g] += p
        heapq.heappush(genre_songs[g], (-p, i))
    
    playlist = []
    for g in sorted(genre_plays.keys(), key=lambda g: -genre_plays[g]):
        for _ in range(min(2, len(genre_songs[g]))):
            playlist.append(heapq.heappop(genre_songs[g])[1])
    
    return playlist