# RestartDockerLangbot

## 安装

配置完成 [LangBot](https://github.com/RockChinQ/LangBot) 主程序后使用管理员账号向机器人发送命令即可安装：

```
!plugin get https://github.com/wanjiaju3108/RestartDockerLangbot
```
或查看详细的[插件安装说明](https://docs.langbot.app/plugin/plugin-intro.html#%E6%8F%92%E4%BB%B6%E7%94%A8%E6%B3%95)

## 使用

需要在宿主机中预先安装go语言环境

将restart-langbot文件上传到宿主机中

在宿主机执行以下命令
```commandline
sudo chmod +x restart-langbot
nohup ./restart-langbot > out.log 2>&1 &
```
向机器人输入以下命令即可重启
```commandline
.重启
```