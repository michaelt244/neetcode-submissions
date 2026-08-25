class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i: [] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)


        visting = set()
        
        def dfs(src):
            if src in visting:
                return False #there is a cycle
            if adjList[src] == []:
                return True #no pre prerequisite

            visting.add(src)
            #check all the prerequisite of the src

            for pre in adjList[src]: 
                if not dfs(pre):
                    return False
            
            #if no cycle remove the current class out the set
            visting.remove(src)
            adjList[src] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
