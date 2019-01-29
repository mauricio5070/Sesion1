In [1]:  def anagrama(x):
   ...:     y= x.copy()
   ...:     y.reverse()
   ...:     if x==y:
   ...:         print ('Es un anagrama')
   ...:     else:
   ...:         print('No es un anagrama')
   ...:

In [2]: A=['A','N','A']

In [3]: anagrama(A)
Es un anagrama

In [4]: B=['P','E','R','R','O']

In [5]: anagrama(B)
No es un anagrama

In [6]: C=[1,1,1]

In [7]: D=[1,2,3]


In [8]: anagrama(C)
Es un anagrama

In [9]: anagrama(D)
No es un anagrama
