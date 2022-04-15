class Solution(object):
    ''' Extra spaces between words should be distributed as evenly as possible. 
        If the number of spaces on a line do not divide evenly between words, 
        the empty slots on the left will be assigned more spaces than the slots on the right. '''
    def fillSpaces(self, words, maxWidth, final):
        wlist = words.split();
        if len(wlist) == 0: return maxWidth*" "
        wlen = 0;
        for word in wlist: wlen += len(word)
        num_words = len(wlist)
        num_spaces = maxWidth - wlen
        if num_words > 1:
            mean_spaces = num_spaces / (num_words - 1)
            remain_spaces = num_spaces % (num_words - 1)
        else:
            mean_spaces = 0
            remain_spaces = num_spaces
        new_word = ""
        for word in wlist:
            if new_word != "":
                if final == 1: new_word += " "
                else:
                    new_word += mean_spaces*" "
                    if remain_spaces:
                        new_word += " "
                        remain_spaces -= 1
            new_word += word
        if len(new_word) < maxWidth: new_word += (maxWidth - len(new_word))*" "
        return new_word
        
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0: return [""]
        curlen = 0
        buf = ""
        ret = []
        for word in words:
            lw = len(word)
            trylen = curlen + lw
            if buf != "": trylen += 1
            if trylen > maxWidth or buf == "":
                if lw != 0 and buf != "": ret.append(self.fillSpaces(buf, maxWidth, 0))
                buf = word
                curlen = lw
            else:
                buf += " " + word
                curlen = curlen + lw + 1;
        if len(buf) != 0: ret.append(self.fillSpaces(buf, maxWidth, 1))
        if len(ret) == 0: return [maxWidth*" "]
        return ret

