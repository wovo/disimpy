class circuit
   def __init__( self, name = "" ):
      self.name = name[:]

class node:
   def __init__( self, name = "" ):
      self.name = name[:]
      
class nand:      
   def __init__( self, a, b ):
      self.inputs = [ a, b ]

   def value( self ):
      r = True
      for x in self.inputs:
         r = r and x.value()
      return r   
      
      

a = input.bit()
b = input.bit()
c = ports.nand( a, b )
output.bit( c )

one
zero
fixed()

def not( a ):
   return nand( a, a )
   
def and( a, b ):
   return not( and( a, b ))

def or( a, b ):
   return( nand( not( a ), not( b ))

def nor( a, b ):
   return not( or( a, b ))

def xor( a, b ):
   x = nand( a, b )
   y = nand( x, a )
   z = nand( x, b )
   return nand( y, z )   
   
def sr( a, b )
   x = feedback()
   y = nand( a, x )
   x.attach( nand( b, y ) )
   return bus( d = x, d_ = y )
   
def half_adder( a, b, toolkit ):
   return class with toolkit as t 
      return toolkit.bus( 
         sum = t.xor( a, b ),
         carry = t.and( a, b )
      )   
      
def full_adder( a, b, c, toolkit ):
         
         
t.add( 
t += 
t = add_full_adder( t, ... )         

class node:
   """something that you can ask for its binary value
   """
   
   def value( self ) -> bool:
      raise "value() not implemented"

class nand( node ):      
   """a nand port with an unlimited number of inputs

   This port is used as a base for constructing ports in toolkits.
   """

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      r = True
      for x in self.inputs:
         r = r and x.value()
      return r
      
class toolkit:
   """a bunch of building blocks for constructing circuits
   """
   
   def __init__( self, name ):
      self.name = name[ : ]
      self.resources = {}         
      
   def add( self, name, n = 1 ):
      self.resources[ name ] = self.resources.get( name, 0 ) + n   
      
   def report( self ):
      print( name )
      for r in self.resources:
         print( r, self.resources[ r ] )

class toolkit_nand( toolkit ):
   """a toolkit with only an (unlimited inputs) nand gate
   """

   def __init__( self, name ):
      super().__init__( name )
      self.port_count = 0
      
   def nand( self, inputs ):
      self.add( "gate" )
      self.add( "nand" )
      self.add( "inputs", len( inputs ) )
      return nand( inputs )

class toolkit_nand2( toolkit ):
   """a toolkit with only a 2 input nand gate
   """

   def __init__( self, name ):
      super().__init__( name )
      self.port_count = 0
      
   def nand2( self, a, b ):
      self.add( "gate" )
      self.add( "nand2" )
      self.add( "inputs", 2 )
      return nand( [ a, b ] )
      
- toolkit met al de klassiekers als basis functies
      
- uitbreiden met and, or, nor      
- evaluate delay

t = toolkit_nand2( "my toolkit" )

t += def nor( t, a, b ): 
   return t.not( t.or( a, b ))
   
t += xor( t, a, b ):
   x = t.nand( a, b )
   y = t.nand( x, a )
   z = t.nand( x, b )
   return t.nand( y, z )    
        
bus is outside 
   
- named multiple returns   
- should be single assign...

