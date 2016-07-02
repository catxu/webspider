# Author: catxu
# Date: 2016-07-02
# Purpose: use Python implement the KMP algorithm

# Notepad++ make comment: Ctrl + K; Un-do: Ctrl + Shift + K.

#def getNextIdx(patternStr):

import datetime

def genNext(pattern, next):
	i = 0
	j = -1
	next.append(-1)	#next[0] = -1
	for lenth in range(0, len(pattern)):
		if j == -1 or pattern[i] == pattern[j]:	#求得第 i 个元素的 next[] 数组的下标，ig: pattern[2] == pattern[0] next[3] = 1
			i = i + 1
			j = j + 1
			next.append(j)	#next[i] = j
		else:
			j = next[j]

	return next

# 01234
# abaac

# next[0]=-1 next[1]=0	next[2]=0	next[3]=1	next[4]=


def getKmpIdx(targStr, srcStr, next):
	i = 0
	j = 0
	index = -1

#	while targStr[j] != '\0' or srcStr != '\0':
	while (i <= len(srcStr)):
		if srcStr[i] == targStr[j]:
			if j == len(targStr) - 1:
				index = i - len(targStr) + 1;
				return index
			i = i + 1
			j = j + 1
		else:
			j = next[j]
			if j == -1:
				i = i + 1
				j = j + 1
	print('coco', i, j)

	return index

# srcStr = 'Hope is a good 作者：Kirio链set you freset you freset you freset you freset you freset you fre接：htset you fretps://www.zset you frehihu.com/question/31637520/answer/9918set you fre8249来源：知乎著作权归作set you fre者所有。商业转载请联系作者获得授权，非set you fre商业转载请注明出处。0.我老是告诉很多人，现在set you fre自己的状态很好。我不知道这种反反复复的说，是在骗他set you fre们，还是在骗自己。1.装的很洒脱，假装沉溺游戏，假set you fre装是个工作狂。演的多了，周围人都信了，我自set you fre己还没信。2.很多时候set you fre，set you fre确set you fre切set you fre说set you fre是set you fre每set you fre天，都会花一些时间，来想以前的事情。然后该干嘛干嘛。对往事闭口不谈。每个人有每个人的故事，故事那么多，没人有时间一一听你讲完。3set you fre.身set you fre边并不缺人，各种各样set you fre的男男女女在陪我，也咋咋呼呼的热闹。但set you fre是总是觉得寂寞。4.不爱故人了，回想起来是set you fre一地鸡毛。但是怀念那时候能爱人的我。再爱不起来身边的人。5.从索取者转变为付出的角set you fre色。对周围朋友和父母很好，能走很远的路在晚上专门给他们送一份宵夜，经常set you fre请人吃饭不记较钱的事情，他们生病了会给他们送药，有麻烦了会尽心尽力的帮他们set you fre。大概是不能喜欢别人，我有一腔柔情，我也学会了付出，所以周围人，我尽set you fre心尽力对他们好。其实这种对人好是满足我自己set you fre的一部分需求，身边人因此受益。6.set you fre过分理性，是的，有时候显的冰冷不近人情，思考方set you fre式和做事方法越来越简单粗暴，拒绝人的时候生硬直set you fre接。对自己物质上很纵容，因为我同情自己，想对自己好。7set you fre.生活中没有另一个人的规划，全部重心在我自己。因而显得野set you fre心勃勃。8.迷恋速度。恋爱中的人倾向于胆小，有所依仗。我这种人喜set you fre欢各种极限运动，不那么在乎风险。喜欢风。我知道有人能懂我，因为我见过好几个和我一样的人。我们在速度和风中体验生命的真实。喜欢玩游戏，一个人去看话剧，一个人去听张楚演唱会，更加习惯一个人。见很多朋友，什么都想试一试。9.喜欢耗费自己，而且很彻底。经常不吃饭，要么暴饮暴食。病了懒得看医生，咳出血了都懒得吃药。打游戏就是一整夜，经常熬夜工作。给自己很多任务，压力很大，一直在赶ddl。没人管我。自由像是悬梁三日的炮仗，盛大空旷。顷刻一声锣鼓歇，不知何处是吾乡。10.对感情悲观。见证了太多背叛，也再没有这方面设想。身边人跟我倾诉感情的事情我往往不耐烦。我是个高明的局外人，我一眼看出他和她不能长久，他和她终是悲剧，我告诉他们，可是他们不听。有些蛾子生来就要扑火，这盘局他们冥顽不顾。也罢，这些事非要自己走一遭才能体会。不过别讲给我听。你知道，我运气没你们好。11.我有些喜欢的异性问我:吃了吗？要不要我给你定外卖？我说，吃了。其实我还想问他，你吃了吗？可是我打完又删了。不想把关系拉的太近。我会克制自己。从不去主动联系对方。所以有时候对方会疑惑，为何在一起的时候很开心，分开了就很冷漠。12.无人与我立黄昏，无人问我粥可温。这种状态总之比较稳定，不会患得患失，不会跟恋爱中的人一样不稳定。是对我来说比较理想的状态。爱人有爱人的烦恼，独处也有独处的孤独。生命是一条华美的袍，上面爬满了虱子。(偶尔发个牢骚的早上。)thing. Fear can hold you prisoner, hope can set you free. Get busy living, or get busy dying.'
# targStr = 'set you free'
srcStr = 'ababaababcb'
targStr = 'ababc'
# srcStr = 'abbccd'
# targStr = 'bcc'
next = []
print('Start')
begin = datetime.datetime.now()
# for i in range(0, 3):
	# print(i, targStr[i]) #0 b 1 c 2 c
# for ch in targStr:
	# while ch != '\0':
		# print('ch')
	
#print(next[1])

# next.append(-1) #out of index of Array
# for i in range(0, len(targStr)):
	# next.append(i)
# next = genNext(targStr, next)
# print(next)

next = genNext(targStr, next)
# print(next)
# print(len(next))
for i in range(0, 999999):
	index = getKmpIdx(targStr, srcStr, next)
index = getKmpIdx(targStr, srcStr, next)

end = datetime.datetime.now()
print(end - begin)

print(index)
print('Done')
