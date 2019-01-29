  def anagrama(x):
        y= x.copy()
        y.reverse()
        if x==y:
            print ('Es un anagrama')
        else:
            print('No es un anagrama')
   

A=['A','N','A']

anagrama(A)
Es un anagrama

B=['P','E','R','R','O']

anagrama(B)
No es un anagrama

C=[1,1,1]

D=[1,2,3]


anagrama(C)
Es un anagrama

anagrama(D)
No es un anagrama
