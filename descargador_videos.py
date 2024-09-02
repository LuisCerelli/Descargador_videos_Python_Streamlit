import pytube
import streamlit as st

class YoutubeDownloader:
     def __init__(self, url):
          self.url = url
          self.youtube = pytube.Youtube(self.url, on_progress_callback=YoutubeDownloader.onProgress)
          self.stream = None