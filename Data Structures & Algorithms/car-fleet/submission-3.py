class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        eta = deque()
        count = 0

        zipped = list(zip(position,speed))
        pairs = sorted(zipped, reverse=True)

        for i in range(len(pairs)):
            time = (target - pairs[i][0]) / pairs[i][1]
            eta.append(time)

        while eta:
            count += 1
            cur = eta.popleft()
            while eta and eta[0] <= cur:
                eta.popleft()
    
                

        return count


        