import subprocess
import numpy as np

p1 = subprocess.Popen(['cat', 'a.scr'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['prsim', 'a.prs'], stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen(['grep', ' : '], stdin=p2.stdout, stdout=subprocess.PIPE)
p4 = subprocess.Popen(['sed', '-r', '-e s/0 .*://'], stdin=p3.stdout, stdout=subprocess.PIPE)
dat = p4.communicate()[0]
x = np.fromstring(dat, dtype=int, sep=' ')
times = x[::2]
values = x[1::2]
times0 = times[values==0]
times1 = times[values==1]
dtimes = np.diff(times)
dtimes0 = np.diff(times0)
dtimes1 = np.diff(times1)
print 'times:', times
print 'values:', values
print 'times0:', times0
print 'times1:', times1
print 'diff(times):', dtimes
print 'diff(times0):', dtimes0
print 'diff(times1):', dtimes1

dt = dtimes0[0]
period_ps = 60*dt
freq_MHz = 1./period_ps/1E-6
print 'period: %d ps' % period_ps
print 'freq: %f MHz' % freq_MHz
