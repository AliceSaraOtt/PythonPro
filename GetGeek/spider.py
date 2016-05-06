# coding:utf8
import requests
from lxml import etree
import re
import sys, os, glob, time

# import scrapy
reload(sys)
sys.setdefaultencoding("utf-8")

# baesurl = "http://www.jikexueyuan.com/search/s/q_"
# base_path = "f:/jike/"

headers = {"Host": "www.jikexueyuan.com",
           "Referer" : "http://passport.jikexueyuan.com/sso/login",
           "Upgrade-Insecure-Requests" : "1",
           "Cache-Control":"max-age=0",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
           "Accept-Encoding": "gzip, deflate, sdch",
           "Cookie": "connect.sid=s%3A_F8cMBfnk-Xv6G42FGAd5drtYlmOfhuL.jJwUrM8zo%2B%2FjX%2BhgWGzancvROOEMob%2FwQOpkXM9TTxQ; looyu_id=c868d2b3011f2a0db3fafc52379df2e7ff_20001269%3A1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221543e8a9e58570-06f27d2e9-3b664008-1fa400-1543e8a9e59336%22%7D; stat_uuid=1461338768184864910509; ohterlogin=qq; sso_closebindpop=bindphone; undefined=; _gat=1; stat_fromWebUrl=; stat_ssid=1461820452643; QINGCLOUDELB=84b10773c6746376c2c7ad1fac354ddfd562b81daa2a899c46d3a1e304c7eb2b|Vxpp/|Vxpom; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1461338134,1461345138; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1461348847; looyu_20001269=v%3Ac868d2b3011f2a0db3fafc52379df2e7ff%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DGw_AcXlC2MvUdvDmpW-01eOFMvsWEfhzD9CzxSRYQCnKB-EEefnCHphfSbNzF_p-%2526wd%253D%2526eqid%253D9eeb3aff0010311800000006571a401b%2Cr%3A%2Cmon%3Ahttp%3A//m9104.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/; _99_mon=%5B0%2C0%2C0%5D; stat_isNew=0; _ga=GA1.2.43647688.1461338134; uname=jike_0672750; uid=4268209; code=WTIEH9; authcode=0c9dUHHO1Kuk0IuhcuWLEi7MyXrmLfWIt4K0Oc9vCVMwdKlvhxySUjCYOk8f9UnQn19tyYwPwzxogpn7xMvkNYwYUHepQHISH%2B68LF4HJLuvmjLbHwTohEBofbufy9Un; level_id=3; is_expire=1; domain=4214682474",
           "Connection": "keep-alive",
           "DNT": "1"}

