import os

path = ""
file_list = os.listdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/origin_train_labels')
filelist = os.listdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/origin_train_labels')
os.chdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/origin_train_labels')

def apis():
    for i in filelist:
        data = i.split('.')
        process = data[0] + "_." + data[1]
        os.rename(i, process)
        print(f"processing : {process}")
    return None

def utils():
    filelist = os.listdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/origin_train_labels')
    for j in file_list:
        os.system(f'mv {j} {path}')

if __name__ == "__main__":
    utils()


# # 갱신
# filelist = os.listdir('/home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/origin_train_labels')
# for j in file_list:
#     os.system(f'cp {j} /home/work/Cycle-GAN-summer2Winter/pix2pix/results/test_extract_day2rain3ansan_highway/label')