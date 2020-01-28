"""disimpy: digital circuit simulator in Python
"""     

import disimpy_base as base

class g_not( base.node ):      

   def __init__( self, input ):
      self.input = input

   def value( self ) -> bool:
      return not self.input[ 0 ].value()

class g_and( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      r = True
      for x in self.inputs:
         r = r and x.value()
      return r

class g_nand( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      r = True
      for x in self.inputs:
         r = r and x.value()
      return not r

class g_or( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      r = False
      for x in self.inputs:
         r = r or x.value()
      return r

class g_nor( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      r = False
      for x in self.inputs:
         r = r or x.value()
      return not r

class g_xor( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      n = 0
      for x in self.inputs:
         n += 1 if x.value() else 0
      return n == 1

class g_xnor( base.node ):      

   def __init__( self, inputs ):
      self.inputs = inputs[ : ]

   def value( self ) -> bool:
      n = 0
      for x in self.inputs:
         n += 1 if x.value() else 0
      return n != 1

