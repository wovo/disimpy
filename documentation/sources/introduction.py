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
    
# update quote ''my_nor_gate test'' 3
my_nor_circuit = disimpy.circuit( my_nor, inputs = 3 )    
print( disimpy.truth_table( my_nor_circuit ))
print( disimpy.truth_table( my_nor, inputs = 3 ))

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
    



