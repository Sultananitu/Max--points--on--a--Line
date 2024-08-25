class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        if n <= 2:
            return n
        
        max_points = 0
        for i in range(n):
            
            perpendicular = 0
            same_points = 0
            slopes = []
            
            for j in range(n):
                if points[i][0] == points[j][0]:
                    if points [i][1] == points[j][1]:
                        same_points += 1
                    else:
                        perpendicular += 1
                    continue
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                slope = 1000000000 * dy / dx
                slopes.append(slope)
                
            max_ = 0
            c = Counter(slopes)
            if len(c) > 0:
                _, max_ = c.most_common(1)[0]
                
            if max_ + same_point > max_points:
                max_points = max_ + same_point
                
            if perpendicular + same_point > max_points:
                max_points = perpendicular + same_point
                
        return max_points
                
                
                
            
        
        