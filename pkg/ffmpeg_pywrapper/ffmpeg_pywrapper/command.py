#!/usr/bin/python

'''
Command class. Use subprocess to launch
and get results back.
'''

from subprocess import check_output


class Command(object):
    '''
    Command class definition
    '''
    
    def execute(self, command, options, save_output):
        '''
        Launch command line
        '''
        cmd_line = options.split(' ')
        
        if len(cmd_line) > 0:
            
            cmd_line.insert(0, command)
        else:
            cmd_line.append(command)
            cmd_line.append(options)
        
        try:
            out = check_output(cmd_line)
        
            if save_output:
                return str(out)
        
        except OSError:
            raise FileNotFoundException('OSError: File not found exception!')          
        
        

class FileNotFoundException(Exception):
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)        
        