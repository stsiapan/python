import psutil

alarm_percent = 90
alarm_var = psutil.disk_usage('/')
ps_list = psutil.pids()

if alarm_var.percent > alarm_percent:
    print ('warning! free space will end soon!!!')
else:
    print ('you have a lot of free space')

for i in ps_list:
    process =  psutil.Process(i)
    if process.name() == 'java':
        a = process.name()
        b = process.pid

try:
    if a:
        print ('java process is running and have pid: {} '.format (b))
except:
    print ('java is over')

print ('memory usage: ', psutil.virtual_memory())
print ('disk usage: {}'.format (alarm_var))

