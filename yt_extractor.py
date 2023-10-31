import youtube_dl
from youtube_dl.utils import DownloadError

ydl = youtube_dl.YoutubeDL()


def get_info(url):
    with ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None

    video = result["entries"][0] if "entries" in result else result
    infos = ['id', 'title', 'channel', 'view_count', 'like_count',
             'channel_id', 'duration', 'categories', 'tags']

    def key_name(key):
        return "video_id" if key == "id" else key

    return {key_name(key): video[key] for key in infos}