<a name="toc-anchor-0"></a>

# 1 disimpy introduction

Disimpy is a Python library for the definition
and simulation of digital circuits.

[pdf version](https://gitprint.com/wovo/blob/master/disimpy/documentation/introduction.md)

*****************************************************************************

<a name="toc-anchor-1"></a>

## 1.1 Content

<!-- update table_of_contents( input, 2 ) -->

  - [1 disimpy introduction](#toc-anchor-0)

    - [1.1 Content](#toc-anchor-1)
      [1.2 Combinatorial circuits](#toc-anchor-2)
      [1.3 Built-in operators and functions](#toc-anchor-3)
      [1.4 Circuits with feedback](#toc-anchor-4)

<!-- update end -->

<!-- update example_path( "sources/introduction.py" ) -->

*****************************************************************************

<a name="toc-anchor-2"></a>

## 1.2 Combinatorial circuits

In dimspy a circuit is created by a function that takes the inputs
of the circuit as parameters, and returns the output(s) of the circuit.
Such a *circuit function* does not *calculate* the output,
instead it *creates (and returns) a circuit* that can calculate the output.

Circuit functions for the basic gates (or, and, xor, not) are available 
as overloads of the bitwise logic operators (&,|,^,~).
These functions operate on a single wires.

In this my_nand_gate function the created a circuit consists of two
basic gates, an *and* and a *not*, and 
the circuit calculates the *nand* function.

<!-- update quote( input, "", "''my_nand_gate''" ) -->
~~~Python
def my_nand_gate( a, b ):
    return ~ ( a & b )
~~~

To test a circuit function, it must first be used to create a circuit.
For the my_nand_gate function this creates a circuit that has two 
inputs named a and b, and a single output.
You can assign values to the inputs, and retrieve the result.
Inputs can be set by assigning to the attributes, or
by calling the set method with keyword parameters.

<!-- update quote( input, "", "''my_nand_gate test''" ) -->
~~~Python
my_nand_circuit = disimpy.circuit( my_nand_gate )

my_nand_circuit.a, my_nand_circuit.b = 0, 1
print( "nand( 0, 1 ) =>", c.value() )

my_nand_circuit.set( a = 1, b = 1 )
print( "nand( 1, 1 ) =>", c.value() )
~~~
<<>>

The function truth_table() returns a table that shows the output(s)
of a circuit function for all possible inputs.

<!-- update quote( input, "", "''my_nand_gate truth table''" ) -->
~~~Python
print( disimpy.truth_table( my_nand_gate ))
~~~
<<>>

A circuit function for a gate with multiple inputs 
can get its inputs as a sequence. 

This my_nor_gate example circuit function is realized by using reduce() to apply 
the or operator | to all elements of the list, 
and applying the not operator ~ to the result.
Reduce requires a function (not an operator) as its first parameter, so 
a lambda is used to create a function from the | operator.

<!-- update quote( input, "", "''my_nor_gate''" ) -->
~~~Python
def my_nor_gate( port ):
    return ~ reduce( lambda a, b : a | b, port )
~~~	
   
When such a function is used to create a circuit
or to in a call to truth_table, the number 
of inputs in the input port must be specified. 
This can be done via a keyword parameter to the circuit function
with the same name as the port.
The truth_table function can also be called with a circuit
(instead of a circuit function).

<!-- update quote( input, "", "''my_nor_gate test''" ) -->
~~~Python
my_nor_circuit = disimpy.circuit( 
    my_nor, 
    inputs = 3
)    
print( disimpy.truth_table( my_nor ), inputs = 3 )
print( disimpy.truth_table( my_nor_circuit ))
~~~
    
A circuit function can be used as a building block 
for functions that create more complex circuits. 

The xor is available as a basic gate, 
but it could be defined as the classic xor-from-nands,
using the my_nand_gate function as building block.

<!-- update quote( input, "", "''my_xor_gate 1''" ) -->
~~~Python
def my_xor_gate( a, b ):
    return my_nand_gate( 
        my_nand_gate( a, my_nand_gate( a, b ) )
        my_nand_gate( b, my_nand_gate( a, b ) )
    )    
~~~

This uses five calls to my_nands_gate,
because the expression my_nand_gate( a, b ) is used twice.
To prevent this, a local variable can be used 
to re-use the output of the sub-circuit my_nand_gate( a, b ).

<!-- update quote( input, "", "''my_xor_gate 2''" ) -->
~~~Python
def my_xor_gate( a, b ):
    nand_ab = my_nand_gate( a, b )
    return my_nand_gate( 
       my_nand_gate( a, nand_ab )
       my_nand_gate( b, nand_ab )
    )        
~~~	
    
It can be useful to combine a single wire
with each of the wires in the sequence.
This function applies a to each of the wires in b, 
and returns the results as a sequence.

~~~Python
def my_nand_for_port_and_wire( a, b ):
    return [ ~ ( x & b ) for x in a ]    
~~~

A logic gate can also be applied to two same-length sequences of wires, 
yielding a sequence of the xor's of pairs of wires 
from the two input sequences.

~~~Python
def my_xor_for_two_ports( a, b ):
    return [ x ^ y for x, y in zip( a, b ) ]
~~~

A circuit that has named outputs can be represented by an
object with the outputs as attributes. 

~~~Python
def half_adder( a, b ):
   r = object()
   r.sum = a ^ b
   r.carry = a & b
   return r
~~~
   
The disimpy.bus function can be used to create such an object.

~~~Python   
def full_adder( a, b, c ):
   ab = half_adder( a, b )
   abc = half_adder( ab.sum, c )
   return disimpy.bus(
       sum = abc.sum, 
       carry = ab.carry | abc.carry 
   )    
~~~

*****************************************************************************

<a name="toc-anchor-3"></a>

## 1.3 Built-in operators and functions
       
The disimpy built-in logical operators work for single wires only.

The logic functions are more flexible.
The disimpy and, nand, or, nor, xor and xnor functions
can operate on:
   - two wires, returning a wire
   - one sequence of wires, returning a wire
   - two sequences of wires of the same length, 
        returning a sequence of wires of that same length
   - a dictionary and a wire, returning a dictionary
   - two busses with the same attributes, 
        returning a port with those same attributes
The not function can operate on
   - a single wire
   - a sequence of wires
   - a bus
   
For an xor with more than two inputs the 'odd parity' definition is used.
(The alternative that is sometimes used is the 'exactly one' definition.)

- truth_table()
- circuit()
- bus()

*****************************************************************************

<a name="toc-anchor-4"></a>

## 1.4 Circuits with feedback

A combinatorial circuit can defined from just logical gates.
For a circuit that has feedback the feedback connections
must first be created by one or more feedback() calls, 
which makes them available for use as inputs.
When their value can be expressed is must be connected
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