class jike_auto_down:
    basepath = ""
    baseurl = ""
    coursetag = ""
    courseid = ""

    def __init__(self, base_path, base_url):
        if base_path and base_url:
            self.base_path = base_path
            self.base_url = base_url
            self.get_tags()
        else:
            print("base_path and base_url is all must needed!")
            return

    def run(self):
        self.get_tags()

    # get_tags 获取所有便签
    def get_tags(self):
        url = "http://www.jikexueyuan.com/path/"
        tag_html = requests.get(url).text.decode("utf-8").encode("GB18030")
        tag_etree = etree.HTML(tag_html)
        tag_lists = [str(tag).rstrip("/")[str(tag).rstrip("/").rindex("/") + 1:] for tag in
                     tag_etree.xpath('/html/body/div[1]/div[4]/div/div[3]/div/a/@href') if tag]
        if tag_lists:
            for tag in tag_lists:
                print(tag)
                self.course_tag = tag
                self.get_total_page(tag)

    # get_tags 获取课程所有页面 课程分页是js生成不好直接抓取，所以就暴力了
    def get_total_page(self, tag):
        if tag:
            for page in range(1, 50):
                page_url = self.base_url + tag + "?pageNum=%d" % page
                print(page_url)
                exit()
                page_html = requests.get(page_url, headers=headers).text.decode("utf-8").encode("GB18030")
                # print(page_html)
                # exit()
                no_userMenu = re.search(r"userMenu", page_html, re.S)
                if no_userMenu is None:
                    print no_userMenu
                    print("please check the cookies")
                    exit()
                    return
                no_search = re.search(r"no-search", page_html, re.S)
                if no_search:
                    print("the tag ;%s,%d is biggest page" % (tag, page - 1))
                    # return page_url_lists
                    break
                else:
                    # page_url_lists.append(page_url)
                    self.get_course_pages(page_url)
                    # print(page_url)

    # getcoursepages 获取课程详细页面
    def get_course_pages(self, tag_url):
        if tag_url:
            print("the tag_url:%s " % tag_url)
            course_page_lists = self.get_xpath_lists(tag_url, headers,
                                                     '//*[@id="changeid"]/ul/li/div/div[2]/h5/a/@href')
            if course_page_lists:
                for course_page_url in course_page_lists:
                    self.get_down_urls(course_page_url)

    # getdownurls通过正则获取视频下载地址
    def get_down_urls(self, course_page_url):
        if course_page_url:
            self.course_id = course_page_url[course_page_url.rindex("/") + 1:course_page_url.rindex(".")]
            # print(course_page_url)
            print("             course_id:%s %s" % (self.course_id, course_page_url))
            course_down_lists = self.get_xpath_lists(course_page_url, headers,
                                                     '//*[@class="video-list"]/div[2]/ul/li/div/h2/a/@href')
            if course_down_lists:
                for course_down_url in course_down_lists:
                    course_down_html = requests.get(course_down_url, headers=headers).text.decode("utf-8").encode(
                            "GB18030")
                    course_down = re.findall(r'source src="(.*?)"', course_down_html, re.S)
                    if course_down:
                        print("                     %s" % course_down[0])
                        if self.addTasktoXunlei(course_down[0]):
                            # print("                     %s is add success!" % course_down[0])
                            print("                     is add success!")
                            time.sleep(5)

    # getfilelists创建文件夹
    def get_file_lists(self, course_tag, course_id):
        course_path = ""
        if self.base_path and os.path.exists(self.base_path) == False:
            try:
                os.mkdir(self.base_path)
            except Exception:
                print("error :%s" % Exception.message)
                return
        if course_tag and os.path.exists(self.base_path + course_tag) == False:
            try:
                os.mkdir(self.base_path + course_tag)
                # print("%s dir is create success!" % (self.base_path + course_tag))
            except Exception:
                print("dir is create error,the error is %s" % Exception.message)

        tmp = self.base_path + course_tag + "\\" + str(course_id)
        if course_id and os.path.exists(tmp) == False:
            try:
                os.mkdir(tmp)
                course_path = tmp
                # print("%s dir is create success!" % tmp)
            except Exception:
                print("dir is create error,the error is %s" % Exception.message)
                return
        else:
            course_path = tmp
        return course_path

    # getxpathlists 专门解析xpath，不用每次都写
    def get_xpath_lists(self, url, headers, xpath):
        try:
            html = requests.get(url, headers=headers).text.decode("utf-8").encode("GB18030")
            tree = etree.HTML(html)
            lists = [str(plist) for plist in tree.xpath(xpath) if plist]
        except Exception:
            print("get xpath list is error is :%s" % Exception.message)
            return
        return lists

    # addTasktoXunlei 添加迅雷任，必须安装迅雷，还需要对迅雷设置默认不提醒，否则就需要手动点击确定了
    def addTasktoXunlei(self, down_url):
        flag = False
        from win32com.client import Dispatch
        o = Dispatch("ThunderAgent.Agent.1")
        # http: // cv3.jikexueyuan.com / 201508011650 / a396d5f2b9a19e8438da3ea888e4cc73 / python / course_776 / 01 / video / c776b_01_h264_sd_960_540.mp4
        if down_url:
            course_infos = str(down_url).replace(" ", "").replace("http://", "").split("/")
            course_path = self.get_file_lists(self.course_tag, self.course_id)
            try:
                o.AddTask(down_url, course_infos[len(course_infos) - 1], course_path, "", "http://cv3.jikexueyuan.com",
                          1, 0, 5)
                o.CommitTasks()
                flag = True
            except Exception:
                print(Exception.message)
                print("                     AddTask is fail!")
        return flag


if __name__ == "__main__":
    myjike = jike_auto_down("e:\\jike\\", "http://www.jikexueyuan.com/search/s/q_")
    myjike.run()
