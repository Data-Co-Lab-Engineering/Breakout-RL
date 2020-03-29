import glob
import io
from IPython.display import HTML
from IPython import display as ipythondisplay
import base64

def show_video():
	mp4list = glob.glob('video/*.mp4')
	if len(mp4list) > 0:
		mp4 = mp4list[0]
		video = io.open(mp4, 'r+b').read()
		encoded = base64.b64encode(video)
		decoded = encoded.decode('ascii')
		ipythondisplay.display(HTML(data='''<video alt="test" autoplay 
								loop controls style="height: 400px;">
								<source src="data:video/mp4;base64,{0}" type="video/mp4" />
						 </video>'''.format(decoded)))

	else: 
		print("Could not find video")