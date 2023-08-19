import os
file_list = os.listdir('processed_img')
label_list = os.listdir('origin_train_labels')

os.chdir('origin_train_labels')

ad1 = []
ad2 = []
labels = []

for i in file_list:
    data = i.split('.')
    ad1.append(data[0])
    print(f"processA = {data[0]}")

for j in label_list:
    data = j.split('.')
    ad2.append(data[0])
    print(f"processB = {data[0]}")

# print(ad1)
# print(ad2)

# for ui in ad1:
#     for ux in ad2:
#         if ui == ux:
#             print(f"일치하는 라벨을 찾았습니다 : {ux}")
#             labels.append(ux)
# ucx = []

# for uix in range(len(ad1)):
#     for ux in range(len(ad2)):
#         if ad1[uix] == ad2[ux]:
#             print(f"일치하는 라벨을 찾았습니다 : {ux}")
#             labels.append(ucx)


values = []

for d in range(len(ad1)):
    # d -> 0
    for x in range(len(ad2)):
        if ad1[d] == ad2[x]:
            print(f"데이터 일치. A = {ad1[d]} B = {ad2[x]}")
            values.append(ad2[x])
        else:
            print(f"A = {ad1[d]} B = {ad2[x]}\n일치하지 않음")
            continue

print(values)

print(labels)

for ji in labels:
    os.system(f'mv {str(ji) + ".txt"} /home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/label_out')
    print(f"exporting label : {ji}")
