import napalm
from napalm_ros import ros
from pprint import pprint as pp

cisco_device_ip_list = ['192.168.100.101']
junos_device_ip_list = ['192.168.100.102']
arista_device_ip_list = ['192.168.100.103']
mikrotik_device_ip_list = ['192.168.100.104']

print('###################################START AUTOMATION####################################')
for ip_device in cisco_device_ip_list:
	print('Connecting to cisco device ip '+ str(ip_device))
	driver = napalm.get_network_driver('ios')
	device = driver(hostname=ip_device, username='cisco', password='cisco123')
	device.open()
	pp(device.get_facts())
	device.close()
	print('-------------------------------------------------------------------------------')

print('#######################################################################################')

for ip_device in junos_device_ip_list:
	print('Connecting to junos device ip '+ str(ip_device))
	driver = napalm.get_network_driver('junos')
	device = driver(hostname=ip_device, username='root', password='root123')
	device.open()
	pp(device.get_facts())
	device.close()
	print('--------------------------------------------------------------------------------')

print('########################################################################################')

for ip_device in arista_device_ip_list:
	print('Connecting to arista device ip '+ str(ip_device))
	driver = napalm.get_network_driver('eos')
	device = driver(hostname=ip_device, username='admin', password='admin123')
	device.open()
	pp(device.get_facts())
	device.close()
	print('--------------------------------------------------------------------------------')

print('########################################################################################')
for ip_device in mikrotik_device_ip_list:
	print('Connecting to mikrotik device ip '+ str(ip_device))
	driver = napalm.get_network_driver('ros')
	device = driver(hostname=ip_device, username='admin', password='', optional_args={'port':8728})
	device.open()
	pp(device.get_facts())
	device.close()
	print('--------------------------------------------------------------------------------')

print('###########################################END##########################################')
