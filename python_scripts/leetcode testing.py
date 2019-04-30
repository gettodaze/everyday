def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2:
        return len(s)
    i = 0
    maximum = 0
    letters = set(s[i])
    cont = True
    j = 1
    print(s)
    while (j < len(s)):
        if s[j] in letters:
            print(s[i], s[j], letters)
            i = s.index(s[j], i, j)+1
            if len(letters) > maximum:
                maximum = len(letters)
            letters = set(s[i:j])
        else:
            letters.add(s[j])
            j += 1
    else:
        if len(letters) > maximum:
            maximum = len(letters)
    print(maximum)
    return maximum


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # A palindrome is the same forward and backward.
    # return string if < 2 chars
    leng = len(s)
    if leng < 2:
        return s
    ret = ''

    # Start in the middle and traverse outward

    def string_from_center(l, r):
        if s[l] != s[r]:
            return ''
        while l > 0 and r < leng - 1 and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        return s[l:r + 1]

    for i in range(len(s) - 1):
        single = string_from_center(i, i)
        double = string_from_center(i, i + 1)
        ret = max(ret, single, double, key=len)
    print(ret)
    return ret


def convert(s, numRows):
    def abs(num):
        if num < 0:
            num = -num
        return num

    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    def oscillating_counter(rang, max_val):
        y = 1
        count_up = False
        for i in range(rang):
            if y == 0:
                count_up = True
            elif y == max_val:
                count_up = False
            y += 1 if count_up else -1
            yield (i, y)

    chars = [[] for _ in range(numRows)]
    print(chars)
    for i, assignment in oscillating_counter(len(s), numRows-1):
        print(i, assignment)
        chars[assignment].append(s[i])
        print(chars)

    final = []
    for char_list in chars:
        final.extend(char_list)

    return ''.join(final)

    def reverse_int(x):
        y = str()

    # Case 1: only 1 row: same string
    # 2 rows: every row gets every other
    # 3 rows: 1: 1,_,5,_,9
    #           2 4 6 8 10
    #           3,_,7,_
    #
    # 4 rows: 1: 1     7     3
    #           2   6 8   2
    #           3 5   9 1
    #           4     0
    # row_one_additive = (numRows-1)*2
    # 4 rows:


if __name__ == '__main__':
    convert("PAYPALISHIRING",3)