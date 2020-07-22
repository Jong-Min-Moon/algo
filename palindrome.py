class queue():
    def __init__(self):
        self.contents = []
    
    def enqueue(self, x):
        self.contents.append(x)
    
    def dequeue(self):
        x = self.contents.pop(0)
        print(x, 'out,', self.contents, 'left')
        return x
    
class stack():
    def __init__(self):
        self.contents = []
    
    def push(self, x):
        self.contents.append(x)
    
    def pop(self):
        x = self.contents.pop()
        print(x, 'out,', self.contents, 'left')
        return x   

a = queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.contents)

a.dequeue()
a.dequeue()
a.dequeue()
a.dequeue()


b = stack()
b.push(1)
b.push(2)
b.push(3)
b.push(4)
print(b.contents)

b.pop()
b.pop()
b.pop()
b.pop()



def pldr(s):
    qu = queue()
    st = stack()

    #enqueue and push
    for achar in s:
        if achar.isalpha():
            qu.enqueue(achar.lower())
            st.push(achar.lower())
    print(qu.contents, st.contents)
    #dequeue and pop.
    while qu.contents:
        if qu.dequeue() != st.pop():
            return False

    return True

print(pldr('Wow'))
print(pldr("Madam, I'm Adam."))
print(pldr("Madam, I am Adam."))
