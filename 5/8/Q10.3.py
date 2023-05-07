word = 'echo'
t = ()
count = 3

echo = (word,)
echo *= count
cho = (word[1:],)
cho *= count
ho = (word[2:],)
ho *= count
o = (word[3:],)
o *= count

t = echo + cho + ho + o
print(t)