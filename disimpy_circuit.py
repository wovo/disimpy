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
      
class circuit:
   def __init__( self, *args, **kwargs ):
      if len( args ) != 0:
         raise "circuit must have only keyword arguments"
   
      self._outputs = {}   
      for arg in kwargs:
         setattr( self, arg, kwargs[ arg ] )
         self._outputs[ arg ] = kwargs[ arg ]
         
import inspect         
         
def truth_table( c ):
   if not inspect.isfunction( c ):
      raise "truth_table() must be called with a function"
      
   # create the list of input variables   
   sig = str( inspect.signature( c ))
   sig = sig.replace( "(", "" ).replace( ")", "" ).split( "," )
   inputs = []
   for arg in sig:
      arg = arg.split( "=" )[ 0 ].strip()
      inputs.append( arg )
      
   s = ""
   # for all input values
   for v in range( 0, 2 ** len( inputs ), 1 ):
      args = []
      s1 = ""
      
      # create the list of input literals
      for x in inputs:
         b = ( v & ( 1 << len( inputs ) - 1 )) != 0
         args.append( base.literal( b ))
         s1 += "1" if b else "0"
         s1 += " " * len( x )
         v = 2 * v
         
      # call the function with the input literals as arguments   
      result = c( *args )   
      
      # first input value?
      if not "\n" in s:
         # create the header
         for x in inputs:
            s += "%s " % x
         for x in result._outputs:
            s += "%s " % x
            
      # add the input values      
      s += "\n" + s1
      
      # add the output values
      for x in result._outputs:
         s += "1" if result._outputs[ x ].value() else "0"
         s += " " * len( x )
         
   return s         
      
