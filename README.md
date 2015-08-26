# douyu_notify

##python版
因为不想用第三方库，所以只有简陋的弹窗提醒，弹窗只支持win，不支持*nix。

如果需要邮件提醒，请自行修改邮箱、密码。可以发送到139或 wo 邮箱，间接实现短信提醒。

Usage: python douyu.py kyu999 chenyifaer erke



##powershell版
有人反映安装python太麻烦，所以写了个powershell版，懒得写多线程和邮件提醒功能了，只支持单个直播间弹窗提醒。

Usage: powershell IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/ACGT/douyu_notify/master/douyu_notify.ps1')
