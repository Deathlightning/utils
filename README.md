# utils

平常写的一些小工具

## file_server

通过HTTP协议进行局域网文件传输，本来基于WebRTC的工具库是不少的，但是实践中可能由于内部网络管制难以联通，使用python写了个上传文件的小工具，下载文件可通过以下命令，

注意路径间隔符必须使用斜线

```python
python -m http.server 9000 -d D:/oneDrive/dataset/weight
```
