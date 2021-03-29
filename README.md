# daily_signin 日常签到

### **更新历史**

2021.3.27  改变签到方式，每个签到程序单独运行。增加WPS签到

2021.3.26  增加有道云笔记签到

2021.3.23  为避免index.py太过臃肿，修改了代码结构。正在尝试多线程签到

2021.3.21  增加tool.lu签到

2021.3.20  增加CSDN、天翼云盘签到

2021.3.19  创建项目，建立吾爱破解签到

### **通知示例**

![](https://images.gitee.com/uploads/images/2021/0319/224105_cdd105fd_7943916.png)



### **签到列表**

|                   网站名称                   | 签到时间  | 多账号 |              说明               |
| :------------------------------------------: | :-------: | :----: | :-----------------------------: |
| [吾爱破解](https://www.52pojie.cn/forum.php) | 7:20,8:20 |   否   |                                 |
|        [CSDN](https://blog.csdn.net/)        | 7:23,8:23 |   否   |                                 |
|      [天翼云盘](https://cloud.189.cn/)       | 7:26,8:26 |   是   |  帐号：手机号，密码：不能带&。  |
|                                              |           |        | 帐号和帐号、密码和密码间用&连接 |
|         [在线工具](https://tool.lu/)         | 7:29,8:29 |   否   |                                 |
|  [有道云笔记](https://note.youdao.com/web)   | 7:32,8:32 |   是   |                                 |
|    [WPS](https://vip.wps.cn/taskcenter/)     | 7:35,8:35 |   否   | 网页、客户端、小程序多渠道签到  |



注：1. 多账号cookie之间用&分隔。
2. 如需更改签到时间，到.github\workflows\xxxx.yml中更改
3. 不需要签到的网站不需要加secrets
### secrets

- 添加方式：setting-secrets-add a new secret
- [secrets说明](https://github.com/lqkxs3608/daily_signin/blob/main/secrets.md)

### **获取cookie**

1. 浏览器登录网站——按F12打开开发人员工具——NETWORK拉动右边的滚动条到最顶部，点击最上面的选项（如下图）

![](https://gitee.com/kxs2018/img-bed/raw/master/imgs/getcookie.jpg)

2. 上面复制好的cookie先保存到本地，然后复制相应的代码到浏览器开发人员工具的console里，再把cookie复制粘帖到代码里并按enter，所需要的cookie就复制到剪切板了，粘帖到本地备用即可。

   ```
   # 吾爱破解cookie转换代码（这行不用复制）
   var CV = '单引号里面放前面拿到的cookie';
   var CookieValue = CV.match(/htVD_2132_auth=.+?;/) + CV.match(/htVD_2132_saltkey=.+?;/);
   copy(CookieValue);
   ```

[各网站cookie转换代码](https://github.com/lqkxs3608/daily_signin/blob/main/cookie.md)  

