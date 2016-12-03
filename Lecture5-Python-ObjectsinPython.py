##Lecture 5
##Objects in Python
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Tuples, Lists, Dictionaries - used to collect data items.

##Tuple - ordered sequence of items. Immutablee. 
Test = (1, 2, 3, 4, 5)
print Test[0]
print Test[0:5]
print Test[-1] ##gives the last item.
print len(Test)##gives the length of the tuple.

##Finds divisors and then collects them into a tuple.
x = 20
divisors = ()
for i in range(1,x):
    if x%i == 0:
        divisors = divisors+(i,)
print divisors

##Lists - ordered sequence of items. Mutable.
##Techs is appended to the one element list Univs. The one element is itself a list.
Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = []
Univs.append(Techs)##append doesn't assign but mutates the list. It actually changes it.
print 'Univs =', Univs

Univs.append(Ivys)##now contains two elements.
print 'Univs =', Univs
for e in Univs:##iterate the elements in the list.
    print 'e =', e

flat = Techs + Ivys
print 'flat =', flat

artSchools = ['RISD', 'Harvard']
for u2 in artSchools:
    if u2 in flat:
        flat.remove(u2)##now flat will excluse the elements of artSchools

print 'flat =', flat

flat.sort()##sorts alphabeticaly 
print 'flat =', flat

flat[1] = 'UMass'##replace the first element of flat with a new value.
print 'flat =', flat

##More examples of mutating lists.
L1 = [2]
L2 = [L1, L1]
print 'L2 =', L2
L1[0] = 3
print 'L2 =', L2
L2[0] = 'a'
print 'L2 =', L2

L1 = [2] ##even with this, L2 will still print ['a', [3]] because it still points to an unchanged list.
print 'L2 =', L2 
L2 = L1

def copyList(LSource, LDest):
    for e in LSource:
        LDest.append(e)
        print 'LDest =', LDest

L1 = []
L2 = [1,2,3]
copyList(L2,L1)
print L1
print L2
##copyList(L1,L1)##this creates an alias. copyList will continuously append the same object creating an endless loop.
##print L1

##For dicts(dictionaries), the keys can be any immutable type. Set of <key:value> paires.
D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
print D['pi']
D1 = D
print D1
print D1[1]
D[1] = 'uno'
print D1
for k in D1.keys():
    print k, '=', D1[k]

##Another dictionary example. English to French. (dicts are sets not sequences so they do not print in order)
EtoF = {'bread': 'du pain', 'wine': 'du vin',
        'eats': 'mange', 'drinks': 'bois',
        'likes': 'aime', 1: 'un',
        '6.00':'6.00'}
print EtoF
print EtoF.keys()
del EtoF[1]
print EtoF

##Basic translation with a dictionary.
def translateWord(word, dictionary): ##looks for a key in the dictionary. Returns the key if found. 
    if word in dictionary:
        return dictionary[word]
    else:
        return word ##otherwise it just returns the word

def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ':
            word = word + c ##find strings of characters between spaces and assemble them into words
        else:
            translation = translation + ' ' + translateWord(word, EtoF) ##once a space is reached, translate word, then add to translation.
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF) ##assumes last word has no space after it.

print 'John eats bread =', translate('John eats bread')
print 'Steve drinks wine =', translate('Steve drinks wine')
print 'John likes 6.00 =', translate('John likes 6.00')
