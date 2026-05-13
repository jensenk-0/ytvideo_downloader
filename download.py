from pytubefix import YouTube


def downloader(link, path):
    
    
    yt = YouTube(link)
    
    main_video = yt.streams.get_highest_resolution()

    main_video.download(path)




