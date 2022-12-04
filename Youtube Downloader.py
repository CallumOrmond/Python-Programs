import pytube

link = input("Paste Link Here - ")
print("Downloading...")

pytube.YouTube(link).streams.first().download(output_path=r"C:\Users\callu\Pictures")
print("Video Download Done!")