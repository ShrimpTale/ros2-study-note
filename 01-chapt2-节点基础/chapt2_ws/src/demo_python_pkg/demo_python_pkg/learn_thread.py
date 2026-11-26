import threading
import requests
#         ↑发HTTP请求的第三方库

class Download:
    def download(self,url,callback_world_count):
        print(f'任务线程：{threading.get_ident()}，开始下载：{url}')
        #                          获取线程编号
        response =requests.get(url)#get方法取得url，下载本体
        response.encoding='utf-8'#utf-8是字符串里的内容
        callback_world_count(url,response.text)#调用回调函数
    #                                  ↑
        #requests.get() 返回的是一个 Response 对象(response变量)，而 Response 类内部定义了 text 这个属性

    def start_download(self,url,callback_world_count):
        #self.download(url,callback_world_count)
        #不能这样，download会跑在start_download同一个线程
        #下载完期间start_download会被其卡住
        
        thread =threading.Thread(target=self.download,args=(url,callback_world_count))
        #                ↓                     ↓
        #         这个线程要执行什么函数     传入要执行函数的参数

        thread.start()#启动线程


def world_count(url,result):
    #回调函数
    print(f"{url}:{len(result)}->{result[0:5]}")
    #     ↓         ↓→给出元素/字符数量     ↓
    #格式化，将变量与表达式替换为值      取从0到5的前五个(0-4)字符/元素
    
def main():  
    download=Download()
    download.start_download('http://localhost:8001/novel1.txt',world_count )
    download.start_download('http://localhost:8001/novel2.txt',world_count )
    download.start_download('http://localhost:8001/novel3.txt',world_count )