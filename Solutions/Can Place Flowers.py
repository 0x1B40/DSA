class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # flowerbed = [ 0, 1 , 0 , 1 , 1 ,1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
        # Calculate the number of flowerbeds implantable, compare it with n
        #  [0, 0 , 0 , 0 , 0]
        # [1, 0, 0 , 0, 1]
        # [ 1, 1, 0, 0, 1]
        length = len(flowerbed)
        counter = 0

        if(length == 1):
            if(flowerbed[0] ==0):
                counter +=1
                flowerbed[0] = 1

        for i in range(length):
            
            if( length >=2):
                if( i == 0):
                    if(flowerbed[i] == 0 and flowerbed[i+1]==0):
                        flowerbed[i] = 1
                        counter += 1
                elif(i==length-1):
                    if(flowerbed[length-1] == 0 and flowerbed[length-2] ==0 ):
                        flowerbed[length-1] = 1
                        counter += 1
                else:
                    if((flowerbed[i]==0) and (flowerbed[i-1] == 0) and (flowerbed[i+1] ==0)):
                        flowerbed[i] = 1
                        counter += 1 

        print("counter is: " + str((counter)))
        print("flowerbed array: " + str(flowerbed))
        
        if(n <= counter):
            return True
        else:
            return False

    
            


        