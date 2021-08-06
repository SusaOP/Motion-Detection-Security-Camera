PersonalSecuritySystem README file

This program is intended to permit a personal user to develop and implement their own security system.
It has a handful of features that should help you maintain personal security in your home:
1) Video recording in 30s increments, deleting the file if it does not detect movement
2) Saving of files if they do detect movement
3) Emailing via a private SMTP server of a handful of random screenshots from the detected video file

Intended to be implemented on a Raspberry Pi with USB camera/other video device.

This mimics the way in which commercial programs contact you when necessary.
You need to:
1) Create a private SMTP server on your Raspberry Pi/Old PC
2) Have a sending email address to send the movement-detection photos to
3) Have enough local storage to hold the movement-detection video files

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Files explained:

main.py:
    Processes functions, decides what files are worth saving.

operateCamera.py:
    Opens and records with the camera. Saves files in directory according to their time-of-recording.

into_frames.py:
    Disassembles video file into individual frames.

compare_frames.py:
    Compares all the video's frames with the initial frame to determine how similar they are.
    Saves frame ID which has most variance from the initial frame - This should be an identifying image

send_email.py:
    Establishes a smtp server (smtp.gmail.com) using existing gmail account (with less-secure-apps enabled)
    Uses gmail account's credentials to send an email containing the most significant frame of the video

