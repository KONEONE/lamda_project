import time

class LogProduct:
    def __init__(self, user_num=5):
        self.user_num=user_num
        self.web_json_path="./data/web2.json"
        self.likelist=['家居家纺', '日用百货', '母婴用品', '美食特产', '文化娱乐', '出差旅游', '鞋', '游戏', '金融', '医疗保健', '服装配饰', '箱包', '珠宝钟表', '电脑/办公', '运动户外', '本地生活', '手机/手机配件', '家用电器', '个护化妆', '家具建材', '数码', '房产', '汽车用品']
        self.web=self.get_web_tree()

    def get_web_tree(self):
        """
        获取web的树型结构
        :return:
        """
        import json
        with open(self.web_json_path, "r", encoding="utf-8") as f:
            web_dict=json.load(f)
        return web_dict

    def DFS(self, web, user, ans : list, depth=0, upstr="www.example.com/"):
        for key in web.keys():
            if user.is_down(depth, key):
                # print(user.ip, user.name, user.time, upstr + key)
                time_str=time.strftime("%Y-%m-%d:%H:%M:%S", time.localtime())
                log_str=user.ip+" "+user.name+" "+time_str+" "+upstr+key
                ans.append(log_str)
                if key == "end":
                    # print(user.ip, user.name, user.time, upstr + key + "/" + web[key])
                    log_str = user.ip + " " + user.name + " " + time_str + " " + upstr + key
                    ans.append(log_str)
                else:
                    self.DFS(web[key], user, ans , depth + 1, upstr + key + "/")

    def random_ip(self):
        import random
        import time
        random.seed(time.time())
        random_list=["12","41","115","45","48","65","78","71","47","11"]
        ip=""
        size=len(random_list)
        for i in range(4):
            ip+=random_list[random.randint(0, size-1)]
            if i < 3:
                ip+="."
        return ip

    def product_user_data(self):
        """
        生成一个随机的用户对象，主要生成name(随机), ip(随机), time, like(随机)
        :return: 返回随机用户的点击网站的浏览日志
        """
        import random
        import time
        from utils.user import User
        random.seed(time.time())
        usr_name=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], random.randint(2,5)))
        ip=self.random_ip()
        time_str=time.strftime("%Y-%m-%d:%H:%M:%S", time.localtime())
        like_str=self.likelist[random.randint(0, len(self.likelist)-1)]
        usr=User(ip, usr_name, time_str, like_str)

        usr_log=[]
        web=self.web
        self.DFS(web, usr, usr_log)

        return usr_log

    def product(self):
        """
        产生self.usr_num 个用户的访问网站的日志记录
        :return: list
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        pool = ThreadPoolExecutor(max_workers=3)
        all_task = [pool.submit(self.product_user_data) for i in range(self.user_num)]

        res = []

        for future in as_completed(all_task):
            usr_log = future.result()
            res+=usr_log

        return res
