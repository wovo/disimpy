

# update quote ''my_nand_gate'' 2
def my_nand_gate( a, b ):
    return ~ ( a & b )
    
# update quote ''my_nand_gate test'' 5
my_nand_circuit = disimpy.circuit( my_nand_gate )
my_nand_circuit.a, my_nand_circuit.b = 0, 1
print( "nand( 0, 1 ) =>", c.value() )
my_nand_circuit.a, my_nand_circuit.b = 1, 1
print( "nand( 1, 1 ) =>", c.value() )

# update quote ''my_nand_gate truth table'' 1
print( disimpy.truth_table( my_nand_gate ))