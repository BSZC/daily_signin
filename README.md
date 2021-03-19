# daily_signin 日常签到

### **更新历史**

2021.3.19  创建项目，建立吾爱破解签到

### **通知示例**

![](https://gitee.com/kxs2018/daily_signin/blob/main/pic/textcard.png)

### **签到列表**

|                   网站名称                   |   secrets   | 多账号 |
| :------------------------------------------: | :---------: | :----: |
| [吾爱破解](https://www.52pojie.cn/forum.php) |  PJ_COOKIE  |   否   |
|        [CSDN](https://blog.csdn.net/)        | CSDN_COOKIE |   否   |



注：多账号cookie之间用&分隔

### secrets

- 添加方式：setting-secrets-add a new secret
- [secrets说明](https://github.com/lqkxs3608/daily_signin/blob/main/secrets.md)

### **获取cookie**

1. 浏览器登录网站——按F12打开开发人员工具——NETWORK拉动右边的滚动条到最顶部，点击最上面的选项（如下图）

![](https://gitee.com/shuye72/MyActions/raw/main/icon/jd4.jpg)

2. 上面复制好的cookie先保存到本地，然后复制相应的代码到浏览器开发人员工具的console里，再把cookie复制粘帖到代码里并按enter，所需要的cookie就复制到剪切板了，粘帖到本地备用即可。

   ```
   # 吾爱破解cookie转换代码（这行不用复制）
   var CV = '单引号里面放前面拿到的cookie';
   var CookieValue = CV.match(/htVD_2132_auth=.+?;/) + CV.match(/htVD_2132_saltkey=.+?;/);
   copy(CookieValue);
   ```

[各网站cookie转换代码](https://github.com/lqkxs3608/daily_signin/blob/main/cookie.md)
