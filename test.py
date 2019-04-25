#coding=utf-8
import xml.dom.minidom
from readRoadNet import *
import numpy as np
from const import *
from coordTransform_utils import *


dom1 = xml.dom.minidom.Document()
root1 = dom1.createElement('root')
dom1.appendChild(root1)

mMap = readXml('../data/map/map.xml')

ways = mMap.getElementsByTagName('way')

for way in ways:
	tags = way.getElementsByTagName('tag')
	isRoad = False
	newWay = dom1.createElement('way')
	wayId = way.getAttribute('id')
	newWay.setAttribute('id',wayId)
	
	for tag in tags:
		newTag = dom1.createElement('tag')

		k = tag.getAttribute('k').encode('utf-8')
		v = tag.getAttribute('v').encode('utf-8')
		
		newTag.setAttribute('k',k)
		newTag.setAttribute('v',v)
		newWay.appendChild(newTag)
		
		newWay.appendChild(newTag)
		if k == 'highway':
			for item in roadType:
				if v == item:
					isRoad = True


	if not isRoad:
		continue
	print 'get way %s' % wayId
	root1.appendChild(way)

f = open('../data/map/road.xml','w')
dom1.writexml(f,indent='',addindent='\t',newl='\n',encoding='UTF-8')
f.close()

'''
f = open('../data/20161013','r')
dataList = []
for line in f.readlines():
	data = line.split(',')
	data[4] = data[4].strip()
	dataList.append(data)
newList = sorted(dataList,key = lambda x : x[2])
posList = []
for item in newList:
	#posList.append(gcj02_to_bd09(item[3],item[4]))
	#posList.append(gcj02_to_wgs84(float(item[3]),float(item[4])))
	print item[4] + ',' + item[3]
'''
#for item in posList:
	#print str(item[1]) + ',' + str(item[0])
'''
mMap = readXml('../data/map/map.xml')
nodes = readNodes(mMap)
ways = readWays(mMap)

dom1 = xml.dom.minidom.Document()
root1 = dom1.createElement('root')
dom1.appendChild(root1)
for nodeId in nodes:
	node = dom1.createElement('node')
	node.setAttribute('id',nodeId)
	node.setAttribute('lon',nodes[nodeId][0])
	node.setAttribute('lat',nodes[nodeId][1])
	root1.appendChild(node)

f = open('../data/map/node.xml','w')
dom1.writexml(f,indent='',addindent='\t',newl='\n',encoding='UTF-8')
f.close()
'''