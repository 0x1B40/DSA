class Solution(object):
    def reverseWords(self, s):

        #find all the words, put them in a list
        # reverse them
        # output or return

        def findWords(string):
            list_of_words = []
            string =string.strip()
            #"   ahmed   is  ali what how mean?"
            
            while(string.find(" ") != -1):
                last_index=string.find(" ")
                list_of_words.append(string[:last_index])
                string =string[last_index:].strip()
            
            list_of_words.append(string)


            print("list of words: " + str(list_of_words))

            return list_of_words

        
        list_of_words =findWords(s)

        list_of_words = list_of_words[::-1]
        string = ""
        for word in list_of_words:
            string =  string + " " + word

        string =string.strip()
        return string 








        """
        :type s: str
        :rtype: str
        """
        