import psutil

alarm_percent = 90
alarm_var = psutil.disk_usage('/')
ps_list = psutil.pids()
memory_usage = psutil.virtual_memory()


if alarm_var.percent > alarm_percent:
    #print ('warning! free space will end soon!!!')
    with open ('my.html', 'w') as f:
        f.write('<h1 style="color:red;">warning! free space will end soon!!!</h1>\n')
else:
    #print ('you have a lot of free space')
    with open ('my.html', 'w') as f:
        f.write('<h1 style="color:green;">you have a lot of free space</h1>\n')

for i in ps_list:
    process =  psutil.Process(i)
    if process.name() == 'java':
        a = process.name()
        b = process.pid

try:
    if a:
        #print ('java process is running and have pid: {} '.format (b))
        with open ('my.html', 'a') as f:
            f.write('<h2 style="color:green;">java process is running and have pid: {}</h2>\n'.format (b))
except:
    #print ('<h2 style="color:red;">java is over</h2>\n')
    with open ('my.html', 'a') as f:
        f.write('<h2 style="color:red;">java is over</h2>\n')

with open ('my.html', 'a') as f:
    f.write('###***###\n<h3 style="color:blue;">memory is: {}</h3>\n###***###\n<h3 style="color:blue;">disk usage is: {}</h3>\n'.format(alarm_var, memory_usage))
