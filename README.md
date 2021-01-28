# 东南大学每日上报健康申报小助手

> 免责声明：本脚本仅为个人为学习python之目的所编写，使用该脚本造成的一切后果均由使用者承担。  本人提倡每日按时手动进行疫情上报与入校申请，配合学校进行好疫情防控。

# Intro
疫情期，各高校行每日上报制，然则上报多矫，正所谓金玉其外，败絮其中。君不见体温350°无人闻，折让导员趋学生。导员何错？学生何错？笑。

小助手基于selenium，Gay站上已有许多类似地高校填报小助手，原理都是类似的QWQ。使用Driver控制浏览器，selenium填写信息request到server。

本小助手提供的功能：
 - 持续自动填报
 - 多人填报
 - 随机数防止检测

小助手默认在服务器环境下运行，保证py文件在执行后需要一直开启。如果没有服务器支持，也可以用win/mac/linux自带的定时执行程序功能。
# 使用说明

 1. 下载最新Chrome浏览器，并查看版本。
 在[https://npm.taobao.org/mirrors/chromedriver/](https://npm.taobao.org/mirrors/chromedriver/)处选择对应浏览器版本的Chromedriver文件下载。
 2. 安装selenium包。
 3. 将Chromedriver文件命名为Chromedriver.exe放到py文件统一文件夹下，修改config为自己的账号密码，如果只想填报自己的信息，删掉其他user即可。
 4. 运行py文件。

