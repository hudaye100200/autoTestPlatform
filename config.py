#encoding:utf-8
# #name:mod_config.py

from configparser import ConfigParser
'''
ConfigParser模块在python3中修改为configparser.这个模块定义了一个ConfigParser类，
该类的作用是使用配置文件生效，配置文件的格式和windows的INI文件的格式相同
该模块的作用 就是使用模块中的RawConfigParser()、ConfigParser()、 
SafeConfigParser()这三个方法（三者择其一），
创建一个对象使用对象的方法对指定的配置文件做增删改查 操作
'''
import os

def getConfig(section, key):
    config = ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '\setting.conf'
    print(path)
    config.read(path)
    print(config.read(path))
    return config.get(section, key)


if __name__ == '__main__':
    a = getConfig('database','db')
    print(a)
