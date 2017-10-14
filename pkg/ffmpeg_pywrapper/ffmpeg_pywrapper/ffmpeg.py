#!/usr/bin/python

'''
ffmpeg command wrapper.
'''


from command import Command, FileNotFoundException
from ffprobe import FFprobe

from decimal import Decimal
import os, time, tempfile
import logging

class FFmpeg(Command) :
	'''
	FFmpeg class definition.
	Class extends from Command class.
	'''
	
	FAST = 'fast'
	ULTRAFAST = 'ultrafast'
	
	def __init__(self, video_file):	
		'''
		Constructor
		'''
		
		# Initialize private variables
		self.command = 'ffmpeg'
		self.file = video_file
		self.preset = None
		self.name = 'ffmpeg'
		self.level = logging.DEBUG
		
		# logging initialize
		self.__init_logging()
		
		
	# COMMAND LINE METHOD
	
	def command_line_execution(self, options):
		'''
		This function is the raw command line ffprobe wrapper.
		Options variable is not parsed, ffprobe will return an error message if it is not 
		built properly. 
		Return ffprobe command output.
		'''
		try:
			result = self.execute(self.command, options, True)
		
		except (FileNotFoundException):
			logging.error('Error: ' + self.file + ' command not found') 
			
		return result
	


	# CONVERT VIDEO AND/OR AUDIO

	def convert_to(self, output, video_codec=None, audio_codec=None):
		'''
		Convert video stream into 'video_codec' and audio stream into 'audio_codec'.
		If 'audio_codec' is not supplied, audio_codec will be copied.
		If 'video_codec' is not supplied, video_codec will be automatic detected from output file extension.
		Output file will be created into the same directory.
		Note: not all containers accept all audio codecs!!!
		'''
		if output is None:
			return None
		
		options = ''
		preset_print = ''
		
		if self.preset is not None:
			# check for preset setting
			preset = ' -preset ' + self.preset
			preset_print = self.preset
		else:
			preset = ''
			preset_print = ''
		
		if video_codec is None and audio_codec is None:
			# direct ouput
			options = '-v quiet -y -i ' + self.file + preset + ' ' + output
			video_codec = 'by output extension'
			audio_codec = 'by output extension'
		else:
			# complex filter command
			if video_codec is None:
				video_codec = 'copy'
				
			if audio_codec is None:
				audio_codec = 'copy'
				
			options = '-v quiet -y -i ' + self.file + ' -acodec ' + audio_codec + \
				' -vcodec ' + video_codec + preset + ' ' + output
				
		logging.debug('Input: ' + self.file)
		logging.debug('Output: ' + output)
		logging.debug('Output Audio codec: ' + audio_codec)
		logging.debug('Output Video codec: ' + video_codec)
		logging.debug('Preset method: ' + preset_print)
		logging.debug('encoding ...')
		
		try:
			t_begin = time.time()
			result = self.execute(self.command, options, True)
			t_end = time.time()
			logging.debug('... encoding done in ' + '{0:.2f}'.format(t_end-t_begin) + ' s.')
			
		except (FileNotFoundException):
			logging.error('Error: ' + self.file + ' command not found') 
			
		return result

	# SPLIT VIDEO INTO CHUNKS.

	def split(self, n_chunks, output=None):
		'''
		Split video file into n_chunks. Audio and audio are copied. 
		'''
		# get stream duration to calculate time chunks
		ff = FFprobe(self.file)
		stream_duration = ff.get_format_duration()
		
		# calculate time chunks
		n_chunks = int(n_chunks)
		
		if n_chunks == 1:
			chunk_duration = int(round(Decimal(stream_duration)))
		else:
			chunk_duration = int(round(Decimal(stream_duration) / Decimal(n_chunks)))
		
		rest = Decimal(stream_duration) - Decimal(chunk_duration*n_chunks)
		
		if Decimal(rest) > 0 and Decimal(rest) < 1: # if milliseconds are going to be missed, then we recalculate chunk_duration
			chunk_duration = int(round((Decimal(stream_duration) + 1) / Decimal(n_chunks)))
		
		if chunk_duration < 1: # minimum chunk duration unit 1s
			chunk_duration = 1
		
		logging.debug('Stream duration: ' + str(stream_duration).replace('\n', '') + ' s')
		logging.debug('Chunks: ' + str(n_chunks) )
		logging.debug('Chunk duration: ' + str(chunk_duration))
		
		try:
			# generate multiples outputs
			if(n_chunks > 1):
				if output is not None:
					output = self.__create_output(output)
				else:
					output = self.__create_output('part.' + self.__get_input_extension())
			
			options = '-v quiet -y -i ' + self.file + ' -acodec copy -f segment -segment_time ' \
				+ str(chunk_duration) + ' -vcodec copy -reset_timestamps 1 ' + output
			
			result = self.execute(self.command, options, True)
		
		except (FileNotFoundException):
			logging.error('Error: ' + self.file + ' command not found') 
			
		return result

	# CONCATENATE VIDEO CHUNKS.
	
	def concatenate(self, video_list, output):
		'''
		Concatenates video files from a list of path files.
		'''
		list_file = self.create_video_list_file(video_list)
		
		options = '-v quiet -y -f concat -safe 0 -i ' + list_file + ' -c copy ' + output
		
		try:
			result = self.execute(self.command, options, True)
			
			if list_file is not None:
				os.remove(list_file)
				logging.debug('Temporary file deleted: ' + list_file)
		
		except (FileNotFoundException):
			logging.error('Error: ' + self.file + ' command not found') 
			
		return result

	def create_video_list_file(self, input, output_dir=None):
		'''
		Creates 'output' file formatted for the concatenate method 
		Takes a video path files list as argument 'input'
		Example of 'input': ['/home/foo/first.mp4','/home/foo/second.mp4'] 
		Such 'input' creates a '/output_dir/video_files.txt' or '/tmp' instead wich contains:
			file '/home/foo/first.mp4'
			file '/home/foo/second.mp4'
		Finally, link to /tmp/video_files.txt is returned.
		'''
		tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
		
		logging.debug('Temporary file created: ' + tf.name)
		
		# TODO: HACK: to DEBUG!!
		dir_name = os.getcwd()
		
		for val in input:
			tf.write('file \'' + dir_name + '/' + val + '\'\n')
		tf.close()
		
		return tf.name
	
	def set_preset(self, preset):
		'''
		Set preset for video conversion. 
		'''
		self.preset = preset
	
	# PRIVATE METHODS

	def __create_output(self, output):
		'''
		Create output path file
		'''
		path_list = os.path.split(output)
		dir_name = path_list[0]
		file_name = path_list[1]
		
		if dir_name != '':
			dir_name += '/'
		
		if file_name != '':
			file_list = file_name.split('.')
			output = dir_name + file_list[0] + '%02d.' +file_list[1]
		else:
			# File not found
			raise FileNotFoundException
		
		return output
	
	def __get_input_extension(self):
		'''
		Return the string extension from the input file
		'''
		return self.file.split('.')[1]
	
	def __init_logging(self):
		'''
		Logging initialize. A file ffmpeg_wrapper.log is created in /var/log directory
		'''
		logging.basicConfig(level=self.level, \
						format='[%(levelname)s] - [' + self.name + '][%(funcName)s]: %(message)s')
	