import shutil,os,re
old_path='G:\\Lachnospiraceaea_DataSet\\Genomes'
new_path='G:\\Lachnospiraceaea_DataSet\\Proteinfaa_Files'
for derName, subfolders, filenames in os.walk(old_path):
 for i in range(len(filenames)):
        if filenames[i].endswith('protein.faa'):
            file_path=derName+'\\'+filenames[i]
            newpath=new_path+'\\'+filenames[i]
            shutil.copy(file_path,newpath)

print('Moving is finished!')