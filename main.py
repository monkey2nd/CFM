#encoding:utf-8
from tk import message
from scrape_class import scrall
from p_for_d import Mak
import os
import pathlib
path='..\\'

script_file_name=os.getcwd()

def folders_serch(path):
    files=os.listdir(path)
    return files

def rename_path(path,name):
    path=path+'\\'+name
    return path
files=folders_serch(path)
script_file_name=pathlib.Path(script_file_name)
parent_folder_bacename=script_file_name.name
files.remove(parent_folder_bacename)

if not files==[]:
    while(1):
        make_files_num=input('作成するファイル数は一週間分でいいですか？ [y/（作成したいファイル数）]')
        try:
            if make_files_num=='y':
                make_files_num=1
                print(str(make_files_num)+'週間分作成します')
                break
            elif type(int(make_files_num))==int:
                make_files_num=int(make_files_num)
                print(str(make_files_num)+'週間分作成します')
                break
        except ValueError:
            print('yか数字で入力してくださいn')

# f_name1：曜日　f_name2：授業名
    
    for f_name1 in files:
        temp_pass=rename_path(path,f_name1)
        temp_name1_ls=folders_serch(temp_pass)
        for f_name2 in temp_name1_ls:
            temp_pass2=rename_path(temp_pass,f_name2)
            temp_name2_ls=folders_serch(temp_pass2)

            for i in range(make_files_num):
                g_path=temp_pass2+'/'+str(len(temp_name2_ls)+1+i)+'週目'
                os.makedirs(g_path)
                print('作成ファイル　：'+g_path)

else:
    app=message()
    scrall()
    dic=Mak()
    for day in dic.keys():
        os.makedirs(str(script_file_name.parent)+'\\'+day+'曜日')
        for time in dic[day].keys():
                os.makedirs(str(script_file_name.parent)+'\\'+day+'曜日'+'\\'+time+'限　'+dic[day][time])


