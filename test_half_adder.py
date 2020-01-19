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
   
lib = ds.libs.gates 
   
def half_adder( a, b ):
   return ds.circuit( 
     sum = lib.f_xor( a, b ), 
     carry = lib.f_and( a, b ) 
   )   
      
def full_adder( a, b, cin ):
   one = half_adder( a, b )
   two = half_adder( a.sum, cin )
   return ds.circuit(
      sum = two.sum,
      carry = lib.f_or( one.sum, two.sum )
   )   
   
x = half_adder( 0, 0 )   

#print( c.truth_table() )
#print( c.statistics() )

import inspect

def g():
   caller = inspect.currentframe().f_back
   print( "g" )
   print( caller.f_lineno )
   print( caller.f_locals )
   print( caller.f_code.co_name )
   print( caller.f_code.co_names )
   print( caller.f_code.co_varnames )
   print( caller.f_code.co_argcount )
   
class bla:
   def __init__( self, x ):
      self.x = x   
      #g()
      
   def f( self, a, b = 5 ):
      g()   
   
def f( f, b, c = 5, d = 9 ):
   e = 9
   g()

#f( 1, 2, 3 )
#x = bla( 5 )
#x.f( 7 )

 
      
      
