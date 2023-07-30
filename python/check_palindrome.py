def check_palindrome(word):
    start = 0
    end = len(word) - 1
    print("we are here")
    while start <= end:
        if word[start] != word[end]:
            print("not a palindrome")
            break
        start = start + 1
        end = end - 1
    
    print("is a palindrome")
    
check_palindrome("nbbabbn")