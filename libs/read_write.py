#!/usr/bin/python3

''' 

AMZY-0 (M.Amin Azimi .K) 
Copyright (C) (2019-2020-2021)  AMZY-0 (M.Amin Azimi .K) 

"Luxarg" (This program) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

from tkinter import messagebox
from os import path
from os import getenv


def message(path_msg, text_msg):


    if text_msg == 'saved !':
        msg = messagebox.showinfo('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))
    
    else:
        msg = messagebox.showerror('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))


def writer(path_and_filename, text, widget_destroy):
    
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = '''Field is empty !
Please HIT <F2> and enter your file name again ...'''
        message(path_and_filename, '')

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory')   

    elif path_and_filename[:2] == '~/':
        path_and_filename = path_and_filename.replace('~/','%s/'% 
        str(getenv('HOME'))).strip()
    
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    

    # relational path for home
    elif path_and_filename[:2] == '~/':
        path_and_filename = path_and_filename.replace('~/','%s/'% 
        str(getenv('HOME'))).strip()
        
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    
    # relational path for home directory added (~)  
    elif path_and_filename == '~':
            message(path_and_filename, ': Is directory')

    else:
        
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    

    return widget_destroy.destroy()

####################################################
# reader 
####################################################

# read a file 
def reader(path_and_filename, text_field, widget_destroy):

    # delete all the buffer and after open file 
    text_field.delete('1.0', 'end')
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = 'Field is empty !\nPlease HIT <F2> and enter your path and file name again ...'
        message(path_and_filename, '')
    

    elif path_and_filename == '~':
        message(path_and_filename, ': Is directory (Directory is not readable)')   

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory (Directory is not readable)') 
    
    
    elif path_and_filename[:2] == '~/':
        try:
            path_and_filename = path_and_filename.replace('~/', '%s/' %
            str(getenv('HOME').strip()))

            fin = open(path_and_filename, 'r')
            readed =  fin.read()
            text_field.insert('1.0', str(readed))
            text_field.configure(state='disabled')
            fin.close()

        except FileNotFoundError as error:
            message('', str(error)[10:])

    else :
        try:
            path_and_filename = path_and_filename.replace('~/', '%s/' %
            str(getenv('HOME').strip()))

            fin = open(path_and_filename, 'r')
            readed =  fin.read()
            text_field.insert('1.0', str(readed))
            text_field.configure(state='disabled')
            fin.close()

        except FileNotFoundError as error:
            message('', str(error)[10:])
            
            
    text_field.configure(state='disabled')
    return widget_destroy.destroy()