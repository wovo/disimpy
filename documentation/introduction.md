<a name="toc-anchor-0"></a>

# Disimpy introduction

Disimpy is a Python library for the definition
and simulation of digital circuits.

[pdf version](https://gitprint.com/wovo/disimpy/blob/master/documentation/introduction.md)

*****************************************************************************

<a name="toc-anchor-1"></a>

## Content

<!-- update table_of_contents( input, 3 ) -->

  - [Disimpy introduction](#toc-anchor-0)

    - [1. Combinatorial circuits](#toc-anchor-1)

    - [2. Built-in operators and functions](#toc-anchor-2)

<!-- update end -->

<!-- update example_path( "sources/introduction.py" ) -->

*****************************************************************************

<a name="toc-anchor-1"></a>

## 1. Combinatorial circuits

In dimspy a circuit is created by a function that takes the inputs
of the circuit as parameters, and returns the output(s) of the circuit.
Such a *circuit function* does not *calculate* the output,
instead it *creates (and returns) a circuit*.
That circuit can be used to calculate the output for a given
set of input values.

Circuit functions for the basic gates (or, and, xor, not) are available 
as overloads of the bitwise logic operators (&,|,^,~).
These functions operate on a single wires (single logical value, 0 or 1).

In this my_nand_gate() function the created circuit consists of two
basic gates, an *and* and a *not*, and 
the created circuit calculates the *nand* function.

<!-- update quote( input, "", "''my_nand_gate''" ) -->
~~~Python
def my_nand_gate( a, b ):
    return ~ ( a & b )
~~~

To test a circuit function, it must first be used to create a circuit.
For the my_nand_gate() function this creates a circuit that has two 
inputs named a and b, and a single output.
The input values of this circuit can be assigned a value
by assigning to the attributes, or
by calling the set method with keyword parameters.
When the inputs are set, the output value can be retrived by a value() call.

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

A circuit function can accept multiple input wires
as a Python sequence. 

This my_nor_gate() circuit function uses reduce() to apply 
the or operator | to all elements of the sequence, 
and applying the not operator ~ to the result.
Reduce requires a function (not an operator) as its first parameter, so 
a lambda is used to create a function from the | operator.

<!-- update quote( input, "", "''my_nor_gate''" ) -->
~~~Python
def my_nor_gate( port ):
    return ~ reduce( lambda a, b : a | b, port )
~~~	
   
When such a function is used, either to create a circuit
or in a call to truth_table(), the number 
of inputs in the port must be specified. 
This can be done via a keyword parameter to the circuit() 
or truth_table() function calls, with the same name as the port.

<!-- update quote( input, "", "''my_nor_gate test 1''" ) -->
~~~Python
my_nor_circuit = disimpy.circuit( my_nor_gate, inputs = 3 )    
print( disimpy.truth_table( my_nor_gate, inputs = 3 ))
~~~

The truth_table function can also be called with a circuit
(instead of a circuit function).

<!-- update quote( input, "", "''my_nor_gate test 2''" ) -->
~~~Python
print( disimpy.truth_table( my_nor_circuit ))
~~~
    
A circuit function can be used as a building block 
for functions that create more complex circuits. 

The xor is available as a basic gate, 
but it could be defined as the classic xor-from-nands,
using the my_nand_gate() circuit function as building block.

<!-- update quote( input, "", "''my_xor_gate 1''" ) -->
~~~Python
def my_xor_gate( a, b ):
    return my_nand_gate( 
        my_nand_gate( a, my_nand_gate( a, b ) )
        my_nand_gate( b, my_nand_gate( a, b ) )
    )    
~~~

This uses five calls to my_nands_gate(),
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
with each of the wires in a sequence.

This my_nand_for_port_and_wire() function uses list comprehension 
to apply a to each of the wires in b, and return the result as a list.

<!-- update quote( input, "", "''my_nand_for_port_and_wire 2''" ) -->
~~~Python
def my_nand_for_port_and_wire( a, b ):
    return [ ~ ( x & b ) for x in a ]    
~~~

Another usefull pattern is to apply an logic gate to two 
same-length sequences of wires, yielding a sequence of the gate outputs 's 
for pairs of wires from the two input sequences.

This my_xor_for_two_ports() function compares two 
(presumably same-length) sequences of wires, 
and produces a list of the xor's of the pairs of wires.

<!-- update quote( input, "", "''my_xor_for_two_ports 2''" ) -->
~~~Python
def my_xor_for_two_ports( a, b ):
    return [ x ^ y for x, y in zip( a, b ) ]
~~~

A circuit that has named outputs is called a bus. 
It is created by a call to the bus function.
The outputs are available as attributes of the bus.

This half-adder() circuit function  has two input wires, 
and two named outputs *sum* and *carry*.

<!-- update quote( input, "", "''half_adder''" ) -->
~~~Python
def half_adder( a, b ):
    return disimpy.bus(
       sum = a ^ b
       carry = a & b 
    )
~~~	

This full_adder() circuit uses two half-adders to create a full adder. 
It has three equivalent inputs (it doesn't matter which is used
as normal input or carry), and two named outputs *sum* and *carry*.

<!-- update quote( input, "", "''full_adder''" ) -->
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

<a name="toc-anchor-2"></a>

## 2. Built-in operators and functions
       
The disimpy built-in logical operators (&,|,^,~) 
work for single wires only, and have only the 'true output' form 
(| is *or*, if *nor* must be created from ~ and |).

The disimpy basic logic functions are available in true and inverted
versions, and more flexible in the inputs that are accepted.

The disimpy and, nand, or, nor, xor and xnor functions
can operate on:
   - two wires, returning a wire
   - one sequence of wires, returning a wire
   - two sequences of wires of the same length, 
        returning a sequence of wires of that same length
   - a bus and a wire, returning a byus with the same attributes
   - two busses with the same attributes, 
        returning a bus with those same attributes
		
The not function can operate on
   - a single wire, returning a single wire
   - a sequence of wires,
     returning a sequence of wires of that same length
   - a bus, returning a bus with the same attributes
   
For an xor with more than two inputs the 'odd parity' definition is used.
(The alternative that is sometimes used is the 'exactly one' definition.)

- truth_table()
- circuit()
- bus()

