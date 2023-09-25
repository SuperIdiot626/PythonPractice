userlist=[]

class users(object):
    def __init__(self,name,password):
        #
        self.name=name                          #设置姓名
        self.account=len(userlist)+10000        #设置账号
        self.password=password                  #设置密码
        self.id=len(userlist)+1                 #id
        userlist.append(self)                   #把自己添加进用户列表里
        self.ban_state=False                    #是否被ban
    
    def changepassword(self):
        old_password=input("请输入旧密码：")
        if old_password==self.password:
            print("****验证成功！****")
            new_password=input("请输入新密码：")
            new_password_check=input("请再次输入新密码：")
            if new_password==new_password_check:
                self.password=new_password
                print("****改密成功！****")
                print(self.password)

class admin(users):
    def __init__(self,name,password):
        super().__init__(name,password)

    def banuser(self,id):
        if id<=len(userlist):
            userlist[id].ban_state=True
            print('已将账号为%d用户设置为封禁状态'%userlist[id].account)
        else:
            print("未找到指定用户")
    def unbanuser(self,id):
        if id<=len(userlist):
            userlist[id].ban_state=False
            print('已将账号为%d用户设置为开放状态'%userlist[id].account)
        else:
            print("未找到指定用户")

    def show_all(self):
        for i in userlist:
            print(i.name,i.account,i.id,i.ban_state)



user1=users("sb1","123456")
user2=users("sb2","1234567")
user3=users("sb3","12345678")
user4=users("sb4","123456789")
admin1=admin("admin","100")
admin1.show_all()
admin1.banuser(1)
admin1.banuser(2)
admin1.show_all()

admin1.unbanuser(1)
admin1.unbanuser(2)
admin1.show_all()