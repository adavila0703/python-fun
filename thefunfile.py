# Write a function that computes the volume of a sphere given its radius.
def volume_sphere(num):
    comp = (4 / 3) * 3.14 * (num ** 3)
    return comp


# print(str(round(volume_sphere(2), 2)))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def checknum(num, r1, r2):
    if num in range(r1, r2):
        return True
    else:
        return False


# print(checknum(3,2,7))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(wrd):
    print("hello?")
    uppercount = 0
    lowercount = 0
    for w in wrd:
        if w.isupper():
            uppercount += 1
        elif w.islower():
            lowercount += 1
    return f"Upper count is {uppercount} \nLower count is {lowercount}"


# print(up_low("This Is a Test StrinG!!"))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
multi = 1


def list_multi(*args):
    global multi
    for a in args:
        if type(a) is int:
            multi *= a
    return multi


yourlist = [1, 2, 3, -4]


#print(list_multi(list(map(list_multi, yourlist))))


# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(wrd):
    cut = wrd.split()
    nspace = ''.join(cut)
    if list(nspace) == list(reversed(nspace)):
        return True
    else:
        return False


# print(palindrome('racecar'))


# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def pan(wrds):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    li = sorted(wrds.lower())
    joining = ''.join(li)
    remov = ''.join(list(dict.fromkeys(joining.strip())))
    if remov == abc:
        return True
    else:
        return False

#print(pan("The quick brown fox jumps over the lazy dog"))


# Make a function where you can filter from a list of numbers of ranges 0 to 1000, numbers which are divisible by
# 2 and 3.
def crazy_math(num):
    return num % 2 == 0 and num % 3 == 0


crazylist = range(0, 1000)


# print(list(filter(crazy_math, crazylist)))


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_evens(*args):
    if args[0] % 2 == 0 and args[1] % 2 == 0:
        return min(args)
    elif args[0] % 2 == 1 or args[1] % 2 == 1:
        return max(args)


# print(lesser_evens(2,4))
# print(lesser_evens(2,5))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(wrds):
    if wrds.split()[0][0] == wrds.split()[1][0]:
        return True
    else:
        return False


# print(animal_crackers('Levelheaded Llama'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False


def makes_twenty(*args):
    if sum(args) == 20 or args[0] == 20 or args[1] == 20:
        return True
    else:
        return False


# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(wrds):
    li = list(wrds)
    split = ""
    count = 0
    for l in li:
        if count == 0:
            split += l.upper()
        elif count == 3:
            split += l.upper()
        else:
            split += l
        count += 1
    return split


# print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(wrds):
    li = wrds.split()
    li.reverse()
    comp = ' '.join(li)
    return comp


# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
#
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if n in range(90, 111) or n in range(190, 211):
        return True
    else:
        return False


# print(almost_there(111))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def checkarr(num):
    i = 1
    for n in num:
        try:
            if n == 3 and num[i] == 3:
                return True
        except:
            pass
        i += 1
    return False

# print(checkarr([3, 0, 3, 3, 0, 0, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(wrds):
    word = ''
    for w in wrds:
        word += w*3
    return word

#print(paper_doll('hello'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If
# their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST' blackjack(5,6,7) --> 18 blackjack(9,9,9) --> 'BUST' blackjack(9,9,11) --> 19


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶ summer_69([1, 3,
# 5]) --> 9 summer_69([4, 5, 6, 7, 8, 9]) --> 9 summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(num):
    newlist = []
    for n in num:
        if n in range(6, 10):
            pass
        else:
            newlist.insert(0, n)
    return sum(newlist)


#print(summer_69([2, 1, 6, 9, 11]))



# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
#
# By convention, 0 and 1 are not prime.


# -The only even prime number is 2. All other even numbers can be divided by 2.
# -If the sum of a number's digits is a multiple of 3, that number can be divided by 3.
# -No prime number greater than 5 ends in a 5. Any number greater than 5 that ends in a 5 can be divided by 5.
# -Zero and 1 are not considered prime numbers.
# -Except for 0 and 1, a number is either a prime number or a composite number. 
#     A composite number is defined as any number, greater than 1, that is not prime.

def count_primes(num):
    for n in num:
        if n % 2 == 1 or n % 3 == 2:
            num.remove(n)
    return num

print(count_primes(list(range(0, 1000))))

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter¶
# print_big('a')
#
# out:   * * * ***** *   * *   * HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to
# specific 5-line combinations of patterns. For purposes of this exercise, it's ok if your dictionary stops at "E".


# Use for, .split(), and if to create a Statement that will print out words that start with 's':
def splityo():
    st = 'Print only the words that start with s in this sentence'
    thelist = st.split()
    for a in thelist:
        if a[0] == "s":
            print(a)


# splityo()

# Use range() to print all the even numbers from 0 to 10.'
def evennum():
    a = [x for x in range(0, 11) if x % 2 == 0]
    print(a)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
def difbythree():
    a = [x for x in range(1, 51) if x % 3 == 0]
    print(a)


# Go through the string below and if the length of a word is even print "even!"
def evenword():
    st = 'Print every word in this sentence that has an even number of letters'
    for a in st.split():
        if len(a) % 2 == 0:
            print(a)


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz():
    cool_list = [0] * 100
    for a in range(1, 100):
        if a % 3 == 0:
            cool_list[a] = "Fizz"
            if a % 5 == 0:
                cool_list[a] = "Buzz"
                if a % 3 == 0 and a % 5 == 0:
                    cool_list[a] = "FizzBuzz"
        else:
            cool_list[a] = a
    print(cool_list)


# Use List Comprehension to create a list of the first letters of every word in the string below:
def listcomp():
    st = 'Create a list of the first letters of every word in this string'
    licomp = [a[0] for a in st.split()]
    print(licomp)


# Reverse a string
hello = ['reverse']
# print(list(map(lambda x:x[::-1], hello)))


# Unpack 'hello' from this nexted list/dictionary
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# print(d['k1'][0]['nest_key'][1][0])


# unpack this hello
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}

# print(d["k1"][2]["k2"][1]["tough"][2][0])
