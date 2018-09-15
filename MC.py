import pymouse,pykeyboard,os,sys
from pymouse import *
import time
from pykeyboard import *
import itchat
from itchat.content import *

itchat.auto_login(hotReload=True)

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)#当对方发送文本时调用以下方案
def connect(msg):
    if msg["Text"] == "/Login":
        itchat.send_msg("已经连接，请发送指令...", toUserName=msg["FromUserName"])

        @itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)#当对方发送文本时调用以下方案
        def event(msg):
            k = PyKeyboard()
            motion = msg["Text"].split()
            if motion[0] == "/go":#向前
                if len(motion) == 3:
                    if motion[2] == "0":
                        itchat.send_msg("向前 " + motion[1] + " 步 , 潜行", toUserName=msg["FromUserName"])
                        k.press_key("W")  # 按住键盘，休眠时间后松开
                        time.sleep(int(motion[1]))
                        k.release_key("W")

                elif len(motion) == 2:
                    itchat.send_msg("向前 "+motion[1]+" 步", toUserName=msg["FromUserName"])
                    k.press_key("w")#按住键盘，休眠时间后松开
                    time.sleep(int(motion[1]))
                    k.release_key("w")

                elif len(motion) == 1:
                    itchat.send_msg("向前", toUserName=msg["FromUserName"])
                    k.press_key("w")
                    time.sleep(1)
                    k.release_key("w")

            elif motion[0] == "/back":#向后
                if len(motion) == 3:
                    if motion[2] == "0":
                        itchat.send_msg("向后 " + motion[1] + " 步 , 潜行", toUserName=msg["FromUserName"])
                        k.press_key("S")  # 按住键盘，休眠时间后松开
                        time.sleep(int(motion[1]))
                        k.release_key("S")

                elif len(motion) == 2:
                    itchat.send_msg("向后 "+motion[1]+" 步", toUserName=msg["FromUserName"])
                    k.press_key("s")
                    time.sleep(int(motion[1]))
                    k.release_key("s")

                elif len(motion) == 1:
                    itchat.send_msg("向后 ", toUserName=msg["FromUserName"])
                    k.press_key("s")
                    time.sleep(1)
                    k.release_key("s")

            elif motion[0] == "/left":#向左
                if len(motion) == 2:
                    itchat.send_msg("向左 "+motion[1]+" 步", toUserName=msg["FromUserName"])
                    k.press_key("a")
                    time.sleep(int(motion[1]))
                    k.release_key("a")

                else:
                    itchat.send_msg("向左", toUserName=msg["FromUserName"])
                    k.press_key("a")
                    time.sleep(1)
                    k.release_key("a")

            elif motion[0] == "/right":#向右
                if len(motion) == 2:
                    itchat.send_msg("向右 "+motion[1]+" 步", toUserName=msg["FromUserName"])
                    k.press_key("l")
                    time.sleep(int(motion[1]))
                    k.release_key("l")

                else:
                    itchat.send_msg("向右", toUserName=msg["FromUserName"])
                    k.press_key("d")
                    time.sleep(1)
                    k.release_key("d")

            elif motion[0] == "/shift":#下蹲
                itchat.send_msg("下蹲",toUserName=msg["FromUserName"])
                k.press_key(k.shift_key)#shift

            elif motion[0] == "/up":#跳起
                itchat.send_msg("跳起",toUserName=msg["FromUserName"])
                k.press_key(32)#空格
                time.sleep(0.5)
                k.release_key(32)
                k.release_key(k.shift_key)#松开shift

            elif motion[0] == "/leap":#跳跃
                itchat.send_msg("向前跳跃",toUserName=msg["FromUserName"])
                k.press_key("w")
                time.sleep(0.5)
                k.press_key(32)
                time.sleep(0.5)
                k.release_key(32)
                k.release_key("w")

            elif motion[0] == "/drop":#丢弃
                itchat.send_msg("丢弃",toUserName=msg["FromUserName"])
                k.tap_key("Q")

            elif motion[0] == "/pack":#背包
                itchat.send_msg("背包",toUserName=msg["FromUserName"])
                k.tap_key("E")

            elif motion[0] == "/F3":#调试模式
                itchat.send_msg("调试模式", toUserName=msg["FromUserName"])
                k.tap_key(k.function_keys[3])

            elif motion[0] == "/F5":#切换人称
                itchat.send_msg("切换人称",toUserName=msg["FromUserName"])
                k.tap_key(k.function_keys[5])

            elif motion[0] == "/cmd":#输入指令
                itchat.send_msg("指令 /" + " ".join(motion[1:len(motion)]) + "正在执行",toUserName=msg["FromUserName"])
                k.tap_key("/")
                time.sleep(0.5)
                k.type_string(" ".join(motion[1:len(motion)]))
                time.sleep(0.5)
                k.tap_key(13)

            elif motion[0] == "/chat":#输入一段话
                itchat.send_msg("您说了\"" + " ".join(motion[1:len(motion)]) + "\"", toUserName=msg["FromUserName"])
                k.tap_key("T")
                time.sleep(0.5)
                k.type_string(" ".join(motion[1:len(motion)]))
                time.sleep(0.5)
                k.tap_key(13)

            elif motion[0] == "/exit":#退出微信登录
                itchat.send_msg("已经退出登录",toUserName=msg["FromUserName"])
                itchat.logout()
                k.tap_key(27)

itchat.run()
itchat.dump_login_status()