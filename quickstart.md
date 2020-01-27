disimpy is a Python library for the definition
and simulation of digital circuits.

The basic gates (or, and, xor, not) are available 
as overloads of the bitwise logic operators (&,|,^,~),
operating on single wire.

combinatorial circuits

A circuit is created by a function that takes
the inputs as parameters, and returns the output.
Such a circuit function does not *calculate* the output,
instead it creates a *circuit* that can calculate the output.

In this example the circuit consists of two
basic gates, an *and* and a *not*, and it calculates the *nand* function.

def my_nand_gate( a, b ):
    return ~ ( a & b )

To test a circuit function, it must first be used to create a circuit.
For the my_nand_gate function this creates a circuit that has two 
inputs named a and b, and a single output.
You can assign values to the inputs, and retrieve the result.

my_nand_circuit = disimpy.circuit( my_nand_gate )
my_nand_circuit.a, my_nand_circuit.b = 0, 1
print( "nand( 0, 1 ) =>", c.value() )
my_nand_circuit.a, my_nand_circuit.b = 1, 1
print( "nand( 1, 1 ) =>", c.value() )

The function truth_table() returns a table that shows the output(s)
of a circuit function for all possible inputs.

print( disimpy.truth_table( my_nand_gate ))
<<>>

A circuit function for a gate with multiple inputs 
can get its inputs as a sequence. 

In this example a nor circuit function that can handle any number of inputs 
is realized by using reduce() to apply the or operator | to all elements 
of the list, and applying the not operator ~ to the result.

import functools
def my_nor( inputs ):
    return ~ functools.reduce( lambda x, y : x | y, inputs )
   
When such a function is used to create a circuit,
or to call truth_table, the number 
of inputs in the input port must be specified. 
The truth_table function can also be called with a circuit
(instead of a circuit function).

my_nor_circuit = disimpy.circuit( 
    my_nor, 
    inputs = 3
)    
print( disimpy.truth_table( my_nor ), inputs = 3 )
print( disimpy.truth_table( my_nor_circuit ))
    
A circuit function that can be used as a building block 
for functions that create more complex circuits. 
The xor is available as a basic gate, 
but it could be defined as the classic xor-from-nands,
using the my_nand_gate function.

def my_xor_gate( a, b ):
    return my_nand_gate( 
        my_nand_gate( a, my_nand_gate( a, b ) )
        my_nand_gate( b, my_nand_gate( a, b ) )
    )      

This uses five calls to my_nands_gate,
because the expression my_nand_gate( a, b ) is used twice.
To prevent this, a local variable can be used 
to re-use the output of a sub-circuit.

def my_xor_gate( a, b ):
    nand_ab = my_nand_gate( a, b )
    return my_nand_gate( 
       my_nand_gate( a, nand_ab )
       my_nand_gate( b, nand_ab )
    )     
    
It can be useful to combine a single wire
with each of the wires in the sequence.
This function applies a to each of the wires in b, 
and returns the results as a sequence.

def my_nand_for_port_and_wire( a, b ):
    return [ ~ ( x & b ) for x in a ]    

A logic gate can also be applied to two same-length sequences of wires, 
yielding a sequence of the xor's of pairs of wires 
from the two input sequences.

def my_xor_for_two_ports( a, b ):
    return [ x ^ y for x, y in zip( a, b ) ]
    
A circuit that has named outputs can be represented by an
object with the outputs as attributes. 

def half_adder( a, b ):
   r = object()
   r.sum = a ^ b
   r.carry = a & b
   return r
   
The disimpy.bus function can be used to create such an object.

   
def full_adder( a, b, c ):
   ab = half_adder( a, b )
   abc = half_adder( ab.sum, c )
   return disimpy.bus(
       sum = abc.sum, 
       carry = ab.carry | abc.carry 
   )    
   
built-in operators and functions   
       
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

circuits with feedback

A combinatorial circuit can defined from just logical gates.
For a circuit that has feedback the feedback connections
must first be created by one or more feedback() calls, 
which makes them available for use as inputs.
When their value can be expressed is must be connected
to the feedback.

This circuit function creates the classic two-nor set-reset latch.

def sr( s, r ):
   q, q_ = feedback( 2 )
   q_.connect( s, q )
   q.connect( r, q_ )
   return named( q = q, q_ = q_ )
   
x = circuit( sr() )
sr.s = 0
sr.r = 1
sr.
   
A circuit like this that has state (memory) can't be
characterized by a truth table. 
Instead 

   dut = circuit( sr )
  


def and( a, b = None )
   if b != None:
      return a & b
   else:
      return reduce( lambda a, b : a & b, p )
   
c = circuit( nand_of_port, p = port( 3 ) )   

a simple ALU
- or 

def selective_or( n : port, m : port ):

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

Library design sequence:
- idea
- write implementation
- try it to write code
- document it