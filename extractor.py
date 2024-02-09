import os
import shutil
import subprocess

def main():
    print('iPhone Photo Extractor v1.0')
    open()
    extract()
    print('\n\n')


def open():
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, 'Output')
    if not os.path.exists('Output/'):
        os.makedirs('Output/')
    subprocess.Popen(['explorer', path])


def extract():
    folders = os.listdir('DCIM/')
    picturecount = 0
    progress = 0
    for i in range(2):
        for folder in folders:
            foldercontents = os.listdir(f'DCIM/{folder}/')
            sorted = [image for image in foldercontents if not image.endswith('.AAE') and not image.endswith('.HEIC')]
            if i == 1:
                for image in sorted:
                    progress +=1
                    percentage = "{:.0f}%".format(progress/picturecount*100)
                    shutil.copy(f'DCIM/{folder}/{image}', 'Output/')
                    print(f'\rProgress: {percentage}', end='', flush=True)
            else:
                picturecount += len(sorted)


main()