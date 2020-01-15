import psutil

alarm_percent = 90
alarm_var = psutil.disk_usage('/')
ps_list = psutil.pids()
memory_usage = psutil.virtual_memory()
human_read = 1024000000.

disk_u = {
    'total disk usage (Gb):': alarm_var.total/human_read,
    'used disk usage (Gb):': alarm_var.used/human_read,
    'percent disk usage (%):': alarm_var.percent
}

mem_u = {
    'total memory (Gb):': memory_usage.total/human_read,
    'available memory (Gb):': memory_usage.total/human_read,
    'used memory (Gb):': memory_usage.used/human_read,
    'free memory (Gb):': memory_usage.free/human_read,
    'percent (%):': memory_usage.percent
}

if alarm_var.percent > alarm_percent:
    with open ('my.html', 'w') as f:
        f.write('<h1 style="color:red;">warning! free space will end soon!!!</h1>\n')
else:
    with open ('my.html', 'w') as f:
        f.write('<h1 style="color:green;">you have a lot of free space</h1>\n')

for i in ps_list:
    process =  psutil.Process(i)
    if process.name() == 'java':
        a = process.name()
        b = process.pid

try:
    if a:
        with open ('my.html', 'a') as f:
            f.write('<h2 style="color:green;">java process is running and have pid: {}</h2>\n'.format (b))
except:
    with open ('my.html', 'a') as f:
        f.write('<h2 style="color:red;">java is over</h2>\n')

with open ('my.html', 'a') as f:
    for i in disk_u:
        f.write('<h3 style="color:brown;">{} {}</h3>\n'.format(i, disk_u[i]))

with open ('my.html', 'a') as f:
    for i in mem_u:
        f.write('<h3 style="color:blue;">{} {}</h3>\n'.format(i, mem_u[i]))
