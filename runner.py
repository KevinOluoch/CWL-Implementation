#!/usr/bin/env python3

import os
import sys
import yaml
import ast
import subprocess

import parser

'''
from ruamel.yaml import YAML
yaml=YAML()
'''

template = "./Template.yml"
cwl_file = sys.argv[1]


with open( template, 'r' ) as clt_template:
  print( 'The CWL Template' )
  cltool_template = yaml.load(clt_template)
print(cltool_template)

with open( cwl_file, 'r' ) as clt:
  print( 'The Command Line Tool')
  cltool = yaml.load(clt)
print(cltool)


parser_exit_code = parser.cltool_parser (cltool_template, cltool)
print ('Parser Exit Code')
print (parser_exit_code)


# Creat the system command
# Add the baseCommand if it is given


if not parser_exit_code:
  if 'baseCommand' in cltool.keys():
    command = [cltool['baseCommand']]
  else:
    command = []

# Get the inputs from the command line
if len (sys.argv) > 2:
  print ('arguments: ' + str( sys.argv ))
  inputs = sys.argv[2:]
  print ('inputs : ' + str( inputs ) )





# inputBinding fuction
def str_is_int( i ):
  try:
    int(i)
    return True
  except:
    return False

def separate( prefix, value, boolean ):
  if boolean == 'true':
    return [ prefix, ' ', value ]
  elif boolean == 'false':
    return [ prefix + str( value ) ]
  else:
    raise ValueError( "'separate' should be either ture of false" )

def prefix( prefix_value, value, field_dict):
  if 'separate' in iptbdg_dict.keys():
    return separate( field_dict[ 'prefix' ], input_value, 
                     field_dict[ 'separate' ] )
  else:
    return [field_dict['prefix' ], ' ', input_value ]

def inputbinding( input_value, data_type, field_dict ):
  if data_type == 'boolean' and ( input_value == ( 'true' or 'false' ) ):
    if ( 'prefix' in field_dict.keys() ) and input_value == 'false':
      cmd_value = [ field_dict[ 'prefix' ] ]
    else:
      cmd_value = None
  
  elif data_type == 'string' and isinstance( input_value, str ):
    if 'prefix' in field_dict.keys():
      cmd_value = prefix( field_dict[ 'prefix' ], 
                          input_value, 
                          field_dict )
    else:
      cmd_value = [ input_value ] 
  elif data_type == 'int' and ( isinstance( input_value, int ) or
                              ( isinstance( input_value, str ) and
                                str_is_int( input_value ) ) ):
    if 'prefix' in field_dict.keys():
      cmd_value = prefix( field_dict[ 'prefix' ], input_value, field_dict )
    
  elif data_type == 'File' and os.path.isfile ( input_value ): 
    if 'prefix' in field_dict.keys():
      cmd_value = prefix( field_dict[ 'prefix' ], 
                          input_value, 
                          field_dict )
    else:
      cmd_value = [ input_value ] 
  elif data_type == 'null':
    cmd_value = None
  elif data_type == 'array':
    raise TypeError ( "'array' not yet supported" )
  elif data_type == 'object':
    raise TypeError ( "'object' not yet supported" )
  else:
    raise ValueError ( "%s should be a %s" %(input_value, data_type) )

  return cmd_value




# Use the inputs to create a command
  inputs_list = []
  for argmt in inputs:
    if argmt[:2] == '--':
      key_values = argmt.split('=')
      print('key_values' + str( key_values ) )
      if key_values[0][2:] in cltool[ 'inputs' ].keys():
        # Create a list of command line inputs
        if isinstance( key_values[0][2:], dict ):
          input_desc = cltool['inputs'][key_values[0][2:]]
          if 'type' in input_desc.keys():
            print( "input_desc[ 'type' ] > %s"  %(input_desc[ 'type' ]) )
            command_inputs = inputbinding( key_values[1], 
                                           input_desc[ 'type' ], 
                                           input_desc[ 'inputBinding' ] )
          else:
            raise ValueError ( "%s missing 'type'" %( key_values[0][2:] ) )

        inputs_list.append( key_values[0][2:] )
        # Create a list that will execute the command 
        command.append( key_values[1] )  
        print ('key_values[0][2:] ' + str( key_values[0][2:] ) )
        print ( command )
    else:
      # Raise Error: a non existend input has been described on the comman
      # command line
      raise ValueError ( 'Unknown input %s' %(argmt) )

# Ensure all the inputs are given
for cltool_input in cltool[ 'inputs' ].keys():
  if cltool_input in inputs_list:
    continue
  else:
    raise ValueError ( 'Missing required input : %s' %( cltool_input ))

# Execute the command
print ( '$ ' + subprocess.list2cmdline( command ) )
subprocess.call( command )

