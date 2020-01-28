"""sources for the introduction.md
"""

# update quote ''my_nand_gate'' 2
def my_nand_gate( a, b ):
    return ~ ( a & b )
    
# update quote ''my_nand_gate test'' 7
my_nand_circuit = disimpy.circuit( my_nand_gate )

my_nand_circuit.a, my_nand_circuit.b = 0, 1
print( "nand( 0, 1 ) =>", c.value() )

my_nand_circuit.set( a = 1, b = 1 )
print( "nand( 1, 1 ) =>", c.value() )

# update quote ''my_nand_gate truth table'' 1
print( disimpy.truth_table( my_nand_gate ))

# update quote ''my_nor_gate'' 2
def my_nor_gate( port ):
    return ~ reduce( lambda a, b : a | b, port )
    
# update quote ''my_nor_gate test 1'' 2
my_nor_circuit = disimpy.circuit( my_nor_gate, inputs = 3 )    
print( disimpy.truth_table( my_nor_gate, inputs = 3 ))

# update quote ''my_nor_gate test 2'' 1
print( disimpy.truth_table( my_nor_circuit ))

# update quote ''my_xor_gate 1'' 5
def my_xor_gate( a, b ):
    return my_nand_gate( 
        my_nand_gate( a, my_nand_gate( a, b ) )
        my_nand_gate( b, my_nand_gate( a, b ) )
    )    
    
# update quote ''my_xor_gate 2'' 6
def my_xor_gate( a, b ):
    nand_ab = my_nand_gate( a, b )
    return my_nand_gate( 
       my_nand_gate( a, nand_ab )
       my_nand_gate( b, nand_ab )
    )        
    
# update quote ''my_nand_for_port_and_wire 2'' 2
def my_nand_for_port_and_wire( a, b ):
    return [ ~ ( x & b ) for x in a ]    

# update quote ''my_xor_for_two_ports 2'' 2
def my_xor_for_two_ports( a, b ):
    return [ x ^ y for x, y in zip( a, b ) ]

# update quote ''half_adder'' 5
def half_adder( a, b ):
    return disimpy.bus(
       sum = a ^ b
       carry = a & b 
    )

# update quote ''full_adder'' 7
def full_adder( a, b, c ):
    ab = half_adder( a, b )
    abc = half_adder( ab.sum, c )
    return disimpy.bus(
        sum = abc.sum, 
        carry = ab.carry | abc.carry 
    )    


