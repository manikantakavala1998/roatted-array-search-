from collections import Counter
def minWindow(s: str, t: str) -> str:
  if not t or not s:
    return "" 
  dict_t=Counter(t)  
  required=len(dict_t)  
  l,r=0, 0 
  formed=0  
  window_counts={}  
  ans=float("inf"), None, None 
  while r<len(s):
    char=s[r]  
    window_counts[char] = window_counts.get(char, 0) + 1
    if char in dict_t and window_counts[char] == dict_t[char]:
      formed+=1 
    while l<=r and formed==required:
      if r-l+1<ans[0]  :
        ans=(r-l+1,l,r)  
      window_counts[s[l]]=-1 
      if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
        formed-=1 
      l+=1 
    r+=1 
  return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
s1, t1= "ADOBECODEBANC", "ABC"  
s2,t2="a","a"  
print("Input 1 Output:", minWindow(s1, t1))

print("Input 2 Output:", minWindow(s2, t2))
