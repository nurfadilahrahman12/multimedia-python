from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

video = VideoFileClip('bcl.mp4')

short_video = video.subclip(0, 10) 
short_video.write_videofile('short_bcl_result.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_bcl_result.mp4')

reversed_video = short_video.fx(vfx.time_mirror)  
reversed_video.write_videofile('reversed_bcl_result.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('SpeedUp_bcl_result.mp4')

video.write_videofile('resultBCL.mp4')