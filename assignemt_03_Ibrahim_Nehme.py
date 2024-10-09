def countDigits(number):
    if(number==0):
        return 0
    else:
        return 1+countDigits(number//10)

def findMax(arr,n):
    if n==0:
        return -1
    if n==1:
        return arr[0]
    else:
        maxofarr= findMax(arr,n-1)
        if arr[n-1]>maxofarr:
            return arr[n-1]
        else:
            return maxofarr

def countTags(html_str, tag):
    open_tag = '<'+tag+'>'
    close_tag = '</'+tag+'>'
    
    if open_tag not in html_str:
        return 0
    
    open_index = html_str.find(open_tag)
    
    close_index = html_str.find(close_tag, open_index)
    
        
    remaining_str = html_str[close_index + len(close_tag):]
    return 1 + countTags(remaining_str, tag)


