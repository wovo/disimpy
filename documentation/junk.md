*****************************************************************************

<a name="toc-anchor-4"></a>

## 1.4 Circuits with feedback

A combinatorial circuit can defined from just logical gates.
For a circuit that has feedback the feedback connections
must first be created by one or more feedback() calls, 
which makes them available for use as inputs.
When its value can be expressed is must be connected
to the feedback.

This circuit function creates the classic two-nor set-reset latch.

~~~Python
def sr( s, r ):
   q, q_ = feedback( 2 )
   q_.connect( s, q )
   q.connect( r, q_ )
   return named( q = q, q_ = q_ )
   
x = circuit( sr() )
sr.s = 0
sr.r = 1
sr.
~~~
   
A circuit like this that has state (memory) can't be
characterized by a truth table. 
Instead 

   dut = circuit( sr )
  


~~~Python
def and( a, b = None )
   if b != None:
      return a & b
   else:
      return reduce( lambda a, b : a & b, p )
   
c = circuit( nand_of_port, p = port( 3 ) )   
~~~

a simple ALU
- or 

~~~Python
def selective_or( n : port, m : port ):
~~~

~~~Python
def xor( 
   a : , 
   b : 
) -> disimpy.connection:
    if is_wire( a ) & is_wire( b ):
       return x ^ b
    elif is_port( a ) & is_port( b ):
       return disimpy.port( [ a ^ b for a, b in zip( a, b ) ] )
    else:
       raise "operands not compatible"  
~~~
   
~~~Python   
import collections
def is_port( x )
   return 
      isinstance( x, collections.Sequence ) \
      and is_instance( x[ 0 ], disimpy.wire )

def my_xor( a, b ):
    if is_wire( a ) and is_wire( b ):
       return x ^ b
    elif is_port( a ) and is_port( b ):
       if len( a ) != len( b ):
          raise "operands must be the same length"
       return [ a ^ b for a, b in zip( a, b ) ]
    else:
       raise "operands must be compatible"        
~~~

Library design sequence:
- idea
- write implementation
- try it to write code
- document it

~~~Python
def ripple_adder( port1, port2, cin ):
   result = []
   for a, b in zip( port1, port2 ):
      stage = full_adder( a, b, cin )
      result.append( stage.sum )
      cin = stage.carry
   return bus( sum = result, carry = cin )   
   
def equal( port1, port2 );
   return nand( xor( port1, port2 ))
   
def larger( port1, port2 ):
   result = []
   for a, b in reverse( zip( port1, port2 )):
         

def decode( port, n = None, port_ = None ):
    """decoder
    
    This circuit function can be used in two ways:
    
       decode( port ) 
       
       decodes the port into a port of 2 \** len( port )
       lines, of which at any time only the n-th line is 1
       (the others are 0), where n is the binary value
       of the input port
       
       decode( port, n )
       
       decodes the port into a single wire, which is 1 if
       and only if the binary value of the port is n.
       
       decode( port, n, _port )
       
       _port must be the bitwise ~ of port. 
       decodes the port into a single wire like decode( port, n ),
       but uses less gates because the inverse of the port bits
       is supplied by the caller.
    """
    
    if n == None:
        if port_ == None:
           return decode( port, n, ~ port_ )
        else:   
           return [ 
              decode( bus, n, bus_ ) 
                 for n in range( 0, 2 ** len( bus )) ]
    else:    
        return and( [
           port[ i ] if ( n & 1 << i ) else port_[ i ]
              for i in range( 0, len( bus ) ] )
 
def ram( a 
 for x in decode( address ) 
 
def sr( set, reset ):
   return bus( q =, q_ = )

def latch( enable, data ):
   return sr( 
      set = enable & data,
      reset = enable & ~ data
   )   
   
def register( clock, data ):
   return latch( 
      clock = ~ clock, 
      data = latch( clock, data ).q )
~~~