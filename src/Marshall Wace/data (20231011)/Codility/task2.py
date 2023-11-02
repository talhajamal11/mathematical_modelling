""" 
You get an implementation of the dirty floor problem, and you’re tasked with finding the bug in it, 
fixing it by changing 2 lines of code max. The bug is in the fact that during DFS, you can loop around 
the room because of negative indices
"""

# Robot Room Cleaner - Leetcode Hard

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def goBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(pos, robot, d, lookup):
            robot.clean()
            for _ in directions: # Try out all 4 direcitons
                new_pos = (pos[0]+directions[d][0],
                           pos[1]+directions[d][1])
                if new_pos not in lookup: # Check set and if this position has not been explored, move to it
                    lookup.add(new_pos)
                    if robot.move():
                        dfs(new_pos, robot, d, lookup)
                        goBack(robot)
                robot.turnRight()
                d = (d+1) % len(directions)
        
        dfs((0, 0), robot, 0, set())



