class User:
    def __init__(self, ip,name,time,like=None):
        self.likelist=like
        self.probalsit=[9,8,9,5,6,8,8,8,8] # 每次不向下点击的概率
        self.ip=ip
        self.name=name
        self.time=time

    def is_down(self, depth=0, keys=None):
        """
        在depth层，判断a该用户是是都继续访问该网页。
        :param depth: 访问网页树的深度
        :param keys: 该用户的偏好。
        :return: 是否向下点击
        """
        import random
        import time
        random.seed(time.time())
        num=random.randint(0,10)
        if self.likelist:
            for key in keys:
                if key in self.likelist:
                    return True
        # print(f"---{num}--")
        if num>=self.probalsit[depth]:
            return True
        return False

    def get_down_index(self, keys=None):
        """
        获取向下点击的下标
        :param keys:
        :return:
        """
        import random
        import time
        random.seed(time.time())
        ans=[]
        if self.likelist:
            for like in self.likelist:
                if like in keys:
                    ans.append(like)
        return ans[random.randint(0, len(ans)-1)] if len(ans)>0 else keys[random.randint(0, len(keys)-1)]


