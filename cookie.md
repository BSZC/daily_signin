## cookie转换代码

#### **吾爱破解**

```
var CV = '单引号里面放浏览器复制好的cookie';
var CookieValue = CV.match(/htVD_2132_auth=.+?;/) + CV.match(/htVD_2132_saltkey=.+?;/);
copy(CookieValue);
```