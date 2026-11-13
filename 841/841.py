class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited=set()
        def dfs(cur):
            visited.add(cur)
            curKeys=rooms[cur]
            for room in curKeys:
                if(room not in visited):
                    dfs(room)
        dfs(0)
        return len(rooms)==len(visited)
