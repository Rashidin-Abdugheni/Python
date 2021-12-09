import os
import tkinter
import tkinter.filedialog
import time
import threading
import pygame  # 实现音频播放
root = tkinter.Tk()
root.title('MP3 Player 1.0 By Rashidin Abdugheni 🦅')
root.configure(bg='#9FF781')
root.geometry('460x600')
root.resizable(False, False)
# And Image should be in the same folder where there is script saved
#p1 = PhotoImage(file = 'C:/Users/Mr.R/Pictures/1.jpg')


folder = ''  # 接收文件路径 默认为空
res = []  #
num = 0
now_music = ''


# 第二步：实现功能

def buttonChooseClick():
    # 添加文件函数

    global folder
    global res
    # 如果folder不为空，则····
    if not folder:
        folder = tkinter.filedialog.askdirectory()  # 选择目录，返回目录名
        musics = [folder + '\\' + music
                  for music in os.listdir(folder) \
 \
                  if music.endswith(('.mp3', '.m4a', '.wav', '.ogg'))]

        ret = []
        for i in musics:
            ret.append(i.split('\\')[1:])
            res.append(i.replace("\\", '/'))

        var2 = tkinter.StringVar()
        var2.set(ret)
        lb = tkinter.Listbox(root, listvariable=var2)
        lb.place(x=70, y=230, width=300, height=300)

    if not folder:
        return
    global playing
    playing = True

    # 根据情况禁用或启用相应按钮

    bottonPlay['state'] = 'normal'
    bottonStop['state'] = 'normal'

    # buttonPause['state'] = 'normal'

    pause_resume.set('Play')


# 播放音乐函数
def play():
    # 初始化混响设备

    if len(res):
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                # 随机播放
                nextMusci = res[num]
                print(nextMusci)
                print(num)
                pygame.mixer.music.load(nextMusci.encode())
                # 播放一次
                pygame.mixer.music.play(1)
                # print(len(res)-1)
                if len(res) - 1 == num:
                    num = 0
                else:
                    num += 1
                nextMusci = nextMusci.split("\\")[1:]
                musicName.set('Playing...' + ''.join(nextMusci))
            else:
                time.sleep(0.1)


# 点击播放函数
def bottonPlayClik():
    bottonNext['state'] = 'normal'
    bottonPrev['state'] = 'normal'

    # 选择要播放的音乐文件夹
    if pause_resume.get() == 'Play':
        pause_resume.set('Pause')
        global folder

        if not folder:
            # 选择目录，返回目录名
            folder = tkinter.filedialog.askdirectory()

        if not folder:
            return

        global playing

        playing = True

        # 创建一个进程来播放音乐，当前主进程用来接收用户操作

        t = threading.Thread(target=play)

        t.start()

    elif pause_resume.get() == 'Pause':

        pygame.mixer.music.pause()
        pause_resume.set('Continue')

    elif pause_resume.get() == 'Continue':
        pygame.mixer.music.unpause()

        pause_resume.set('Pause')



def bottonStopClik():
    global playing

    playing = False

    pygame.mixer.music.stop()



def bottonNextClik():
    global playing

    playing = False

    pygame.mixer.music.stop()

    global num

    if len(res) == num:
        num = 0
    playing = True
    global t
    t = threading.Thread(target=play)

    t.start()


# 上一首函数
def bottonPrevClik():
    global playing

    playing = False

    pygame.mixer.music.stop()

    global num

    if num == 0:
        num = len(res) - 2

    elif num == len(res) - 1:
        num -= 2
    else:
        num -= 2
    print(num)

    playing = True
    global t
    t.threading.Thread(target=play)

    t.start()


# 关闭窗口函数
def closeWindows():
    global playing
    playing = False
    time.sleep(0.3)

    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except:
        pass
    root.destroy()


# 声音控制函数
def control_voice(value=0.5):
    pygame.mixer.music.set_volume(float(value))


# 添加按钮
bottonChoose = tkinter.Button(root, text='Add Musics',fg="Red", command=buttonChooseClick,bg="sky blue")
# 按钮布局
bottonChoose.place(x=70, y=50, width=140, height=20)

# 播放按钮	跟踪变量值的变化
pause_resume = tkinter.StringVar(root, value='Play')
bottonPlay = tkinter.Button(root, textvariable=pause_resume,fg="Red", command=bottonPlayClik,bg="sky blue", font = ('arial', 11))
# 按钮布局
bottonPlay.place(x=230, y=50, width=140, height=20)
bottonPlay['state'] = 'disabled'  # 未添加文件（刚启动）时禁用

# 停止播放
bottonStop = tkinter.Button(root, text='Stop',bg="sky blue")
# 按钮布局
bottonStop.place(x=70, y=80, width=140, height=20)

# 下一首
bottonNext = tkinter.Button(root, text='Next', command=bottonNextClik,bg="sky blue",fg="Red")
# 按钮布局
bottonNext.place(x=230, y=80, width=140, height=20)
bottonNext['state'] = 'disabled'

# 上一首
bottonPrev = tkinter.Button(root, text='Previous', command=bottonPrevClik,bg="sky blue",fg="Red")
# 按钮布局
bottonPrev.place(x=70, y=110, width=300, height=20)
bottonPrev['state'] = 'disabled'

# 显示内容--播放状态
musicName = tkinter.StringVar(root, value='❀MP3 Player 1.0 By Rashidin Abdugheni❀')
labelName = tkinter.Label(root, textvariable=musicName)
labelName.place(x=70, y=20, width=300, height=20)

# 显示内容--音量调节
s = tkinter.Scale(root, label='Voice Volume', from_=0, to=1, orient=tkinter.HORIZONTAL, length=240,
                  showvalue=0, tickinterval=2, resolution=0.1, command=control_voice,bg="sky blue",fg="Red")
s.place(x=70, y=150, width=300)

# 关闭窗口
root.protocol("WM_DELETE_WINDOW", closeWindows)

# 启用消息循环:显示出上一步创建的画板对象
root.mainloop()