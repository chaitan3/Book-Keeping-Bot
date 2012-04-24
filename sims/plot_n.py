from pylab import *
p=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg_errors=[0.021611455147457662, 0.016728286991950003, 0.012447249303605084, 0.0098847748269269824, 0.011042922449361718, 0.0063358424150074723, 0.0056879021122503513, 0.0050229107118635041, 0.0044298348377207544, 0.0045101188388226221, 0.0037522023596860891]
max_errors=[0.042359091770850774, 0.028872363134639603, 0.024052898165116694, 0.015095981522774856, 0.019993544322549503, 0.0096722604921680548, 0.0087145597260604567, 0.0078640746439454859, 0.007050224245622406, 0.0082836018423817718, 0.0060660273647614761]
#p=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#avg_errors=[0.13064415966719378, 0.06668065193589752, 0.041762329011805016, 0.032087372453887632, 0.025940955208013445, 0.020902001927315856, 0.017491418497665633, 0.015251430191803542, 0.013885627880904829, 0.012176964514276323, 0.011514942464426524]
#max_errors=[0.21239150183818203, 0.13538639866599453, 0.084122160747495719, 0.054197295395114649, 0.044296771862364491, 0.034071346137693588, 0.027097041447043252, 0.025724184978861642, 0.022963139885812136, 0.023385019343718602, 0.018861835160912162] 
xlabel('Number of Lasers on each axis')
ylabel('Position error')
plot(p, max_errors, 'r--',label='Maximum error')
plot(p, avg_errors, label='Average error')
legend()
show()

