
# Check for errors in the syntax
def cltool_parser (cltool_template, cltool):

  repeatition = []
  for field, argmt in cltool.items():

    # Check if a field has been repeated
    if field in repeatition:
      raise NameError ('There are two or more fields named %s' %(field))
    else:
      repeatition.append(field)

    # Check if all the field are valid and take appropriate action if they 
    # are
    if field == 'inputs':
      if isinstance(argmt, dict):
        pass # IMPLEMENT
      elif isinstance(argmt, str) and argmt == '[]':
        pass
      else:
        raise ValueError( '''
inputs field must have subfield of commandlinetool 
inputs or be an empty tuple '[]'; value given is %s''' %( argmt ) )

    if field == 'outputs':
      if isinstance(argmt, dict):
        pass # IMPLEMENT
      elif isinstance(argmt, str) and argmt == '[]':
        pass
      else:
        raise ValueError( '''
outputs field must have subfield of commandlinetool 
outputs or be an empty tuple '[]'; value given is %s''' %( argmt ) )

    if field == 'class':
      if argmt == 'CommandLineTool':
        pass
      else:
        raise ValueError( 'class must be CommandLineTool; value given is %s' %( argmt ) )

    if field == 'id':
      if isinstance( argmt, str):
        pass
      else:
        raise ValueError( 'id must be a string') #;'value given is %s' %( argmt ) )

    if field == 'requirements':
      if isinstance(argmt, dict):
        pass
      else:
        raise ValueError( 'requiments must be given as subfields' )

    if field == 'hints':
      if isinstance(argmt, dict):
        pass
      else:
        raise ValueError( 'hints must be given as subfields' )

    if field == 'label':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'label must be a string' )

    if field == 'doc':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'doc must be a str' )

    if field == 'cwlVersion':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'doc must be a str; current supported version is "v1.0"' )

    if field == 'baseCommand':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'baseCommand must be a str' )

    if field == 'arguments':
      if isinstance(argmt, dict):
        pass # IMPLEMENT
      else:
        raise ValueError( '''
arguments field must have subfields ''')
 
    if field == 'stdin':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'stdin must be a str' )

    if field == 'stderr':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'stderr must be a str' )

    if field == 'stdout':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'stdout must be a str' )

    if field == 'successCodes':
      if isinstance(argmt, int):
        pass
      else:
        raise ValueError( 'successCodes must be a int' )

    if field == 'temporaryFailCodes':
      if isinstance(argmt, int):
        pass
      else:
        raise ValueError( 'temporaryFailCodes must be a int' )

    if field == 'permanentFailCodes':
      if isinstance(argmt, str):
        pass
      else:
        raise ValueError( 'permanentFailCodes must be a int' )

  return 0

