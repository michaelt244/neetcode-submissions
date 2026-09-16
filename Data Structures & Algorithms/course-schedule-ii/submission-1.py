class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        orderlist = []

        cycle = set() #helping us track if we have a loop - actively searching 
        visted = set() #already searched

        def dfs(course):
            if course in cycle:
                return False
            if course in visted:
                return True

            #adding course to the set since we are currently visiting it
            cycle.add(course)

            #now checking the prerequisites
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False

            #removing it from the set since we are done visiting it
            cycle.remove(course)
            visted.add(course)
            orderlist.append(course)
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return orderlist
                          
            
