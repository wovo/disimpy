"""disimpy: digital circuit simulator in Python
"""     

import disimpy as ds

def my_xor( lib, a, b ):
   nand = lib.f_nand
   x = nand( a, b )
   y = nand( x, a )
   z = nand( x, b )
   return nand( y, z ) 
      
t1 = ds.libs.nand()
t = ds.libs.gates()
c = ds.circuit( t, "a single gate circuit" )
x = c.input( "x" )
y = c.input( "y" )
z = my_xor( c.lib, x, y )
c.output( z, "z" )

print( c.truth_table() )
print( c.statistics() )

 
      
      
