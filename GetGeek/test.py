import requests

#cookies = {'Cookie' : 'connect.sid=s%3A_F8cMBfnk-Xv6G42FGAd5drtYlmOfhuL.jJwUrM8zo%2B%2FjX%2BhgWGzancvROOEMob%2FwQOpkXM9TTxQ; looyu_id=c868d2b3011f2a0db3fafc52379df2e7ff_20001269%3A1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221543e8a9e58570-06f27d2e9-3b664008-1fa400-1543e8a9e59336%22%7D; stat_uuid=1461338768184864910509; ohterlogin=qq; sso_closebindpop=bindphone; undefined=; _gat=1; stat_fromWebUrl=; stat_ssid=1461820452643; QINGCLOUDELB=84b10773c6746376c2c7ad1fac354ddfd562b81daa2a899c46d3a1e304c7eb2b|Vxpp/|Vxpom; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1461338134,1461345138; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1461348847; looyu_20001269=v%3Ac868d2b3011f2a0db3fafc52379df2e7ff%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DGw_AcXlC2MvUdvDmpW-01eOFMvsWEfhzD9CzxSRYQCnKB-EEefnCHphfSbNzF_p-%2526wd%253D%2526eqid%253D9eeb3aff0010311800000006571a401b%2Cr%3A%2Cmon%3Ahttp%3A//m9104.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/; _99_mon=%5B0%2C0%2C0%5D; stat_isNew=0; _ga=GA1.2.43647688.1461338134; uname=jike_0672750; uid=4268209; code=WTIEH9; authcode=0c9dUHHO1Kuk0IuhcuWLEi7MyXrmLfWIt4K0Oc9vCVMwdKlvhxySUjCYOk8f9UnQn19tyYwPwzxogpn7xMvkNYwYUHepQHISH%2B68LF4HJLuvmjLbHwTohEBofbufy9Un; level_id=3; is_expire=1; domain=4214682474'}
cookies = {'Cookie' : 'ooyu_id=c868d2b3011f2a0db3fafc52379df2e7ff_20001269%3A1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221543e8a9e58570-06f27d2e9-3b664008-1fa400-1543e8a9e59336%22%7D; stat_uuid=1461338768184864910509; ohterlogin=qq; sso_closebindpop=bindphone; uname=jike_0672750; uid=4268209; code=WTIEH9; authcode=0c9dUHHO1Kuk0IuhcuWLEi7MyXrmLfWIt4K0Oc9vCVMwdKlvhxySUjCYOk8f9UnQn19tyYwPwzxogpn7xMvkNYwYUHepQHISH%2B68LF4HJLuvmjLbHwTohEBofbufy9Un; level_id=3; is_expire=1; domain=4214682474; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1461338134,1461345138; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1461348891; XSRF-TOKEN=eyJpdiI6Ik50OVRSS05lK2o2OXlqVEdIQXZwTXc9PSIsInZhbHVlIjoiSFBNVDNNTTJ4cEdFZkRPbjYwSDByYnJ4bkRuRUVsWmNQYnBGQzZJR013OXkxczZFWGpuQkpNbEtzQW5HVzFDMTlzUXZMeUZUZ3pJVlR1N0E4ZzlVWEE9PSIsIm1hYyI6Ijk4NzJkZmEzNWEyZjQ4MGQyMzUzOWIxY2NiZmIwMjRiZmJiZTdkYTc2MDFkNDE0NjQ0NGNkNmI5NGNlZDE5ZWUifQ%3D%3D; laravel_session=eyJpdiI6InRBMHdLRms5MUNPUkl2ZjdoNUROXC9RPT0iLCJ2YWx1ZSI6Ilp5VDRHeEVtRHJVdE5EUUtWZklFRkRPcHlxU1F0KzFNcUVVQmdwbGtpRWY0REZyZTZjQjJ4RkNRNThsQVwvZTFCajJHS2hIN3UwOGVwMXVNNXN0K2hCUT09IiwibWFjIjoiYzhkMTI4OGVmNzg4YmJhN2JiOWZkNzgxNDIzMTNkMmFhNmU1NTI1ZGJlZTI5ODQxNTUyNjc2OTU2OWQxYTdhNiJ9; QINGCLOUDELB=1bb571da02dcd2ad08ff904df3dac9a3d562b81daa2a899c46d3a1e304c7eb2b|VxptT|Vxpp+; stat_fromWebUrl=; undefined=; stat_ssid=1461851438512; stat_isNew=0; Hm_lvt_532e28cc3b6b596b381c569d4e6cd0e4=1461338773,1461338786; Hm_lpvt_532e28cc3b6b596b381c569d4e6cd0e4=1461349696; _ga=GA1.2.43647688.1461338134; looyu_20001269=v%3Ac868d2b3011f2a0db3fafc52379df2e7ff%2Cref%3Ahttps%253A//www.baidu.com/link%253Furl%253DGw_AcXlC2MvUdvDmpW-01eOFMvsWEfhzD9CzxSRYQCnKB-EEefnCHphfSbNzF_p-%2526wd%253D%2526eqid%253D9eeb3aff0010311800000006571a401b%2Cr%3A%2Cmon%3Ahttp%3A//m9104.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/; _99_mon=%5B0%2C0%2C0%5D'}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
#url = 'http://search.jikexueyuan.com/course/?q=android'
#url = 'http://www.jikexueyuan.com'
url = 'http://www.jikexueyuan.com/course/26.html'

html = requests.get(url,headers=headers,cookies=cookies)

print html.content
