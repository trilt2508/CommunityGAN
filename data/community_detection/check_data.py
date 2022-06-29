file_name_input_train = 'D:\ky20212\WebMining\CommunityGAN\data\community_detection\com-youtube_train.txt'
file_name_input_sample = "D:\ky20212\WebMining\CommunityGAN\data\community_detection\com-youtube.sampled.cmty.txt"
D = {}
L = []
with open(file_name_input_train, 'r') as f:
    while True:
        try:
            [a, b] = [int(x) for x in f.readline().split()]
        except:
            break
        if a not in L:
            L.append(a)
            D[a] = []
        if b not in L:
            L.append(b)
            D[b] = []
        D[a].append(b)
        D[b].append(a)
        if len(L) % 10000 == 0:
            print(len(L))
replace = {}
L.sort()
print(len(L))
List_sample = []
with open(file_name_input_sample, 'r') as f:
    while True:
        x_ = [int(x) for x in f.readline().split()]
        if len(x_) == 0:
            break
        for x__ in x_:
            if x__ not in List_sample:
                List_sample.append(x__)
List_sample.sort()
print(len(List_sample))