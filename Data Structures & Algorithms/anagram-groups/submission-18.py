class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        #empty dictionary 
        groups = {}
        #go by each work and count the frequency of each charcter as this is all we care about
        #once we have the frequecney we can use that as the key to the dicitonary 
        #anagrams will have that same frequency so we can add that word to the list if so 
        for word in strs:
            #default lsit of [0,0,0,0,0 ... 0] to get the frequency
            check = [0] * 26

            for w in word:
                #standrize the asci count to fit into the check list size(26)
                check[ord(w) - ord('a')] += 1

            #send a tuple(unmutable) since we cant send a mutable object(list) as a key
            if tuple(check) not in groups:
                groups[tuple(check)] = [word]
            else:
                groups[tuple(check)] += [word]
            
        
        #return all the vlaues in a list
        return list(groups.values())
            
            




