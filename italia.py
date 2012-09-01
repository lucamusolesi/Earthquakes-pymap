from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'i' means use intermediate resolution coastlines.
# lon_0, lat_0 are the central longitude and latitude of the projection.
m = Basemap(llcrnrlon=10,llcrnrlat=44.3,urcrnrlon=13,urcrnrlat=45.2,\
            resolution='f',area_thresh=1000.,projection='poly',\
            lat_0=45,lon_0=10)
# m = Basemap(llcrnrlon=6,llcrnrlat=43,urcrnrlon=15,urcrnrlat=48,\
#             resolution='f',area_thresh=1000.,projection='poly',\
#             lat_0=45,lon_0=10)


# can get the identical map this way (by specifying width and
# height instead of lat/lon corners)
#m = Basemap(width=891185,height=1115557,\
#            resolution='i',projection='cass',lon_0=-4.36,lat_0=54.7)
#m.drawcoastlines()
# draw parallels and meridians.
m.drawparallels(np.arange(-40,61.,2.))
m.drawmeridians(np.arange(-20.,21.,2.))
#m.drawmapboundary(fill_color='aqua') 
m.drawrivers(linewidth=0.5, color='k', antialiased=1, ax=None, zorder=None)
m.drawcountries(linewidth=0.5, color='k', antialiased=1, ax=None, zorder=None)
m.drawlsmask(land_color='0.8', ocean_color='b', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=True, resolution='h', grid=1.25)




#Read data
cr = csv.reader(open("last.csv","rb"))
lats, longs, magn = [], [], []

for row in cr:
    lats.extend([row[0]])
    longs.extend([row[1]])
    magn.extend([row[2]])
 
lats_ = [float(aa) for aa in lats]
longs_= [float(bb) for bb in longs]
magn_ = [float(cc) for cc in magn]

# lat/lon coordinates
# lats = [44.882, 44.831]
# longs = [11.383, 11.490]
# magn = [4.1, 5.1]

# compute the native map projection coordinates for cities
x,y = m(longs_,lats_)

#scale magnitude to emphasise different relative intensity
s_magn = [p * p * p for p in magn_]




number = range(len(magn_))
#scatter scaled circles at the city locations
for magni, xpt, ypt, i in zip(s_magn, x, y, number):
    m.scatter(
        xpt,
        ypt,
        s=magni, #size
        c='red', #color
        marker='o', #symbol
        alpha=0.25, #transparency
        zorder = 2, #plotting order
        )
    plt.savefig('image/00'+str(i)+'.jpg')



# plt.title("Italian Earthquakes")
# plt.show()
#plt.savefig('italia.png')