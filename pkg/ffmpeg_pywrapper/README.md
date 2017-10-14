# The FFmpeg Python Wrapper



This FFmpeg wrapper intends to be a flexible user-friendly wrapper. FFMpeg libraries have to be installed previously. You can download them from [FFmpeg](https://www.ffmpeg.org).
The wrapper is based on the subprocess python base class to handle commands execution.



### Table of content

- [Installation](##Installation)
- [Examples](##Examples)



## Installation 


**ffmpeg_pywrapper** can be installed from one of the following methods:

### From PIP:
```
$>pip install ffmpeg_pywrapper
```

### From Pypi.python.org:

* Download package from [ffmpeg_pywrapper](http://pypi.python.org/ffmpeg_pywrapper).
* Uncompress it:
	
		$>tar zxvf ffmpeg_pywrapper-x.x.x.tar.gz
		
* Install:

		$>cd ffmpeg_pywrapper
		$>python setup.py install

## Examples

The following examples execute **ffmpeg** or **ffprobe** command synchonously. 

### Example 1: retrieve of a ffprobe entry

	>>> from ffmpeg_pywrapper.ffprobe import FFprobe
	>>> ff = FFprobe('input.mp4')
	>>> print 'Duration (seconds): ' + str(ff.get_format_duration())

### Example 2: show all available entries from ffprobe

	>>> from ffmpeg_pywrapper.ffprobe import FFprobe
	>>> ff = FFprobe(None)
	>>> entries = ff.get_available_entries()
	>>> print entries
	
Every list element printed is composed by two strings separated by	two dots. The first one is the **ffprobe** entry, the second one is the wrapper function associated with the entry. See example 1 for the duration entry format.
	
### Example 3: convert video

	>>> from ffmpeg_pywrapper.ffmpeg import FFmpeg
	>>> ff = FFmpeg('input.flv')
	>>> ff.convert_to('output.mp4')

Output format is calculated from from output file extension. So, in that case, the **FLV** video is going to be converted to an **MP4** video.

### Example 4: convert video and audio

The use is the same as such of example 3. In adition, video codec and/or audio could be specified.

	>>> from ffmpeg_pywrapper.ffmpeg import FFmpeg
	>>> ff = FFmpeg('input.flv')
	>>> ff.convert_to('output.mp4', 'h264', 'aac)
	
That example converts the **FLV** container format to a specific video an audio codec passed as argument. In that case, we are going to convert video from **flv1** codec to **mp4** codec and audio from **mp3** codec to **aac** codec respectively.


### Example 4: split video into three chunks

	>>> from ffmpeg_pywrapper.ffmpeg import FFmpeg
	>>> ff = FFmpeg('input.flv')
	>>> ff.split(3)
	
The **ff.split(3)** call is going to create three parts of **input.flv** file automatically:
 
* part01.flv
* part02.flv
* part03.flv

The **split** method is going to calculate the every chunk duration from the total stream duration. So:

	chunk_duration = stream_duration / n_chunks

### Example 5: merge three video chunks

Now, we could want to concatenate the three parts obtained from the exmaple 4. That can be realized by the next piece of code:

	>>> from ffmpeg_pywrapper.ffmpeg import FFmpeg
	>>> ff = FFmpeg(None)
	>>> parts = ['part01.flv', 'part02.flv', 'part03.flv']
	>>> output = 'concatenate.flv'
	>>> ff.concatenate(parts, output)
	
Note that we can retrive the splitted files with the next command too:

	>>> parts = sorted(fnmatch.filter(os.listdir('.'), 'part*.flv'))

Such command is going to return a list with all files found into the actual directory ('.') that pass the filter. That means the files begin per **part** and finishes per **.flv**: **['part01.flv', 'part02.flv', 'part03.flv']**

### Example 6: use of 'ffmpeg' wrapper as a command line

A command line method is been created to allow the developer the flexibility on to **ffmpeg** command. That method is used right this:

	>>> from ffmpeg_pywrapper.ffmpeg import FFmpeg
	>>> ff = FFmpeg(None)
	>>> options = '-v quiet -y -i input.flv -vcode h264 -acodec copy output.mp4'
	>>> ff.command_line_execution(options)

**options** can be anything you could pass to **ffmpeg** command.

