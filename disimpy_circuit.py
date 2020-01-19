"""disimpy: digital circuit simulator in Python
"""     

import inspect
import disimpy_base as base

class _circuit_class:
   """implementation of a digital circuit 
   """
   
   def __init__( self, name ):
      self.name = name[ : ]
      self.inputs = {}
      self.outputs = {}
      
   def add_input( self, name ):
      r = base.input( name )
      if name in self.inputs:
         raise "duplicate input name [%s]" % name
      if name in self.outputs:
         raise "input name [%s] already used as output" % name
      self.inputs[ name ] = r
      return r      

   def add_output( self, source, name ):   
      r = base.output( source, name )
      if name in self.outputs:
         raise "duplicate output name [%s]" % name
      if name in self.inputs:
         raise "output name [%s] already used as input" % name         
      self.outputs[ name ] = r
      return r         
      
   def truth_table( self ):
      s = ""
      for x in self.inputs:
         s += "%s " % self.inputs[ x ].name
      for x in self.outputs:
         s += "%s " % self.outputs[ x ].name
      for v in range( 0, 2 ** len( self.inputs ), 1 ):
         s += "\n"   
         for x in self.inputs:
            b = v & ( 1 << len( self.inputs ) - 1 )
            self.inputs[ x ].set( b != 0 )
            s += "%s " % ( "1" if self.inputs[ x ].value() else "0" )
            v = 2 * v
         for x in self.outputs:
            s += "%s " % ( "1" if self.outputs[ x ].value() else "0" )
      return s   
      
   def statistics( self ):
      s = ""
      if self.name != "":
         s += "\ncircuit name    : %s" % self.name
      s += "\ncircuit inputs  : %d" % len( self.inputs )
      s += "\ncircuit outputs : %d" % len( self.outputs )
      return s

      
def circuit( *kwargs ):
   caller = inspect.currentframe().f_back
   result = _circuit_class( caller.f_code.co_name )
   
   for n in range( 0, caller.f_code.co_argcount ):
      name = caller.f_code.co_varnames[ n ]
      if name != "self":
         print( "in", name )
   
   for arg in kwargs:
      print( "out", arg )
      
   print( "====" )
   print( caller.f_lineno )
   print( caller.f_locals )
   print( caller.f_code.co_name )
   print( caller.f_code.co_names )
   print( caller.f_code.co_varnames )
   print( caller.f_code.co_argcount )