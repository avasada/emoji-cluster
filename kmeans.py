import codecs
from sklearn.cluster import KMeans
import csv 

file_object = codecs.open('onlyemo_model.txt', 'r', encoding='utf8', errors='ignore')
dataset = file_object.readlines()
file_object.close()

emojiCodes = {}

for line in dataset[1:]:
    line = line.split(" ")
    key = line[0]
    key = key[4:]
    emojiCodes[key] = line[1:]

emojis = []
emojiKeys = []
for key in emojiCodes:
    emojis.append(emojiCodes[key])
    emojiKeys.append(key)

new_list = []

for x in emojis:
    for e in x:
        e = [float(e) for e in x]
    new_list.append(e)

emojiLookup = {}

with open("emoji_lookup.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        key = row[0]
        emojiLookup[key] = row[1]

kmeans = KMeans(n_clusters = 15)
kmeans.fit(new_list) 
groups = kmeans.labels_

centroid1 = []
centroid2 = []
centroid3 = []
centroid4 = []
centroid5 = []
centroid6 = []
centroid7 = []
centroid8 = []
centroid9 = []
centroid10 = []
centroid11 = []
centroid12 = []
centroid13 = []
centroid14 = []
centroid15 = []

all_centroids = []
all_centroids.extend([centroid1, centroid2, centroid3, centroid4, centroid5, centroid6, centroid7, centroid8, centroid9, centroid10, centroid11, centroid12, centroid13, centroid14, centroid15])

def sort_emojis(x, n, v):
    if x == n:
        centroid = all_centroids[n]
        centroid.append(v)

for i in range(846):
    x = groups[i]
    v = emojiKeys[i]
    v = emojiLookup[v]
    for n in range(15):
        sort_emojis(x, n, v)

def print_centroid(x):
    print("centroid " + x)
    
def print_list(x):
    print(all_centroids[x])

for x in range(1,16):
    x = str(x)
    print_centroid(x)
    x = int(x)
    x = x - 1
    print_list(x)