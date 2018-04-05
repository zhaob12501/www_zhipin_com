# -*- coding: utf-8 -*-
import scrapy
import time
import datetime
from www_zhipin_com.items import WwwZhipinComItem


class ZhipinSpider(scrapy.Spider):
	# spider的名字定义了Scrapy如何定位（并初始化）spider，所以其必须是唯一的。不过您可以生成多个相同的spider实例（instance），这没有任何限制。name是spider最重要的属性，而且是必须的
	name = 'zhipin'

	# 可选。包含了spider允许爬取的域名（domain）列表（list）。当OffsiteMiddleware启用时，域名不在列表中的URL不会被跟进。
	allowed_domains = ['www.zhipin.com']

	# URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。
	# 这里我们进行了指定，所以不是从这个URL列表里爬取
	start_urls = ['https://www.zhipin.com']

	# 要爬取的页面，可以改为自己需要搜的条件，这里搜的是 北京-python， 其他条件都是不限
	# 北京、上海、广州、深圳、杭州、天津、西安、苏州、武汉、厦门、成都、郑州
	positionUrls = ['https://www.zhipin.com/c101010100/h_101010100/?query=', # 北京
					'https://www.zhipin.com/c101020100/h_101010100/?query=', # 上海
					'https://www.zhipin.com/c101280100/h_101010100/?query=', # 广州
					'https://www.zhipin.com/c101280600/h_101010100/?query=', # 深圳
					'https://www.zhipin.com/c101210100/h_10101010/?query=',  # 杭州
					'https://www.zhipin.com/c101030100/h_10101010/?query=',  # 天津
					'https://www.zhipin.com/c101110100/h_10101010/?query=',  # 西安
					'https://www.zhipin.com/c101190400/h_10101010/?query=',  # 苏州
					'https://www.zhipin.com/c101200100/h_10101010/?query=',  # 武汉
					'https://www.zhipin.com/c101230200/h_10101010/?query=',  # 厦门
					'https://www.zhipin.com/c101250100/h_10101010/?query=',  # 成都
					'https://www.zhipin.com/c101180100/h_10101010/?query=']  # 郑州
	positions = ['python', 'php', 'java', '前端', 'C++', 'iOS', 'Android']

	curPage = 1  # 当前开始跑的页码
	curPositionUrlIndex = 0  # 当前跑的第几个城市
	curPositionIndex = 0  # 当前跑的第几个岗位
	
	# 发送 headers， 伪装为浏览器
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'cache-control': 'max-age=0',
		# 'cookie': 'lastCity=101010100; t=ihwwU9HNfhcMv2Qs; wt=ihwwU9HNfhcMv2Qs; JSESSIONID=""; __c=1522995715; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1522486111,1522494470,1522583104,1522995715; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1522995874; __a=66639934.1512268251.1522583104.1522995715.274.35.7.213',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831",
		'dnt': "1",
		'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
	}

	# 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
	# 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
	def start_requests(self):
		return [self.next_request()]

	# 负责处理response并返回处理的数据以及(/或)跟进的URL。
	def parse(self, response):
		print("request -> " + response.url)
		# CSS 定位
		# job_list = response.css('div.job-list > ul > li')

		# Xpath 定位
		job_list = response.xpath('//div[@class="job-list"]/ul/li')

		for job in job_list:
			item = WwwZhipinComItem()

			# 职位信息
			primary_info = job.xpath('./div/div[@class="info-primary"]')
			# 公司信息
			company_info = job.xpath('./div/div[@class="info-company"]')
			# 其他信息
			publis_info = job.xpath('./div/div[@class="info-publis"]')



			# 职位ID
			item['pid'] = primary_info.xpath('./h3/a/@data-jobid').extract_first().strip()
			# 职位名称
			item["positionName"] = primary_info.xpath('./h3/a/div[@class="job-title"]/text()').extract_first().strip()
			# 薪资
			item["salary"] = primary_info.xpath('./h3/a/span/text()').extract_first().strip()
			# 职位标签(网站已删除该内容)
			# item['positionLables'] = primary_info.xpath('./h3/a/div/div[@class="tags"]/span/text()').extract()
			# 职位描述(暂不可用)
			# item['introduction'] = primary_info.xpath('./h3/a/div/div/div/div[@class="detail-bottom-text"]p/text()').extract()

			primary = primary_info.xpath('./p/text()').extract()

			# 工作地址
			item['city'] = primary[0].strip()
			# 工作时间（年限）
			item['workYear'] = primary[1].strip()
			# 学历
			item['education'] = primary[2].strip()


			# 公司名称
			item['companyShortName'] = company_info.xpath('./div/h3/a/text()').extract_first().strip()

			company_infos = company_info.xpath('./div/p/text()').extract()

			if len(company_infos) == 3: # 有一条招聘这里只有两项，所以加个判断
				# 公司类型
				item['industryField'] = company_infos[0].strip()
				# 融资情况
				item['financeStage'] = company_infos[1].strip()
				# 公司规模
				item['companySize'] = company_infos[2].strip()
			else:
				item['industryField'] = company_infos[0].strip()
				item['financeStage'] = ''
				item['companySize'] = company_infos[1].strip()

			
			# 更新时间
			item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

			# 发布时间
			t = publis_info.xpath('./p/text()').extract_first().strip('发布于')
			if t == '昨天':
				oneday = datetime.timedelta(days=1)
				today = datetime.date.today()
				yesterday = today - oneday
				item['time'] = yesterday.__str__()
			elif ':' in t :
				item['time'] = time.strftime("%Y-%m-%d", time.localtime())
			else:
				item['time'] = '{}-{}-{}'.format(time.strftime("%Y", time.localtime()), t[0:2], t[3:5])

			yield item

		if self.curPage == 20:
			self.curPage = 1
			self.curPositionUrlIndex += 1
			if self.curPositionUrlIndex > len(self.positionUrls):
					self.curPositionIndex += 1
		else:
			self.curPage += 1

		time.sleep(10)
		yield self.next_request()

	# 发送请求
	def next_request(self):
		return scrapy.http.FormRequest(
			self.positionUrls[self.curPositionUrlIndex] + (
				 "%s&page=%d&ka=page-%d" % (self.positions[self.curPositionIndex], self.curPage, self.curPage)),
			headers=self.headers,
			callback=self.parse
		)
