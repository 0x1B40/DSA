class Solution:
    def compress(self, chars: List[str]) -> int:

        length = len(chars)
        compressed = []
        print("chars length: " + str(length))

        if length > 0:
            target_char = chars[0]
            counter = 1
        
        

        for i in range (1,length):
            print(f"chars {i} " + chars[i])
            if(target_char == str(chars[i])):
                counter = counter + 1
                
            else:
                compressed.append(str(target_char))
                print("previous target_char "+ str(target_char))
                target_char = chars[i]
                print("next target_char "+ str(target_char))
               
                if(counter > 1):
                    for char in str(counter):
                        compressed.append(str(char))
                        print("char counter " + str(char) + " appended"  )
                counter = 1

                print("current compressed " + str(compressed))
            
        
        compressed.append(target_char)
        if(counter > 1):
            for char in str(counter):
                compressed.append(str(char))
                print("char counter " + str(char) + " appended"  )

        total_length = len(compressed)
        print("compressed:"  + str(compressed))
        print("length: " + str(total_length))
        
        print(chars)

        for i in range(len(compressed)):
            chars[i] = list(compressed)[i]
        
        return len(chars[:len(compressed)]) 





                    