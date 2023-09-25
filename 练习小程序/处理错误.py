#2020年12月10日20:24:53
while 1:
    try:  #以下为测试代码
        a=int(input('被除数: '))
        b=int(input('除数: '))
        print('商：%d'%(a/b))
    except (ZeroDivisionError,ValueError):  #可以用tuple写入多个异常类型
        print('除数不能为零,或未输入数字')
    except ZeroDivisionError:
        print('除数不能为零')    #Exception本质是一个类
    except Exception as r:    #不确定的异常类型可以使用Exception，
        print(type(r),r)        #可以将异常类型保存在某变量中
    except:   #必须放在有对象的except之后
        print('出现错误')
    else:     #若无异常则执行的语句。可选非必须
        pass
    finally:   #有无异常均会执行的语句，必须放最后。可选非必须
        pass
