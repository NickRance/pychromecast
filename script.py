import time
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

chromecasts = pychromecast.get_chromecasts()
x = [cc.device.friendly_name for cc in chromecasts]
VIDEO_ID = "0jm8nnHqx80"
print(x)

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Beat Chromecast")
#  # Start worker thread and wait for cast device to be ready
cast.wait()
print(cast.device)
# DeviceStatus(friendly_name='Living Room', model_name='Chromecast', manufacturer='Google Inc.', uuid=UUID('df6944da-f016-4cb8-97d0-3da2ccaa380b'), cast_type='cast')

print(cast.status)
# CastStatus(is_active_input=True, is_stand_by=False, volume_level=1.0, volume_muted=False, app_id='CC1AD845', display_name='Default Media Receiver', namespaces=['urn:x-cast:com.google.cast.player.message', 'urn:x-cast:com.google.cast.media'], session_id='CCA39713-9A4F-34A6-A8BF-5D97BE7ECA5C', transport_id='web-9', status_text='')
yt = YouTubeController()
cast.register_handler(yt)
yt.play_video(VIDEO_ID)

# mc = cast.media_controller
# mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
# mc.block_until_active()
# print(mc.status)
# MediaStatus(current_time=42.458322, content_id='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type='video/mp4', duration=596.474195, stream_type='BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state='PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)

#  mc.pause()
#  time.sleep(5)
#  mc.play(