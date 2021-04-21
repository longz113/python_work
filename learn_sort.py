#冒泡排序
def bubbleselect(sortedlist):
      for passnum in range(len(sortedlist)-1,0,-1):
            for i in range(passnum):
                  if sortedlist[i]>sortedlist[i+1]:
                        sortedlist[i],sortedlist[i+1]=sortedlist[i+1],sortedlist[i]
      return sortedlist

#选择排序
def selectionsort(sortedlist):
      for fillslot in range(len(sortedlist)-1,0,-1):
            maxvalue=sortedlist[0]
            pointmax=0
            for pointlocation in range(fillslot+1):
                  if sortedlist[pointlocation]>maxvalue:
                        maxvalue=sortedlist[pointlocation]
                        pointmax=pointlocation
            sortedlist[fillslot],sortedlist[pointmax]=maxvalue,sortedlist[fillslot]
      return sortedlist

#归并排序
def mergesort(alist):
      if len(alist)>1:
            mid=len(alist)//2
            lefthalf=alist[:mid]
            righthalf=alist[mid:]

            mergesort(lefthalf)
            mergesort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                  if lefthalf[i]<righthalf[j]:
                        alist[k]=lefthalf[i]
                        i=i+1
                  else:
                        alist[k]=righthalf[j]
                        j=j+1
                  k=k+1
            while i<len(lefthalf):
                  alist[k]=lefthalf[i]
                  i=i+1
                  k=k+1
            while j<len(righthalf):
                  alist[k]=righthalf[j]
                  j=j+1
                  k=k+1
      return alist
































