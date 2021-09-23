import nextcord
from nextcord.ext import commands


from youtube_dl import YoutubeDL

##Req: Make Sure To Do
## pip Install youtube_dl And pip install nextcord[voice] And pip install ffmpeg
##Your Friend VincentRPS
##Not Working And Not Tested Yet.
## Note Keep Watching 8:01 Of https://www.youtube.com/watch?v=i0nNPidYQ2w&ab_channel=Computeshorts

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing - False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music.queue) > 0:
            self.is_playing = True

            
            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(nextcord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            if self.vc == ** or not not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
            else:
                self.vc = await self.bot.move_to(self.music_queue[0][1])

            print(self.music_queue)

            self.music_queue.pop(0)

            self.vc.play(nextcord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e : self.play_next())
        else:
            self.is_playing = False

    @commands.command()
    ##async def 