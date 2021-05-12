# comparative performance web framework gin vs tornado vs django
# 非正式 开源框架性能对比 简介

### Server sets
### 在预期的受限环境下，服务器受限为如下：
   			processor       : 1
			vendor_id       : AuthenticAMD
			cpu family      : 23
			model           : 24
			model name      : AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
			stepping        : 1
			microcode       : 0x8108109
			cpu MHz         : 2096.064
			cache size      : 512 KB
			physical id     : 2
			siblings        : 1
			core id         : 0
			cpu cores       : 1
			apicid          : 2
			initial apicid  : 2
			fpu             : yes
			fpu_exception   : yes
			cpuid level     : 13
			wp              : yes
			 
    对比三个web框架的get响应性能：调用数从1000 ~ 50000， 并发数从 20~1000
    tornado(python3开源高性能web框架)，django(python3企业级web站点框架)，gin(golang开源高性能web框架)

## set server with three web frameworks  
##	服务设置 三种web框架预期返回内容
	
	gin  >=1.7 && golalng1.13
		get  http://192.168.43.40:8080/user/jack  
			//return  data  Hello jack
		post http://192.168.43.40:8080/user/jack   
			//return json data  
			// {"jack": "admin","message":null,"status": "ok"}
	torando >= 6.1 && python3.8
		get  http://192.168.43.40:8009/user   
			//return json data 
			// default {"name": "tornado","status":"ok"}
		post  http://192.168.43.40:8009/user   
			//return json data 
			//default {"name": "tornado","status":"ok"}

	django >=3.1 && python3.8
		get http://192.168.43.40:2991/user/
			//return json data "{\"name\": \"ghost!\"}"
		post http://192.168.43.40:2991/user/  
			//return json data "{\"name\": \"ghost post!\"}"

## tools
    apacha ab test branch

## execute case 
* 	ab  -n 1000 -c 20 url   # Concurrent 20， 1000 times get

* 	ab  -n 10000 -c 50 url   # Concurrent 50， 10000 times get
* 	ab  -n 10000 -c 100 url   # Concurrent 100， 10000 times get		 

* 	ab  -n 10000 -c 500 url  # Concurrent 500， 10000 times get		
* 	ab  -n 50000 -c 500 url	  # Concurrent 500， 50000 times get	
* 	ab  -n 50000 -c 1000 url  # Concurrent 1000， 50000 times get	

*  methods: post  -p -T , example: -p  test.json -T x-www-form-urlencoded;charset=UTF-8   



## results
## 结果
 
### description line 
*  yellow line example: Connection Times (ms)  Total  46

*  blue line example : Time per request:       21.545 [ms] (mean) 
*  red line example : Time per request:       0.215 [ms] (mean, across all concurrent requests)

####   get request number raise from 1000 to 500000 (with Concurrent 20 to 1000)
![ginget](result/gin_get.gif)

#### when get request number raise from 1000 to 500000 (with Concurrent 20 to 1000)
![tornadoget](result/tornado_get.gif)

#### when request number raise from 1000 to 500000 (with Concurrent 20 to 1000)
![comp_gin_with_tornado](result/comp_gin_tornado_total.gif)


### summary
    gin and tornado have limit with linux open file with Concurrent 1000
    
    gin have lower total Connection Times (ms)
    they are very closer with Time per request:       0.215 [ms] (mean, across all concurrent requests)
    tornado need more Time per request:       21.545 [ms] (mean) 
        that is mean , the user need more time to wait the web server response (only compared to gin)
    django will connection refused on windows (100 concurrents) and apr_pollset_poll: The timeout specified has expired (70007) on linux
    
    so, only in web frameworks performance: gin better than tornado  much better than django
    
    Popularity tornado better than gin because more long history.
    
    that's all. 
 