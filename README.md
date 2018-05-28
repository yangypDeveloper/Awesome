# Awesome

跟随廖雪峰的python3教程实战项目

### day1
![success](./images/2018-05-28-1.png)

> 关于打开网页下载的问题,按照评论解决,如下

```python
-return web.Response(body=b'<h1>Awesome</h1>')
+return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
```