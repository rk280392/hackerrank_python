def anagram(s1,s2):
    s1 = s1.replace(' ','').upper()
    s2 = s2.replace(' ','').upper()
    if sorted(s1) == sorted(s2):
        print("Yes")
    else:
        print("No")

my_str1 = input()
my_str2 = input()

anagram(my_str1, my_str2)
