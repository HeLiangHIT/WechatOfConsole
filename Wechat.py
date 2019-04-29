import itchat
from itchat.content import *

@itchat.msg_register(TEXT) # 注册消息，如果有消息收到
def recv_msg(msg):
    itchat.send_msg('{}'.format(msg['Text']))
    itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    return "T reveived: %s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容

callBack = {
    'listUser':listUser,
    'listRoom':listRoom
}

def ec():
    itchat.logout()

if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR = 2,exitCallback=ec) #登录并记录登录状态
    user_list[] = get_friends();
    user_dict = {}
    for i in len(user_list):
        user_dict[i] = user_list[i]['RemarkName']# id 和昵称存储用户信息
    while True:
        cmd = input().strip() # 命令去除前后空格
        callBack[cmd]() # 调用cmd所匹配的函数
itchat.send("Hello World!"，toUserName=None) # 讲信息发送给user
ithcat.send("@fil@%s" % '/tmp/test.text')
ithcat.send("@img@%s" % '/tmp/test.png')
ithcat.send("@vid@%s" % '/tmp/test.mkv')

@itchat.msg_register(TEXT)   #这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
def simple_reply(msg):
    #这个是向发送者发送消息
    itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    return "T reveived: %s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容

itchat.get_friends()  返回完整的好友列表、
每个好友为一个字典, 其中第一项为本人的账号信息;
传入 update=True, 将更新好友列表并返回, get_friends(update=True)

# 获取任何一项等于name键值的用户
itchat.search_friends(name='autolife')
获取备注,微信号, 昵称中的任何一项等于name键值的用户. (可以与下一项配置使用.)

get_mps
将返回完整的工作号列表
每个公众号为一个字典,
传入 update=True 将更新公众号列表, 并返回.



get_chatrooms : 返回完整的群聊列表.
search_chatrooms : 群聊搜索.
update_chatroom : 获取群聊用户列表或更新该群聊.
memberList = itchat.update_chatroom('@@abcdefg1234567', detailedMember=True)
