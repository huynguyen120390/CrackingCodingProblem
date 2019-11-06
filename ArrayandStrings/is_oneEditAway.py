
def is_oneEditAway(str1,str2):
    def __is_replaceOne(str1,str2):
        """
            Condition: 2 strings has the same length ,
            so we just need to monitor number of character changes.
            If more than 1 change , that can't be one edit away
        """
        replace = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                replace+=1
                if replace > 1:
                    return False
        return True

    def __is_removeOneoraddOne(str1,str2):
        """
            Condition: 2 strings +/- 1 character
            We need to track this for one edit away: N for New Member, C for  Number of Char Change
                Add One: N = 0 && C = 1 (add an existing char) or N=1 && C == 0 (add an new char)
                Remove One: N = 0 && C = 1 (remove an repeated char) or N = 0 && C == 1( remove a unique char)
                Other : outside of these pattern [(0,1),(1,0)]
        """
        monitorTable = {}
        newCharTable = {}
        for s in str1:
            if s in monitorTable:
                monitorTable[s] += 1
            else:
                monitorTable[s] = 1
        for s in str2:
            if s in monitorTable:
                monitorTable[s] -=1
            else:
                if s in newCharTable:
                    newCharTable[s] += 1
                else:
                    newCharTable = 1
        print(monitorTable)
        print(newCharTable)
        #Stat
        charChange = 0
        for s in monitorTable:
            if monitorTable[s] != 0:
                charChange += 1
                if charChange > 1:
                    return False
            
        newMem = len(newCharTable)

        pair = (newMem,charChange)
        print("Hey",pair)
        #Judge
        if pair in [(0,1),(1,0)]:
            return True
        else:
            return False

    
    if str1 == None or str2 == None:
        raise NullString
    elif str1 == str2: # same
        return True 
    elif abs(len(str2) - len(str1)) >2:
        return False
    elif len(str2) - len(str1) == 0:
        return __is_replaceOne(str1,str2)
    else:
        return __is_removeOneoraddOne(str1,str2)
        
            

    
class NullString(Exception):pass
print(is_oneEditAway("concobebenodaucanhtre","concobebenodaucanhtre"))
        


        