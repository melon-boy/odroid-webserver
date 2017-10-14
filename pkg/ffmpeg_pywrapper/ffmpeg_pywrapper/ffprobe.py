#!/usr/bin/python

'''
Wrapper for FFProbe command.
Parse the result of < ffprobe -v error -show_format -show_streams input.mp4 >
and generates user-friendly outputs. 
Properties can be accessed individually.

Example:

from ffmpeg_pywrapper.ffprobe import FFProbe

def main(self):
		
	ff = FFProbe('input.mp4')
	print('Duration in seconds: ' + str(ff.get_duration())

if __name__ == "__main__":
	main()
	
'''


from command import Command, FileNotFoundException

class FFprobe(Command) :
	'''
	FFProbe class definition.
	Class extends from Command class.
	'''
	
	__FORMATS = dict({
		'FILENAME':'filename',
		'NB_STREAMS':'nb_streams',
		'NB_PROGRAMS':'nb_programs',
		'FORMAT_NAME':'format_name',
		'FORMAT_LONG_NAME':'format_long_name',
		'START_TIME':'start_time',
		'DURATION':'duration',
		'SIZE':'size',
		'BIT_RATE':'bit_rate',
		'PROBE_SCORE':'probe_score'
		})
	
	__VIDEO_STREAMS = dict({
		'INDEX':'index',
		'CODEC_NAME':'codec_name',
		'CODEC_LONG_NAME':'codec_long_name',
		'PROFILE':'profile',
		'CODEC_TYPE':'codec_type',
		'CODEC_TIME_BASE':'codec_time_base',
		'CODEC_TAG_STRING':'codec_tag_string',
		'CODEC_TAG':'codec_tag',
		'WIDTH':'width',
		'HEIGHT':'height',
		'HAS_B_FRAMES':'has_b_frames',
		'SAMPLE_ASPECT_RATIO':'sample_aspect_ratio',
		'DISPLAY_ASPECT_RATIO':'display_aspect_ratio',
		'PIX_FMT':'pix_fmt',
		'LEVEL':'level',
		'COLOR_RANGE':'color_range',
		'COLOR_SPACE':'color_space',
		'COLOR_TRANSFER':'color_transfer',
		'COLOR_PRIMARIES':'color_primaries',
		'CHROMA_LOCATION':'chroma_location',
		'TIMECODE':'timecode',
		'REFS':'refs',
		'IS_AVC':'is_avc',
		'NAL_LENGTH_SIZE':'nal_length_size',
		'ID':'id',
		'R_FRAME_RATE':'r_frame_rate',
		'AVG_FRAME_RATE':'avg_frame_rate',
		'TIME_BASE':'time_base',
		'START_PTS':'start_pts',
		'START_TIME':'start_time',
		'DURATION_TS':'duration_ts',
		'DURATION':'duration',
		'BIT_RATE':'bit_rate',
		'MAX_BIT_RATE':'max_bit_rate',
		'BITS_PER_RAW_SAMPLE':'bits_per_raw_sample',
		'NB_FRAMES':'nb_frames',
		'NB_READ_FRAMES':'nb_read_frames',
		'NB_READ_PACKETS':'nb_read_packets'
		})

	__AUDIO_STREAMS = dict({
		'INDEX':'index',
		'CODEC_NAME':'codec_name',
		'CODEC_LONG_NAME':'codec_long_name',
		'PROFILE':'profile',
		'CODEC_TYPE':'codec_type',
		'CODEC_TIME_BASE':'codec_time_base',
		'CODEC_TAG_STRING':'codec_tag_string',
		'CODEC_TAG':'codec_tag',
		'SAMPLE_FMT':'sample_fmt',
		'SAMPLE_RATE':'sample_rate',
		'CHANNELS':'channels',
		'CHANNEL_LAYOUT':'channel_layout',
		'BITS_PER_SAMPLE':'bits_per_sample',
		'ID':'id',
		'R_FRAME_RATE':'r_frame_rate',
		'AVG_FRAME_RATE':'avg_frame_rate',
		'TIME_BASE':'time_base',
		'START_PTS':'start_pts',
		'START_TIME':'start_time',
		'DURATION_TS':'duration_ts',
		'DURATION':'duration',
		'BIT_RATE':'bit_rate',
		'MAX_BIT_RATE':'max_bit_rate',
		'BITS_PER_RAW_SAMPLE':'bits_per_raw_sample',
		'NB_FRAMES':'nb_frames',
		'NB_READ_FRAMES':'nb_read_frames',
		'NB_READ_PACKETS':'nb_read_packets'
		})
	
	
	def __init__(self, video_file):	
		'''
		Constructor
		'''
		
		# Initialize private variables
		self.command = 'ffprobe'
		self.file = video_file

	def get_entry_formats(self):	
		'''
		Return __FORMATS dictionary
		'''
	
		return self.__FORMATS

	def get_entry_video_streams(self):
		'''
		Return __VIDEO_STREAMS dictionary
		'''
		
		return self.__VIDEO_STREAMS
	
	def get_entry_audio_streams(self):
		'''
		Return __AUDIO_STREAMS dictionary
		'''
		
		return self.__AUDIO_STREAMS
	
	def get_available_entries(self):
		'''
		Return list of available entries from ffprobe command
		'''
		availables = []
		
		# Formats
		dict = self.__FORMATS
		for k in list(dict.keys()):
			availables.append(dict[k]	 + " : " + "get_format_" + dict[k] + "()")
			
		# Video streams
		dict = self.__VIDEO_STREAMS
		for k in list(dict.keys()):
			availables.append(dict[k]	 + " : " + "get_video_stream_" + dict[k] + "()")
			
		# Audio streams
		dict = self.__AUDIO_STREAMS
		for k in list(dict.keys()):
			availables.append(dict[k]	 + " : " + "get_audio_stream_" + dict[k] + "()")
			
		return availables

	# FORMAT METHODS	
		
	def get_format_nb_streams(self):
		'''
		Return format nb_streams
		'''
		return self.__get_format(self.__FORMATS['NB_STREAMS'])


	def get_format_start_time(self):
		'''
		Return format start_time
		'''
		return self.__get_format(self.__FORMATS['START_TIME'])


	def get_format_format_long_name(self):
		'''
		Return format format_long_name
		'''
		return self.__get_format(self.__FORMATS['FORMAT_LONG_NAME'])


	def get_format_format_name(self):
		'''
		Return format format_name
		'''
		return self.__get_format(self.__FORMATS['FORMAT_NAME'])


	def get_format_filename(self):
		'''
		Return format filename
		'''
		return self.__get_format(self.__FORMATS['FILENAME'])


	def get_format_bit_rate(self):
		'''
		Return format bit_rate
		'''
		return self.__get_format(self.__FORMATS['BIT_RATE'])


	def get_format_nb_programs(self):
		'''
		Return format nb_programs
		'''
		return self.__get_format(self.__FORMATS['NB_PROGRAMS'])


	def get_format_duration(self):
		'''
		Return format duration
		'''
		return self.__get_format(self.__FORMATS['DURATION'])


	def get_format_probe_score(self):
		'''
		Return format probe_score
		'''
		return self.__get_format(self.__FORMATS['PROBE_SCORE'])


	def get_format_size(self):
		'''
		Return format size
		'''
		return self.__get_format(self.__FORMATS['SIZE'])
	
	# VIDEO STREAM METHODS
	
	def get_video_stream_pix_fmt(self):
		'''
		Return format pix_fmt
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['PIX_FMT'])


	def get_video_stream_index(self):
		'''
		Return format index
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['INDEX'])


	def get_video_stream_chroma_location(self):
		'''
		Return format chroma_location
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CHROMA_LOCATION'])


	def get_video_stream_color_range(self):
		'''
		Return format color_range
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['COLOR_RANGE'])


	def get_video_stream_color_space(self):
		'''
		Return format color_space
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['COLOR_SPACE'])


	def get_video_stream_r_frame_rate(self):
		'''
		Return format r_frame_rate
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['R_FRAME_RATE'])


	def get_video_stream_time_base(self):
		'''
		Return format time_base
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['TIME_BASE'])


	def get_video_stream_width(self):
		'''
		Return format width
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['WIDTH'])


	def get_video_stream_duration_ts(self):
		'''
		Return format duration_ts
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['DURATION_TS'])


	def get_video_stream_display_aspect_ratio(self):
		'''
		Return format display_aspect_ratio
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['DISPLAY_ASPECT_RATIO'])


	def get_video_stream_codec_tag(self):
		'''
		Return format codec_tag
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_TAG'])


	def get_video_stream_duration(self):
		'''
		Return format duration
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['DURATION'])


	def get_video_stream_bits_per_raw_sample(self):
		'''
		Return format bits_per_raw_sample
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['BITS_PER_RAW_SAMPLE'])


	def get_video_stream_nb_frames(self):
		'''
		Return format nb_frames
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['NB_FRAMES'])


	def get_video_stream_nal_length_size(self):
		'''
		Return format nal_length_size
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['NAL_LENGTH_SIZE'])


	def get_video_stream_avg_frame_rate(self):
		'''
		Return format avg_frame_rate
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['AVG_FRAME_RATE'])


	def get_video_stream_start_time(self):
		'''
		Return format start_time
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['START_TIME'])


	def get_video_stream_codec_type(self):
		'''
		Return format codec_type
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_TYPE'])


	def get_video_stream_has_b_frames(self):
		'''
		Return format has_b_frames
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['HAS_B_FRAMES'])


	def get_video_stream_bit_rate(self):
		'''
		Return format bit_rate
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['BIT_RATE'])


	def get_video_stream_sample_aspect_ratio(self):
		'''
		Return format sample_aspect_ratio
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['SAMPLE_ASPECT_RATIO'])


	def get_video_stream_nb_read_packets(self):
		'''
		Return format nb_read_packets
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['NB_READ_PACKETS'])


	def get_video_stream_codec_time_base(self):
		'''
		Return format codec_time_base
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_TIME_BASE'])


	def get_video_stream_color_primaries(self):
		'''
		Return format color_primaries
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['COLOR_PRIMARIES'])


	def get_video_stream_level(self):
		'''
		Return format level
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['LEVEL'])


	def get_video_stream_refs(self):
		'''
		Return format refs
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['REFS'])


	def get_video_stream_codec_tag_string(self):
		'''
		Return format codec_tag_string
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_TAG_STRING'])


	def get_video_stream_height(self):
		'''
		Return format height
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['HEIGHT'])


	def get_video_stream_timecode(self):
		'''
		Return format timecode
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['TIMECODE'])


	def get_video_stream_id(self):
		'''
		Return format id
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['ID'])


	def get_video_stream_profile(self):
		'''
		Return format profile
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['PROFILE'])


	def get_video_stream_nb_read_frames(self):
		'''
		Return format nb_read_frames
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['NB_READ_FRAMES'])


	def get_video_stream_color_transfer(self):
		'''
		Return format color_transfer
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['COLOR_TRANSFER'])


	def get_video_stream_start_pts(self):
		'''
		Return format start_pts
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['START_PTS'])


	def get_video_stream_max_bit_rate(self):
		'''
		Return format max_bit_rate
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['MAX_BIT_RATE'])


	def get_video_stream_codec_long_name(self):
		'''
		Return format codec_long_name
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_LONG_NAME'])


	def get_video_stream_codec_name(self):
		'''
		Return format codec_name
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['CODEC_NAME'])


	def get_video_stream_is_avc(self):
		'''
		Return format is_avc
		'''
		return self.__get_stream_for_video(self.__VIDEO_STREAMS['IS_AVC'])
	
	# AUDIO STREAM METHODS
	
	def get_audio_stream_index(self):
		'''
		Return format index
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['INDEX'])


	def get_audio_stream_codec_name(self):
		'''
		Return format codec_name
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_NAME'])


	def get_audio_stream_max_bit_rate(self):
		'''
		Return format max_bit_rate
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['MAX_BIT_RATE'])


	def get_audio_stream_channel_layout(self):
		'''
		Return format channel_layout
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CHANNEL_LAYOUT'])


	def get_audio_stream_r_frame_rate(self):
		'''
		Return format r_frame_rate
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['R_FRAME_RATE'])


	def get_audio_stream_time_base(self):
		'''
		Return format time_base
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['TIME_BASE'])


	def get_audio_stream_codec_tag_string(self):
		'''
		Return format codec_tag_string
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_TAG_STRING'])


	def get_audio_stream_channels(self):
		'''
		Return format channels
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CHANNELS'])


	def get_audio_stream_duration_ts(self):
		'''
		Return format duration_ts
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['DURATION_TS'])


	def get_audio_stream_codec_tag(self):
		'''
		Return format codec_tag
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_TAG'])


	def get_audio_stream_duration(self):
		'''
		Return format duration
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['DURATION'])


	def get_audio_stream_codec_type(self):
		'''
		Return format codec_type
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_TYPE'])


	def get_audio_stream_nb_frames(self):
		'''
		Return format nb_frames
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['NB_FRAMES'])


	def get_audio_stream_id(self):
		'''
		Return format id
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['ID'])


	def get_audio_stream_profile(self):
		'''
		Return format profile
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['PROFILE'])


	def get_audio_stream_nb_read_frames(self):
		'''
		Return format nb_read_frames
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['NB_READ_FRAMES'])


	def get_audio_stream_sample_fmt(self):
		'''
		Return format sample_fmt
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['SAMPLE_FMT'])


	def get_audio_stream_avg_frame_rate(self):
		'''
		Return format avg_frame_rate
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['AVG_FRAME_RATE'])


	def get_audio_stream_start_pts(self):
		'''
		Return format start_pts
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['START_PTS'])


	def get_audio_stream_start_time(self):
		'''
		Return format start_time
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['START_TIME'])


	def get_audio_stream_bits_per_raw_sample(self):
		'''
		Return format bits_per_raw_sample
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['BITS_PER_RAW_SAMPLE'])


	def get_audio_stream_bit_rate(self):
		'''
		Return format bit_rate
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['BIT_RATE'])


	def get_audio_stream_sample_rate(self):
		'''
		Return format sample_rate
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['SAMPLE_RATE'])


	def get_audio_stream_bits_per_sample(self):
		'''
		Return format bits_per_sample
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['BITS_PER_SAMPLE'])


	def get_audio_stream_codec_long_name(self):
		'''
		Return format codec_long_name
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_LONG_NAME'])


	def get_audio_stream_nb_read_packets(self):
		'''
		Return format nb_read_packets
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['NB_READ_PACKETS'])


	def get_audio_stream_codec_time_base(self):
		'''
		Return format codec_time_base
		'''
		return self.__get_stream_for_audio(self.__AUDIO_STREAMS['CODEC_TIME_BASE'])
	
	# COMMAND LINE METHOD
	
	def command_line_execution(self, options):
		'''
		This function is the raw command line ffprobe wrapper.
		Options variable is not parsed, ffprobe will return an error message if it is not 
		built properly. 
		Return ffprobe command output.
		'''
		try:
			result = self.execute(self.command, options + ' ' + self.file, True)
		
		except (FileNotFoundException):
			print('Error: ' + self.file + ' command not found') 
			
		return result
		
	
	# PRIVATE METHODS
	
	def __get_format(self, format_name):
		'''
		Private function that returns video info from format section.
		'''
		options = '-v error -show_entries format=' + format_name + ' -of default=noprint_wrappers=1:nokey=1' + ' ' + self.file
		
		try:
			result = self.execute(self.command, options, True)
		
		except (FileNotFoundException):
			print('Error: ' + self.file + ' command not found') 
			
		return result
	
	def __get_stream_for_video(self, stream_name):
		'''
		Private function that returns video info from stream section.
		'''
		options = '-v error -select_streams v:0 -show_entries stream=' + stream_name + ' -of default=noprint_wrappers=1:nokey=1' + ' ' + self.file
		
		try:
			result = self.execute(self.command, options, True)
		
		except (FileNotFoundException):
			print('Error: ' + self.file + ' command not found') 
			
		return result
	
	def __get_stream_for_audio(self, stream_name):
		'''
		Private function that returns video info from stream section.
		'''
		options = '-v error -select_streams v:1 -show_entries stream=' + stream_name + ' -of default=noprint_wrappers=1:nokey=1' + ' ' + self.file
		
		try:
			result = self.execute(self.command, options, True)
		
		except (FileNotFoundException):
			print('Error: ' + self.file + ' command not found') 
			
		return result
		
		
def main():
	'''
	Prints available entries from formats, video stream and/or audio stream.
	'''
	ff = FFprobe(None)
	
	print("-------------------------------------------------")
	print("- Available entry formats	- Getter method	   	   ")
	print("-------------------------------------------------")
	formats = ff.get_entry_formats()
	for k in list(formats.keys()):
		print(formats[k]	 + " : " + "get_format_" + formats[k] + "()")
	print("-------------------------------------------------")
	print("- Available video stream entries - Getter Method ")
	print("-------------------------------------------------")
	video_streams = ff.get_entry_video_streams()
	for k in list(video_streams.keys()):
		print(video_streams[k] + " : " + "get_video_stream_" + video_streams[k] + "()")	
	print("-------------------------------------------------")
	print("- Available audio stream entries - Getter Method ")
	print("-------------------------------------------------")
	audio_streams = ff.get_entry_audio_streams()
	for k in list(audio_streams.keys()):
		print(audio_streams[k] + " : " + "get_audio_stream_" + audio_streams[k] + "()")	
		
	print("_________________________________________________")
	print("For entries definitions see ffprobe command doc at")
	print("<a href=\"https://ffmpeg.org/ffprobe.html\">ffprobe Documentarion</a>")
	
if __name__ == '__main__':
	main()
