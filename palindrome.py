def isPalindrome(head):
    palindrome = False
    length = len(head)

    for i in range(length // 2):
        for j in range(-1, -(length//2), -1):
            if head[i] == head[j]:
                print(head[i], head[j])
                palindrome = True

    return palindrome

print(isPalindrome([3,4,5,6,7,7,8,8,7,7,6,5,4,3]))