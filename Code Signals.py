
# coding: utf-8

# In[2]:


a = [1, 2, 2]
b = [2, 1, 1]
if sorted(a) == sorted(b):
    print("true")
else:
    gg = {}
    hh = {}
    for i in list(set(a)):
        gg.update( {i : a.count(i)} )
    for j in list(set(b)):
        hh.update({ j : b.count(j)} )
        if gg == hh:
            print("true")
        else:
            print("false")


# In[3]:


def ss(z):
    a = []
    b = []
    for i in range(0,len(z)+1,2):
        a.append(z[i])


# In[4]:


def evenDigitsOnly(n):
    a = []
    n = str(n)
    for i in n:
        if int(i) % 2 == 0:
            a.append(i)
    if len(a) == len(n):
        return True
    else:
        return False  


# In[5]:


def variableName(name):
    import string
    invalidChars = set(string.punctuation.replace("_", " "))
    if any(char in invalidChars for char in name) or name[0].isdigit():
        return False
    else:
        return True


# In[6]:


def alphabeticShift(inputString):
    import string
    a = []
    b = list(string.ascii_lowercase)
    for i in inputString:
        if b.index(i)+1 == 26:
            a.append(b[0])
        else:
            a.append(b[b.index(i)+1])
    return ''.join(a)   


# In[8]:


def chessBoardCellColor(cell1, cell2):
    c1a = list(cell1)[0]
    c1b = int(list(cell1)[1])
    c2a = list(cell2)[0]
    c2b  = int(list(cell2)[1])
    dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    if (((dic[c1a] + c1b) % 2 == 0) and ((dic[c2a] + c2b) % 2 == 0)) or (((dic[c1a] + c1b) % 2 != 0) and ((dic[c2a] + c2b) % 2 != 0)):
        return True
    else:
        return False


# In[9]:


def circleOfNumbers(n, firstNumber):
    a = range(int(n/2),n)
    da = dict(list(enumerate(a)))
    db = {v: k for k, v in da.items()}
    da.update(db)
    return da[firstNumber]


# In[10]:


def firstDigit(inputString):
    a = list(s)
    for i in range(len(a)):
        if a[i].isdigit() == True:
            print(a[i])
            break


# In[11]:


def growingPlant(u, d, h):
    c = 0
    if u >= h:
        return 1
    else:
        while c*(u-d) <= h:
            c += 1
            if h - (c*(u-d)) <= u:
                return c + 1


# In[12]:


def arrayReplace(a, e, s):
    for n, i in enumerate(a):
        if i == e:
            a[n] = s
    return a


# In[13]:


def isTandemRepeat(s):
    return s[:int(len(s)/2)] == s[int(len(s)/2):]


# In[14]:


def isCaseInsensitivePalindrome(s):
    return s[:].lower() == s[::-1].lower()


# In[15]:


def houseNumbersSum(inputArray):
    return sum(inputArray[:inputArray.index(0)])


# In[16]:


def allLongestStrings(a):
    return [a[i] for i in range(len(a)) if len(a[i]) == max([len(a[i]) for i in range(len(a))])]


# In[17]:


def reflectString(inputString):
    s = ''.join([chr(i) for i in range(97,123)])
    d = dict(zip(s, s[::-1]))
    return ''.join([d.get(i) for i in inputString])

