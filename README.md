# douyu_notify

python版：

因为不想用第三方库，所以只有丑陋的弹窗提醒，弹窗只支持win，不支持mac/linux。

默认只会提醒陈工和二珂的直播。如果需要提醒更多的直播间，请参考代码里的注释自己改一下。

如果需要邮件提醒，请自行修改邮箱、密码。可以发送到139或 wo 邮箱，间接实现短信提醒。



powershell版：

有人反映安装python太麻烦，所以写了个 powershell 版，懒得写多线程和邮件提醒功能了，只支持单个直播间弹窗提醒。默认是673673。

命令行下输入 powershell IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/ACGT/douyu_notify/master/douyu_notify.ps1')
