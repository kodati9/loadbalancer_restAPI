from subprocess import check_output 
import json
import subprocess
import time

	
print('loadbalancer starts......')
print(' ')
print('Set thresold : 2000pkts/sec ')
threshold = 2000
print(' ')
 
delete_rule1='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1-1", "cookie":"0", "priority":"32767", "in_port":"1","active":"false", "actions":"output=4"}'

response=subprocess.call(['curl','-X','POST','-d',delete_rule1,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)

delete_rule2='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"32767", "in_port":"1","active":"false", "actions":"output=5"}'
response=subprocess.call(['curl','-X','POST','-d',delete_rule2,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)


delete_rule3 ='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-2-1", "cookie":"0", "priority":"32767", "in_port":"2","active":"false", "actions":"output=4"}'
response=subprocess.call(['curl','-X','POST','-d',delete_rule3,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)


delete_rule4 ='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-2-2", "cookie":"0", "priority":"32767", "in_port":"2","active":"false", "actions":"output=5"}'
response=subprocess.call(['curl','-X','POST','-d',delete_rule4,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)


delete_rule5 ='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-3-1", "cookie":"0", "priority":"32767", "in_port":"3","active":"false", "actions":"output=4"}'
response=subprocess.call(['curl','-X','POST','-d', delete_rule5,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)


delete_rule6 ='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-3-2", "cookie":"0", "priority":"32767", "in_port":"3","active":"false", "actions":"output=5"}'
response=subprocess.call(['curl','-X','POST','-d',delete_rule6,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)

add_rule1='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1-1", "cookie":"0", "priority":"32768","ipv4_src":"10.0.0.1/255.0.0.0","eth_type":"0x0800","eth_src":"ca:86:80:1c:6b:95","ipv4_dst":"10.0.0.4/255.0.0.0","eth_dst":"86:b6:67:1e:30:cb","in_port":"1","active":"true", "actions":"output=4"}'
response=subprocess.call(['curl','-X','POST','-d',add_rule1,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)

add_rule2='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-2-1", "cookie":"0", "priority":"32768","ipv4_src":"10.0.0.2/255.0.0.0","eth_type":"0x0800","eth_src":"1a:3b:57:0c:37:58","ipv4_dst":"10.0.0.4/255.0.0.0","eth_dst":"86:b6:67:1e:30:cb","in_port":"2","active":"true", "actions":"output=4"}'
response=subprocess.call(['curl','-X','POST','-d',add_rule2,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print(response)


add_rule3='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-3-1", "cookie":"0", "priority":"32768","ipv4_src":"10.0.0.3/255.0.0.0","eth_type":"0x0800","eth_src":"be:62:69:0a:90:56","ipv4_dst":"10.0.0.4/255.0.0.0","eth_dst":"86:b6:67:1e:30:cb","in_port":"3","active":"true", "actions":"output=4"}'
response=subprocess.check_output(['curl','-X','POST','-d',add_rule3,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
print("Actual reponse")

print('')
while(1):
	enable = ''

	response = subprocess.call(['curl','-X','POST','-d',enable,'http://10.0.2.12:8080/wm/statistics/config/enable/json'])
	print("Response 2", response)

        statistics_port_5 = ''
	response = subprocess.check_output(['curl','-X','GET','-d',statistics_port_5,'http://10.0.2.12:8080/wm/statistics/bandwidth/00:00:00:00:00:00:00:01/5/json'])
	print("Final response", response)
	statistics_port_4 = ''
	response = subprocess.check_output(['curl','-X','GET','-d',statistics_port_4,'http://10.0.2.12:8080/wm/statistics/bandwidth/00:00:00:00:00:00:00:01/4/json'])
	print("Final response", response)
        
        
	loadingjson = json.loads(response)
	print(loadingjson[0]["bits-per-second-tx"])

	k = loadingjson[0]["bits-per-second-tx"]

	print(type(k))
	k = int(k)
	print(type(k))
	if (k >= threshold):
  		print("threshold exceeded")
                delete_rule1='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1-1", "cookie":"0", "priority":"32767", "in_port":"1","active":"false", "actions":"output=4"}'

                response=subprocess.call(['curl','-X','POST','-d',delete_rule1,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
                print(response)
  		add_rule4='{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1-2", "cookie":"0", "priority":"32768","ipv4_src":"10.0.0.1/255.0.0.0","eth_type":"0x0800","eth_src":"ca:86:80:1c:6b:95","ipv4_dst":"10.0.0.4/255.0.0.0","eth_dst":"86:b6:67:1e:30:cb","in_port":"1","active":"true", "actions":"output=5"}'
  		response=subprocess.call(['curl','-X','POST','-d',add_rule4,'http://10.0.2.12:8080/wm/staticentrypusher/json'])
  		print(response)
	time.sleep(5)
 
  
   
  






