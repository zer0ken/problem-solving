def solution(n, build_frame):
    PILLAR = 0
    CEIL = 1
    
    structures = set()
    
    def is_stable():
        for x, y, a in structures:
            if a == PILLAR:
                if not (
                    y == 0 
                    or (x, y - 1, PILLAR) in structures
                    or (x - 1, y, CEIL) in structures
                    or (x, y, CEIL) in structures
                ):
                    return False
            elif not (
                (x, y - 1, PILLAR) in structures
                or (x + 1, y - 1, PILLAR) in structures
                or (
                    (x - 1, y, CEIL) in structures
                    and (x + 1, y, CEIL) in structures
                )
            ):
                return False
        return True
    
    for x, y, a, b in build_frame:
        structure = (x, y, a)
        if b:
            structures.add(structure)
            if not is_stable():
                structures.remove(structure)
        else:
            structures.remove(structure)
            if not is_stable():
                structures.add(structure)                
    
    return sorted(map(list, structures))