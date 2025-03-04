str1="aeiouaeiouaeiougfesuir"

def vow_occr(sentence):
    lis=['a','e','i','o','u']
    count=0
    for i in str1:
        if i in lis:
            count=count+1
    return count

print(vow_occr(str1))