filepath = r"C:\Users\ktmks\programming\datas\t10k-labels-idx1-ubyte\t10k-labels.idx1-ubyte"
with open(filepath,mode="rb") as f:
    t = f.read()

test_labels = []
i = 8
while 1:
    try:
        test_labels.append(t[i])
    except IndexError:
        break
    i += 1

