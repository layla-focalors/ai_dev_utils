import os, random

file_list = os.listdir('images')
c = "real"
RANDOM_NUM = 28168
EXTRACT_PATH = "/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/processed_img"
LABEL_PATH = "/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/labels"
label_out = "/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/label_out"
os.chdir('images')

# 파이썬에서 real 문자열을 포함하는 모든 파일 삭제
for i in file_list:
    if c in i:
        os.remove(i)
        print(f"removing file : {i}")
    else:
        continue

os.chdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway')
# 리스트 갱신
file_list = os.listdir('images')

# 파이썬에서 특정 사진들 랜덤 추출
re_file = random.sample(file_list, RANDOM_NUM)
os.chdir('images')
for j in re_file:
    os.system(f'cp {j} /home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/processed_img')
    print(f"extracting : {j}")
# 파일 추출 성공

print(f"파일 추출됨 : {len(re_file)}")

os.chdir(EXTRACT_PATH)
azuc = os.listdir(EXTRACT_PATH)
for u in azuc:
    data = u.strip("fake")
    os.rename(u, data)
    print(f"renaming : {data}")

# 라벨 조회
azic = os.listdir(EXTRACT_PATH)
os.chdir(LABEL_PATH)
osi = os.listdir(LABEL_PATH)

exi = []

re_azic = []
re_osi = []

# 확장자 제거
for y in azic:
    atx = y.split('.')
    re_azic.append(atx[0])
    print(f"확장자 제거 중 : {atx[0]}")

for t in osi:
    wty = t.split('.')
    re_osi.append(wty[0])
    print(f"확장자 제거 중 : {wty[0]}")

# azic - *.png, op = *.txtl
for o in re_azic:
    for op in re_osi:
        if o == op:
            exi.append(op)
        else:
            continue

# print(exi)
for io in exi:
    os.system(f'cp {io} /home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/label_out')
    print(f"copying label : {io}")

