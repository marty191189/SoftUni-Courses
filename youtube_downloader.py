from pytube import YouTube


def download_func(link_1):

    youtube_obj = YouTube(link_1)
    youtube_obj = youtube_obj.streams.get_highest_resolution()

    try:
        youtube_obj.download()
        print("Successful download!")

    except:
        print("Download failed!")

link = input("Please put your Youtube link here: ")

download_func(link)
