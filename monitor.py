import psutil

ps_list = psutil.pids()

for i in ps_list:
    process =  psutil.Process(i)    
    if process.name() == 'java':
        a = process.name()
        b = process.pid

try:
    if a:
        print ('java process is running and have pid: {0} '.format (b))
except:
    print ('java is over')

print ("memory usage: ",  psutil.virtual_memory())
print ("disk usage: ", psutil.disk_usage('/'))
