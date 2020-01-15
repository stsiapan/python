import psutil

alarm_percent = 90
alarm_var = psutil.disk_usage('/')
ps_list = psutil.pids()
memory_usage = psutil.virtual_memory()
delimeter = "####****####"

disk_u = {
    'total disk usage (Gb):': alarm_var.total/1024000000.,
    'used disk usage (Gb):': alarm_var.used/1024000000.,
    'percent disk usage (%):': alarm_var.percent
}

mem_u = {
    'total memory (Gb):': memory_usage.total/1024000000.,
    'available memory (Gb):': memory_usage.total/1024000000.,
    'used memory (Gb):': memory_usage.used/1024000000.,
    'free memory (Gb):': memory_usage.free/1024000000.,
    'percent (%):': memory_usage.percent
}

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

for i in disk_u:
    #print i, disk_u[i]
    with open ('my.html', 'a') as f:
        for i in disk_u:
            f.write('<h3 style="color:brown;">{} {}</h3>\n'.format(i, disk_u[i]))

for i in mem_u:
    # print i, mem_u[i]
    with open ('my.html', 'a') as f:
        for i in mem_u:
            f.write('<h3 style="color:blue;">{} {}</h3>\n'.format(i, mem_u[i]))
