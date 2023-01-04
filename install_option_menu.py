import tkinter as tk
import subprocess
import shutil
import getpass
import os
import ctypes


def extract_compressed_file(file_path, name):
    """
    :param: file_path: file path of the specified option directory
    :param: name: the name of the folder
    """
    # Get the current user's desktop directory
    desktop_dir = "C:\\Users\\" + getpass.getuser() + "\\Desktop\\Utilities\\{0}".format(name)

    # Extract the file to the desktop
    shutil.unpack_archive(file_path, desktop_dir)


def create_folders():
    # Get the desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Create the folders
    folder_names = ["folder_name1", "folder_name2", "folder_name3"]
    for folder_name in folder_names:
        folder_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


def option8():
    extract_compressed_file(r"C:\directory\file.zip", 'folder name to create/extract to')


def option7():
    extract_compressed_file(r"C:\directory\file.zip", 'folder name to create/extract to')


def option6():
    extract_compressed_file(r"C:\directory\file.zip", 'folder name to create/extract to')


def option5():
    subprocess.run([r"C:\directory\file.msi"])


def option4():
    subprocess.run([r"C:\directory\file.exe"])


def option33():
    extract_compressed_file(r"C:\directory\file.zip", 'folder name to create/extract to')


def option3():
    subprocess.run([r"C:\directory\file.msi"])


def option2():
    subprocess.run([r"C:\directory\file.exe"])


def option1():
    subprocess.run([r"C:\directory\file.msi"])


def set_background():
    # sets the background from your specified dir to your main screen and centers it
    image_path = r"C:\directory\background.png"
    spi_setdeskwallpaper = 20
    spif_updateinifile = 1
    spif_sendwininichange = 2
    ctypes.windll.user32.SystemParametersInfoW(spi_setdeskwallpaper, 0, image_path,
                                               spif_sendwininichange | spif_updateinifile)
    key = ctypes.WinDLL("user32.dll").SystemParametersInfoW
    key(spi_setdeskwallpaper, 0, image_path, 3)


class App:

    def __init__(self, master):
        self.button6 = None
        self.button6_var = None
        self.button5 = None
        self.button5_var = None
        self.button4_var = None
        self.button33_var = None
        self.button3 = None
        self.button7_var = None
        self.button33 = None
        self.button4 = None
        self.button7 = None
        self.button3_var = None
        self.button2 = None
        self.button2_var = None
        self.button1 = None
        self.button1_var = None
        self.create_folders_button = None
        self.set_background_button = None
        self.logo = None
        self.checkmark = None
        self.button8_var = None
        self.button8 = None
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Set the window size
        self.master.geometry("250x500")

        # Create the logo
        self.logo = tk.PhotoImage(file=r"C:\Users\h2h_2\Pictures\israel.png")
        self.logo = self.logo.subsample(5)  # Resize the logo
        logo_label = tk.Label(self.master, image=self.logo)
        logo_label.pack(side="bottom")

        # Create the checkmark image
        self.checkmark = tk.PhotoImage(file=r"C:\Users\h2h_2\Pictures\checkmark.png")
        self.checkmark = self.checkmark.subsample(2)  # Resize the checkmark

        # Create the headline label
        headline = tk.Label(self.master, text="HEADLINE", font=("Calibri", 22, 'bold'))
        headline.pack()

        # Create the subheadline label
        subhead = tk.Label(self.master, text="SUBHEADLINE", font=("Calibri", 18, 'bold'))
        subhead.pack()

        # Create the frame for the buttons
        frame = tk.Frame(self.master, bd=1, relief="solid")
        frame.pack(side="top", fill="both", expand=True)

        # Create the button to set the background
        self.set_background_button = tk.Button(frame, text="Set Background", command=set_background,
                                               justify="left")
        self.set_background_button.pack(side="top", fill="both", expand=True)

        # Create the buttons

        self.create_folders_button = tk.Button(frame, text="Create Folders: \n1, 2, 3",
                                               command=create_folders,
                                               justify="center")
        # Creates three folders named from text function
        self.create_folders_button.pack(side="top", fill="both", expand=True)

        self.button1_var = tk.IntVar()
        self.button1 = tk.Checkbutton(frame, text="OPTION 0", command=option1, justify="right",
                                      variable=self.button1_var, onvalue=1, offvalue=1)
        self.button1.pack(side="top", fill="both", expand=True)

        self.button2_var = tk.IntVar()
        self.button2 = tk.Checkbutton(frame, text="OPTION 1", command=option2,
                                      justify="right",
                                      variable=self.button2_var, onvalue=1, offvalue=1)
        self.button2.pack(side="top", fill="both", expand=True)

        self.button3_var = tk.IntVar()
        self.button3 = tk.Checkbutton(frame, text="OPTION 2", command=option3, justify="right",
                                      variable=self.button3_var, onvalue=1, offvalue=1)
        self.button3.pack(side="top", fill="both", expand=True)

        self.button33_var = tk.IntVar()
        self.button33 = tk.Checkbutton(frame, text="OPTION 3", command=option33, justify="right",
                                       variable=self.button33_var, onvalue=1, offvalue=1)
        self.button33.pack(side="top", fill="both", expand=True)

        self.button4_var = tk.IntVar()
        self.button4 = tk.Checkbutton(frame, text="OPTION 4", command=option4, justify="right",
                                      variable=self.button4_var, onvalue=1, offvalue=1)
        self.button4.pack(side="top", fill="both", expand=True)

        self.button5_var = tk.IntVar()
        self.button5 = tk.Checkbutton(frame, text="OPTION 5", command=option5, justify="right",
                                      variable=self.button5_var, onvalue=1, offvalue=1)
        self.button5.pack(side="top", fill="both", expand=True)

        self.button6_var = tk.IntVar()
        self.button6 = tk.Checkbutton(frame, text="OPTION 6", command=option6, justify="right",
                                      variable=self.button6_var, onvalue=1, offvalue=1)
        self.button6.pack(side="top", fill="both", expand=True)

        self.button7_var = tk.IntVar()
        self.button7 = tk.Checkbutton(frame, text="OPTION 7", command=option7, justify="right",
                                      variable=self.button7_var, onvalue=1, offvalue=1)
        self.button7.pack(side="top", fill="both", expand=True)

        self.button8_var = tk.IntVar()
        self.button8 = tk.Checkbutton(frame, text="OPTION 8", command=option8, justify="right",
                                      variable=self.button8_var, onvalue=1, offvalue=1)
        self.button8.pack(side="top", fill="both", expand=True)


root = tk.Tk()
root.title('DEMO')
app = App(root)
root.mainloop()
