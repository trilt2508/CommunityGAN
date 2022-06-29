
file_name_input_train = 'D:\ky20212\WebMining\CommunityGAN\data\community_detection\com-amazon_train.txt'
file_name_input_sample = "D:\ky20212\WebMining\CommunityGAN\data\community_detection\com-amazon.sampled.cmty.txt"
file_name_ouput_train = 'com-amazon_train.txt'
file_name_ouput_agm = 'com-amazon_agm.txt'
file_name_ouput_sample = 'com-amazon.sampled.cmty.txt'
D = {}
L = []
List_sample = []
L_sample = []
with open(file_name_input_sample, 'r') as f:
    while True:
        x_ = [int(x) for x in f.readline().split()]
        if len(x_) == 0:
            break
        List_sample.append(x_)
        for x__ in x_:
            if x__ not in L_sample:
                L_sample.append(x__)
print(len(L_sample))
L_sample.sort()
with open(file_name_input_train, 'r') as f:
    while True:
        try:
            [a, b] = [int(x) for x in f.readline().split()]
        except:
            break
        if a not in L_sample or b not in L_sample:
            continue
        if a not in L:
            L.append(a)
            D[a] = []
        if b not in L:
            L.append(b)
            D[b] = []
        D[a].append(b)
        D[b].append(a)
        # if len(L) % 10000 == 0:
        #     print(len(L))
replace = {}
L.sort()
print(len(L))
for i in range(len(L)):
    replace[L[i]] = i
with open(file_name_ouput_train, 'w') as wf:
    for i in range(len(L)):
        for x in D[L[i]]:
            if i < replace[x]:
                wf.write(f'{i}\t{replace[x]}' + '\n')
print("complete train")
with open(file_name_ouput_agm, 'w') as wf:
    for i in range(len(L)):
        for x in D[L[i]]:
            wf.write(f'{i}\t{replace[x]}' + '\n')
print("complete agm")


for x in List_sample:
    for i in range(len(x)):
        x[i] = replace[x[i]]
with open(file_name_ouput_sample, 'w') as wf:
    for x in List_sample:
        for x_ in x:
            if x_ != x[-1]:
                wf.write(f'{x_} ')
            else:
                wf.write(f'{x_}\n')
print("complete sample")