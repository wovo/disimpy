"""disimpy: digital circuit simulator in Python
"""     

import disimpy_base  as base
import disimpy_gates as basic_gates

class nand( base.toolkit ):
   """a toolkit with only (unlimited number of inputs) nand gates
   """

   def __init__( self, name = "toolkit nand" ):
      super().__init__( name )
      
   def f_nand( self, *inputs ):
      self.add( "gate" )
      self.add( "nand" )
      self.add( "input", len( inputs ) )
      return basic_gates.g_nand( inputs )

class nand2( base.toolkit ):
   """a toolkit with only 2-input nand gates
   """

   def __init__( self, name = "toolkit nand2" ):
      super().__init__( name )
      
   def f_nand( self, a, b ):
      self.add( "gate" )
      self.add( "nand2" )
      self.add( "inputs", 2 )
      return basic_gates.g_nand( [ a, b ] )
      
class gates( base.toolkit ):
   """a toolkit with the class gates 
   """
   
   def __init__( self, name = "toolkit gates" ):
      super().__init__( name )
      
   def _make( self, name, inputs, basic ):
      self.add( "gate" )
      self.add( name )
      self.add( "input", len( inputs ) )
      return basic( inputs )
      
   def f_not( self, *inputs ):
      return self._make( "not", inputs, basic_gates.g_not )
      
   def f_nand( self, *inputs ):
      return self._make( "nand", inputs, basic_gates.g_nand )
      
   def f_and( self, *inputs ):
      return self._make( "and", inputs, basic_gates.g_and )
      
   def f_nor( self, *inputs ):
      return self._make( "nor", inputs, basic_gates.g_nor )
      
   def f_or( self, *inputs ):
      return self._make( "and", inputs, basic_gates.g_or )
      
   def f_xnor( self, *inputs ):
      return self._make( "xnor", inputs, basic_gates.g_xnor )
      
   def f_xor( self, *inputs ):
      return self._make( "xor", inputs, basic_gates.g_xor )
      
   
class gates_from( base.toolkit ):
   """a toolkit with the class gates 
   """
   
   def __init__( self, base = None, name = "" ):
      self.base = base
      if name == "":
         name = "add gates to %s " % base.name
      super().__init__( name )
      
   def f_nand( self, *inputs ):
      self.add( "gate" )
      self.add( "nand" )
      self.add( "input", len( inputs ) )
      return basic_gates.g_nand( inputs )      
      
   def __getattr__( self, item ):
      return getattr( self.base, item )