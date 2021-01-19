# python的构建工具setup.py

## 一、构建工具setup.py的应用场景

在安装python的相关模块和库时，我们一般使用“pip install  模块名”或者“python setup.py install”，前者是在线安装，会安装该包的相关依赖包；后者是下载源码包然后在本地安装，不会安装该包的相关依赖包。所以在安装普通的python包时，利用pip工具相当简单。但是在如下场景下，使用python setup.py install会更适合需求：

在编写相关系统时，python 如何实现连同依赖包一起打包发布？

>   假如我在本机开发一个程序，需要用到python的redis、mysql模块以及自己编写的redis_run.py模块。我怎么实现在服务器上去发布该系统，如何实现依赖模块和自己编写的模块redis_run.py一起打包，实现一键安装呢？同时将自己编写的redis_run.py模块以exe文件格式安装到python的全局执行路径C:\Python27\Scripts下呢？

在这种应用场景下，pip工具似乎派不上了用场，只能使用python的构建工具setup.py了，使用此构建工具可以实现上述应用场景需求，只需在 setup.py 文件中写明依赖的库和版本，然后到目标机器上使用python setup.py install安装。

## 二、setup.py介绍

```python
from setuptools import setup, find_packages

setup(
    name = "test",
    version = "1.0",
    keywords = ("test", "xxx"),
    description = "eds sdk",
    long_description = "eds sdk for python",
    license = "MIT Licence",

    url = "http://test.com",
    author = "test",
    author_email = "test@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],

    scripts = [],
    entry_points = {
        'console_scripts': [
            'test = test.help:main'
        ]
    }
)
```

**setup.py各参数介绍：**

- name 包名称
- version (-V) 包版本
- author 程序的作者
- author_email 程序的作者的邮箱地址
- maintainer 维护者
- maintainer_email 维护者的邮箱地址
- url 程序的官网地址
- license 程序的授权信息
- description 程序的简单描述
- long_description 程序的详细描述
- platforms 程序适用的软件平台列表
- classifiers 程序的所属分类列表
- keywords 程序的关键字列表
- packages 需要处理的包目录（包含__init__.py的文件夹） 
- py_modules 需要打包的python文件列表
- download_url 程序的下载地址
- cmdclass 
- data_files 打包时需要打包的数据文件，如图片，配置文件等
- scripts 安装时需要执行的脚步列表
- package_dir 告诉setuptools哪些目录下的文件被映射到哪个源码包。一个例子：package_dir = {'': 'lib'}，表示“root package”中的模块都在lib 目录中。
- requires 定义依赖哪些模块 
- provides定义可以为哪些模块提供依赖 
- find_packages() 对于简单工程来说，手动增加packages参数很容易，刚刚我们用到了这个函数，它默认在和setup.py同一目录下搜索各个含有 __init__.py的包。

> 其实我们可以将包统一放在一个src目录中，另外，这个包内可能还有aaa.txt文件和data数据文件夹。另外，也可以排除一些特定的包

> find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

- install_requires = ["requests"] 需要安装的依赖包
- entry_points 动态发现服务和插件，下面详细讲

下列entry_points中： console_scripts 指明了命令行工具的名称；在“redis_run = RedisRun.redis_run:main”中，等号前面指明了工具包的名称，等号后面的内容指明了程序的入口地址。
```python
entry_points={'console_scripts': [
    'redis_run = RedisRun.redis_run:main',
    ]}
```

这里可以有多条记录，这样一个项目就可以制作多个命令行工具了，比如：
```python
from setuptools import setup
setup(
    entry_points = {
        'console_scripts': [
            'foo = demo:test',
            'bar = demo:test',
        ]}
)
```

## 三、setup.py的项目示例代码
```python
#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

'''
把redis服务打包成C:\Python27\Scripts下的exe文件
'''

setup(
    name="RedisRun",  #pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="1.0",
    author="Andreas Schroeder",
    author_email="andreas@drqueue.org",
    description=("This is a service of redis subscripe"),
    license="GPLv3",
    keywords="redis subscripe",
    url="https://ssl.xxx.org/redmine/projects/RedisRun",
    packages=['RedisRun'],  # 需要打包的目录列表

    # 需要安装的依赖
    install_requires=[
        'redis>=2.10.5',
        'setuptools>=16.0',
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'redis_run = RedisRun.redis_run:main',
    ]},

    # long_description=read('README.md'),
    classifiers=[  # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
```

## 四、修改后的项目代码

（此时RedisRun模块是DrQueue模块的子模块，这是因为要导入某些公用的模块）
```python
#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

'''
把redis服务打包成C:\Python27\Scripts下的exe文件
'''

setup(
    name="RedisRun",  #pypi中的名称，pip或者easy_install安装时使用的名称
    version="1.0",
    author="Andreas Schroeder",
    author_email="andreas@drqueue.org",
    description=("This is a service of redis subscripe"),
    license="GPLv3",
    keywords="redis subscripe",
    url="https://ssl.xxx.org/redmine/projects/RedisRun",
    packages=['DrQueue'],  # 需要打包的目录列表

    # 需要安装的依赖
    install_requires=[
        'redis>=2.10.5',
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'redis_run = DrQueue.RedisRun.redis_run:main',
    ]},

    # long_description=read('README.md'),
    classifiers=[  # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
```
此时包目录结构为：
![setup_tool_example](../01_PythonBasic/images/setup_dirs_example.png)
