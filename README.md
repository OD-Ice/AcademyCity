# AcademyCity

## 学园都市管理系统

基于django+AdminLTE+bootstrap，以[学园都市]([https://baike.baidu.com/item/%E5%AD%A6%E5%9B%AD%E9%83%BD%E5%B8%82/10653393?fr=aladdin](https://baike.baidu.com/item/学园都市/10653393?fr=aladdin))为背景和原型的假想中的管理系统。

### 展示页面

[AcademyCity](http://59.110.26.52/)

备注：没有单独做移动端，建议使用pc端进行登录，目前移动端登录存在一些布局错位和不可预见的bug。

部分测试账号密码：

| 账户名称  | 登录用手机号 | 密码   | 权限                                                         |
| --------- | ------------ | ------ | ------------------------------------------------------------ |
| superuser | 13333333333  | 123456 | 超级管理员，拥有全部权限                                     |
| user      | 18888888888  | 123456 | 学生用户，为方便测试，拥有除处理待办事务，修改管理者和学生信息外的大部分权限 |
| teacher   | 16666666666  | 123456 | 普通管理者，拥有学生全部权限，拥有处理待办事务，修改删除管理者和学生的权限 |

### 技术相关

前端

+ adminLTE
+ bootstrap
+ jquery+html+css

后端

+ django
+ mysql
+ memcached
+ arttemplate

项目部署

+ 阿里云服务器，ubuntu操作系统
+ nginx+uwsgi
+ supervisor

其他第三方工具

+ [tinymce](http://tinymce.ax-z.cn/)富文本编辑器
+ [sweetalert](https://www.sweetalert.cn/guides.html#getting-started)弹窗的替换模块
+ [gulp](https://www.gulpjs.com.cn/)自动化构建工具
+ [Timetables](https://github.com/Hzy0913/Timetable)课程表

### 项目模块

```
├── 用户管理(基于django用户管理模块进行改写拓展)
│	├── 学生管理
│	│	├── 学生名单增删改查
│	│	├── 搜索功能
│	│	├── 课程表
│	│	├── 成绩查询
│	│	└── 待办事项查看与留言
│	├── 职工管理
│	│	├── 管理者增删改查
│	│	└── 待办事项处理
│	├── 管理者申请
│	├── 等级修改申请
│	└── 个人评论发布记录
├── 学校管理
│	├── 学校信息注册
│	│	├── 校徽
│	│	├── 简介(tinymce)
│	│	└── 其他信息
│	├── 科研等级
│	│	└── 科研等级的增删改查
│	├── 校园列表
│	│	├── 学校信息修改与删除
│	│	└── 搜索功能
│	└── 校园详情页
│	 	├── 信息展示
│	 	└── 用户评论
└── 课程管理
 	├── 课程发布
 	│	└── 学校课程选择
 	└── 成绩录入
```



