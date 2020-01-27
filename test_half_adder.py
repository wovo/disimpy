"""disimpy: digital circuit simulator in Python
"""     

import disimpy as ds
  
def xhalf_adder( lib ):
   c = ds.circuit( lib, "half adder" )
   a = c.input( "a" )
   b = c.input( "b" )
   sum = c.f_xor( a, b )
   carry = c.f_and( a, b )
   c.output( sum, "sum" )      
   c.output( carry, "carry" ) 
   return c   
   
lib = ds.libs.gates() 
   
def half_adder( a, b ):
   return ds.circuit( 
     sum = lib.f_xor( a, b ), 
     carry = lib.f_and( a, b ) 
   )   
      
def full_adder( ax, b, cin ):
   one = half_adder( ax, b )
   two = half_adder( one.sum, cin )
   return ds.circuit(
      sum = two.sum,
      carry = lib.f_or( one.carry, two.carry )
   )
   
def selector( s, a, b ):
   sa = lib.f_and( s, a )
   sb = lib.f_and( lib.f_not( s ), b )
   return ds.circuit(
      result = lib.f_or( sa, sb )
   )   
   
a = ds.input( "a" )
b = ds.input( "b" )
x = half_adder( a, b )

print( ds.truth_table( selector ) )

                    
      
      
