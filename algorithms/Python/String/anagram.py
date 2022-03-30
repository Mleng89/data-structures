# Easy way to solve
def anagram_check2(str1, str2):
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

anagram_check2('dog', 'god')

# Not using a python method: O(n)
def anagram_check(str1,str2): 

    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()

    letters = {}
    if len(s1) != len(s2):
        print(False)
        return

    for i in s1:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    
    for j in s2:
        if j in letters:
            letters[j] -=1
        else:
            print(False)
            return

    print(True)
    return

anagram_check('iceman', 'micean')
anagram_check('Clint Eastwood', 'Old West Action')