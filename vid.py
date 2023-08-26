import webbrowser


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False  # before open the vid, it haven't seen

    def open(self):  # func to open every link
        webbrowser.open(self.link)
        self.seen = True  # after open the vid, it have seen, so it turn to true


class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos


def read_video():
    title = input("Enter title : ") + "\n"
    link = input("Enter link : ") + "\n"
    video = Video(title, link)
    return video


def print_video(video):
    print("Video title : ", video.title, end="")
    print("Video link : ", video.link, end="")


def read_videos():
    videos = []
    total_video = int(input("Enter how many video : "))
    for i in range(total_video):
        print("Enter video ", i + 1)
        vid = read_video()  # create a new varible to return func
        videos.append(vid)
    return videos


def print_videos(videos):
    for i in range(len(videos)):
        print("Video " + str(i + 1) + " : ")
        print_video(videos[i])  # have to call the func above ^ to print it


def write_video_txt(video, file):
    file.write(video.title)  # what is video.title role here?
    file.write(video.link)


def write_videos_txt(videos, file):
    total = len(videos)
    file.write(str(total) + "\n")
    for i in range(total):
        write_video_txt(videos[i], file)  # call out the above func


def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video


def read_videos_from_txt(file):
    videos = []
    total = file.readline()  # why?
    for i in range(int(total)):  # have to convert into int bc everything in txt file is string
        video = read_video_from_txt(
            file)  # why have to insert 'file' in here? - because call out all the func have to included its parameter
        videos.append(video)
    return videos


def read_playlist():
    playlist_name = input("Enter playlist name : ") + "\n"
    playlist_description = input("Enter playlist description : ") + "\n"
    playlist_rating = input("Enter playlist rating : ") + "\n"
    playlist_videos = read_videos()
    new_playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return new_playlist


def read_playlists():
    playlists = []
    total_playlist = int(input("Enter how many playlist : "))
    for i in range(total_playlist):
        print("Enter video ", i + 1)
        playl = read_playlist()  # create a new varible to return func
        playlists.append(playl)
    return playlists


def write_playlist_txt(playlist):
    with open("data.txt", "w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_videos_txt(playlist.videos, file)
    print("You've successfully write to the playlist")


def read_playlist_from_txt():
    with open("data.txt", "r") as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        print_videos = read_video_from_txt(file)
        playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist


def print_playlist(playlist):
    print("- - - - - -")
    print("Playlist name : " + playlist.name, end="")
    print("Playlist description : " + playlist.description, end="")
    print("Playlist rating : " + playlist.rating, end="")
    print_videos(playlist.videos)


def show_menu():
    print("- - - - - - MAIN MENU - - - - - ")
    print("| Option 1 : Create a playlist |")
    print("| Option 2 : Show playlist     |")
    print("| Option 3 : Play a video      |")
    print("| Option 4 : Add a video       |")
    print("| Option 5 : Update playlist   |")
    print("| Option 6 : Remove video      |")
    print("| Option 7 : Save and exit     |")
    print("- - - - - - - - - - - - - - - - ")


def play_video(playlist):
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range("Select a video (1 " + str(total) + ") : ", 1, total)
    print("Open video : " + playlist.videos[choice - 1].title + "--" + playlist.videos[choice - 1].link,
          end="")  # [choice-1] : because in this func, it start collect vids from 1, so choice - 1 = 0, make it start from 0 vids in the list which is 1
    webbrowser.open(playlist.videos[choice - 1].link, new=2)  # new=2 : to open the link in a new tab


def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice


def add_video(playlist):
    print("Enter new video information !")
    new_video = read_video()  # create a new variable for return value of function
    playlist.videos.append(new_video)
    return playlist


def update_playlist(playlist):
    # update name, description, rating
    print("Update my palylist !")
    print("Option 1 : Update playlist's name")
    print("Option 2 : Update playlist's description")
    print("Option 3 : Update playlist's rating")
    choice = select_in_range("Enter what you want to update (1-3) : ", 1, 3)
    if choice == 1:
        new_playlist_name = input("Enter new name for playlist : ") + "\n"
        playlist.name = new_playlist_name  # have to put playlist.name, because if only put name, then it will be undefined
        print("Updated successfully")
        return playlist
    if choice == 2:
        new_playlist_description = input("Enter new description for playlist : ") + "\n"
        playlist.description = new_playlist_description
        print("Updated successfully")
        return playlist

    if choice == 3:
        new_playlist_rating = str(select_in_range("Enter new rating for playlist (1-5) : ", 1, 5)) + "\n"
        playlist.rating = new_playlist_rating
        print("Updated successfully")
        return playlist


def remove_video(playlist):
    print_videos(playlist.videos)
    choice = select_in_range("Enter video you want to remove : ", 1,
                             len(playlist.videos))  # choice is the index of video u wanna remove
    new_video_list = []
    # del playlist.videos[choice-1]
    for i in range(len(playlist.videos)):
        if i == choice - 1:
            continue
        new_video_list.append(playlist.videos[i])
    playlist.videos = new_video_list
    return playlist


def main():
    try:
        playlist = read_playlist_from_txt()
        print("Loaded data successfully !")
    except:
        print("Welcome first user !")

    while True:  # create a loop for user to select options 1-6, every time users select one option it will return back to show menu
        show_menu()
        choice = select_in_range("Select an option (1-7) : ", 1, 7)
        if choice == 1:
            playlist = read_playlist()
            input("\nPress enter to continue\n")
        elif choice == 2:
            print_playlist(playlist)
            input("\nPress enter to continue\n")
        elif choice == 3:
            play_video(playlist)
            input("\nPress enter to continue\n")
        elif choice == 4:
            playlist = add_video(
                playlist)  # the 1st 'playlist' in this sentence is the new return after add new video into already exist playlist
            input("\nPress enter to continue\n")
        elif choice == 5:
            playlist = update_playlist(playlist)
            input("\nPress enter to continue\n")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("\nPress enter to continue\n")
        elif choice == 7:
            write_playlist_txt(playlist)
            input("\nPress enter to continue\n")
            break


main()

