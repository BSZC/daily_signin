## cookie转换代码

#### **吾爱破解**

```
var CV = '单引号里面放浏览器复制好的cookie';
var CookieValue = CV.match(/htVD_2132_auth=.+?;/) + CV.match(/htVD_2132_saltkey=.+?;/);
copy(CookieValue);
```

#### **CSDN**

```
var CV = '单引号里面放浏览器复制好的cookie';
var CookieValue = CV.match(/UserName=.+?;/) + CV.match(/UserToken=.+?;/) +  CV.match(/UserNick=.+?;/);
copy(CookieValue);
```

#### **tool.lu**

##### 如果使用以下代码一定要到 https://plus.tool.lu/user/sign获取cookie

```
var CV = '单引号里面放浏览器复制好的cookie';
var CookieValue = CV.match(/uuid=.+?;/) + CV.match(/laravel_session=.+/);
copy(CookieValue);
```

#### **WPS**

```
var CV = '单引号里面放浏览器复制好的cookie';
var CookieValue = CV.match(/wps_sid=(.+?);/)[1];
copy(CookieValue);
```

