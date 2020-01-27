"""disimpy: digital circuit simulator in Python
"""     

class node:
   """something that you can ask for its binary value
   """
   
   def value( self ) -> bool:
      raise "value() not implemented"
      
   def __enter__( self ):
      pass   
      
      
class literal( node ):
   """an literal has a fixed value
   """
   
   def __init__( self, v : bool ):
      self.name = ""
      self.v = v
      
   def value( self ):
      return self.v   
      
      
class input( node ):
   """an input gets its value from outside
   """
   
   def __init__( self, name, v = 0 ):
      self.name = name[ : ]
      self.v = v
      
   def value( self ):
      return self.v   

   def set( self, v ):
      self.v = v
      
      
class output( node ):
   """an output provides a value to the outside
   """
   
   def __init__( self, source, name ):
      self.name = name[ : ]
      self.source = source
      
   def value( self ):
      return self.source.value()
      

class toolkit:
   """a bunch of building blocks for constructing circuits
   """
   
   def __init__( self, name ):
      self.name = name[ : ]
      self.resources = {}         
      
   def add( self, name, n = 1 ):
      self.resources[ name ] = self.resources.get( name, 0 ) + n   
      
   def statistics( self ):
      s = ""
      if self.name != "":
         s += "\nfrom : %s" %  self.name
      for r in self.resources:
         s += "\n%s : %d" % ( r, self.resources[ r ] )
      return s    