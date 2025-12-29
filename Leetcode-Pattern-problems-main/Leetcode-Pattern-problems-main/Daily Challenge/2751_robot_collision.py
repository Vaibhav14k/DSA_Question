class Solution:
    def survivedRobotsHealths(
        self, positions:list[int], healths:list[int], directions: str
    ) ->list[int]:
        n = len(positions)
        indices = list(range(n))
        stack = []

        # Sort indices based on their positions
        indices.sort(key=lambda x: positions[x])

        for current_index in indices:
            # Add right-moving robots to the stack
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index] > 0:
                    # Pop the top robot from the stack for collision check
                    top_index = stack.pop()
                    if healths[top_index] > healths[current_index]:
                        # Top robot survives, current robot is destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        # Current robot survives, top robot is destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        # Both robots are destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

obj = Solution()
positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(obj.survivedRobotsHealths(positions, healths, directions))