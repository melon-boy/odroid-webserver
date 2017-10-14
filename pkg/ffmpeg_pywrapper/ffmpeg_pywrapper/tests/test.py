#!/usr/bin/python

from unittest import TestCase, main

from ffmpeg_pywrapper.ffprobe import FFProbe

import pkg_resources


class TestFFProbe(TestCase):
    '''
    Unit test for FFProbe output
    '''
    VIDEO_FILE = pkg_resources.resource_filename('ffmpeg_pywrapper', 'res/test.mp4')
    
    def test_print_formats(self):
        
        ff = FFProbe(self.VIDEO_FILE)
        
        filename = str(ff.get_format_filename())
        self.assertTrue(filename)
        
        duration = str(ff.get_format_duration())
        self.assertTrue(duration)
        
        format_name = str(ff.get_format_format_name())
        self.assertTrue(format_name)
        
        start_time = str(ff.get_format_start_time())
        self.assertTrue(start_time)
        
        size = str(ff.get_format_size())
        self.assertTrue(size)
        
        bit_rate = str(ff.get_format_bit_rate())
        self.assertTrue(bit_rate)
        
        print('-------------------------------------------------')
        print('- Test 1: video file formats                    -')
        print('-------------------------------------------------')
        print('File name: ' + str(filename))
        print('Duration (seconds): ' + str(duration))
        print('Format: ' + str(format_name))
        print('Start time (seconds): ' + str(start_time))
        print('File Size (Kb): ' + str(size))
        print('Bit rate (Kb/s): ' + str(bit_rate))
        print('-------------------------------------------------')
        print('- End of Test 1.                                -')
        print('-------------------------------------------------')
        
        print('-------------------------------------------------')
        print('- Test 2: ffprobe command line execution        -')
        print('-------------------------------------------------')
        
        
        
    def test_command_line_execution(self):
        
        ff = FFProbe(self.VIDEO_FILE)
        
        options = '-v error -show_entries format'
        print('Arguments : ' + str(options))
        res = ff.command_line_execution(options)
        print('Output: ' + str(res))
        print('-------------------------------------------------')
        print('- End of Test 2.                                -')
        print('-------------------------------------------------')
        
if __name__ == '__main__':
    main()
        

