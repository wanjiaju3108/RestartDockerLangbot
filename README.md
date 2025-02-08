# RestartDockerLangbot

## 安装

配置完成 [LangBot](https://github.com/RockChinQ/LangBot) 主程序后使用管理员账号向机器人发送命令即可安装：

```
!plugin get https://github.com/wanjiaju3108/RestartDockerLangbot
```
或查看详细的[插件安装说明](https://docs.langbot.app/plugin/plugin-intro.html#%E6%8F%92%E4%BB%B6%E7%94%A8%E6%B3%95)

## 使用

**1、在宿主机执行以下命令**
```commandline
ip addr show docker0
```
如果输出类似于
```
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:76:c9:b0:6e brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:76ff:fec9:b06e/64 scope link
       valid_lft forever preferred_lft forever
```
则可继续进行，否则插件不适配

**2、在宿主机执行以下命令**
```commandline
nohup sh -c 'while true; do nc -l -p 8000 | { sleep 1; } ; docker restart langbot; done' &
```
注意：不要重复执行此命令

如果想要关闭端口监听 需要执行命令
```commandline
ps -ef|grep 'nc -l'
```
获取nohup与nc -l两个进程ID 然后通过kill命令杀掉进程

**3、向机器人输入以下命令即可重启**
```commandline
.重启
```