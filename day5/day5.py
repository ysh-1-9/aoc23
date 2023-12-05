def convert(map, answer):
    #print("map: ", map)
    print("answer: ", answer)
    
    p1 = 0
    p2 = 0
    
    running_diff = 0
    splits = []
    for s,e in answer:
        
        while p2<len(map) and map[p2][0]<s:
            running_diff+=map[p2][1]
            p2+=1
        newsplit = []
        last = s
            
        if p2<len(map) and map[p2][0] == s:
            running_diff+=map[p2][1]
            p2+=1
            
        while p2<len(map) and map[p2][0]<=e:
            if map[p2][0]-1 >= last:
                newsplit+= [((last, map[p2][0]-1), running_diff)]
            last = map[p2][0]
            running_diff+=map[p2][1]
            p2+=1
        if last!=e:
            newsplit+= [((last, e), running_diff)]
        #print("newsplit: ", newsplit)
        splits+=newsplit
    newanswer = [(s+d, e+d) for (s,e),d in splits]
    #print("newanswer: ", newanswer)
    return newanswer
    
    
seeds = None
answer = None
with open('input.txt', 'r') as f:
    t = f.read()
    
    map = []
    for line in t.split('\n'):
        #print(line)
        if line == "":
            
            # nmap = []
            map = sorted(map, key = lambda x: x[0])
            # itr = 0 while itr<len(map):
            #     if map[itr]==last:
            #         diff+=map[itr]
            answer = sorted(answer, key = lambda x: x[0])
            answer = convert(map, answer)
            map = []
        elif ":" in line:
            if not seeds:
                seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
                ns = []
                for idx, x in enumerate(seeds):
                    if idx%2==0:
                        ns.append((x, x+seeds[idx+1]-1))
                answer = ns
                #print(len(ns)) break
        else:
            try:
                a,b,c = [int(x) for x in line.split(' ')]
                diff = a-b
                last_idx = b+c
                map+=[(b, diff), (last_idx, -diff)]
            except:
                print('FFF')
                continue
print(answer)
print(min(answer))
