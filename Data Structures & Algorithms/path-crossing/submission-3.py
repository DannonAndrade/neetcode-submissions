class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        curr = [0,0]

        for move in path:
            if move == 'N':
                curr[1] += 1
                print(curr)
            if move == 'E':
                curr[0] += 1
                print(curr)
            if move == 'S':
                curr[1] -= 1
                print(curr)
            if move == 'W':
                curr[0] -= 1
                print(curr)
            
            if tuple(curr) in visited: return True
            visited.add(tuple(curr))
        
        return False

        