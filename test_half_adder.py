"""disimpy: digital circuit simulator in Python
"""     

import disimpy as ds

  
def half_adder( lib ):
   c = ds.circuit( lib, "half adder" )
   a = c.input( "a" )
   b = c.input( "b" )
   sum = c.f_xor( a, b )
   carry = c.f_and( a, b )
   c.output( sum, "sum" )      
   c.output( carry, "carry" ) 
   return c   
      
c = my_half_adder( ds.libs.gates )

print( c.truth_table() )
print( c.statistics() )

 
      
      
