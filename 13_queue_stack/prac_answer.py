def palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:  #내 답안에서는  i == j 이면 비교할 필요가 없다는 사실을 간과했음
        if s[i].isalpha() == False:
            i += 1 #여기서 루프 하나가 끝나고 다시 while문을 시작함.
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
        

    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Mada, I am Adam"))

