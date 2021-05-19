import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,filedialog,colorchooser
main_app=tk.Tk()
main_app.title('TextWithMe')
main_app.geometry('1100x800')
main_app.wm_iconbitmap('icon.ico')
# ************************main menu*************************
main_menu=tk.Menu()
file=tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
color=tk.Menu(main_menu,tearoff=False)
# file=tk.Menu(main_app,tearoff=False


main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color)

#icons 

new_file=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\new.png')
new_folder=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\new.png')
open_file=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\open.png')
save_file=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\save.png')
save_as_file=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\save_as.png')
exit=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\exit.png')



#EDIT ICONS
# undo=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\UNdo-arrow.png')
# redo=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\redo-arrow.png')
cut=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\cut.png')
copy=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\copy.png')
paste=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\paste.png')
clearall=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\clear_all.png')
find=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\find.png')


# edit.add_command(label='Undo',image=undo,compound=tk.LEFT)
# edit.add_command(label='Redo',image=redo,compound=tk.LEFT)



# view icons
tolbar=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\tool_bar.png')
statusbar=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\status_bar.png')





#COLOR ICONS

light_default=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\light_default.png')
light_plus=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\light_plus.png')
night_blue=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\night_blue.png')
red=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\red.png')
monokai=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\monokai.png')
dark=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\dark.png')


# color.add_command(label='Color')
# color.add_radiobutton(label='light_default',compound=tk.LEFT,image=light_default)
# color.add_radiobutton(label='light_plus',compound=tk.LEFT,image=light_plus)
# color.add_radiobutton(label='night_blue',compound=tk.LEFT,image=night_blue)
# color.add_radiobutton(label='red',compound=tk.LEFT,image=red)
# color.add_radiobutton(label='monokai',compound=tk.LEFT,image=monokai)
# color.add_radiobutton(label='dark',compound=tk.LEFT,image=dark)


# **********************end main menu***********************


# ************************tool bar*************************

tool_bar=ttk.Label(main_app )
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_var=tk.StringVar()
font_tuple=tk.font.families()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_var,state='readonly')

font_box['value']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=4)


# SIZE

size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81,2))

font_size.current(2)
font_size.grid(row=0,column=1,padx=4)


#  bold button
bold_btn_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_btn_img)
bold_btn.grid(row=0,column=2,padx=4)

# italic
italic_btn_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_btn_img)
italic_btn.grid(row=0,column=3,padx=4)

# underline
underline_btn_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_btn_img)
underline_btn.grid(row=0,column=4,padx=4)

#alignment

# align=tk.StringVar()
align_left_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\align_left.png')
align_center_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\align_center.png')
align_right_img=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\align_right.png')


align_left_btn=ttk.Button(tool_bar,image=align_left_img)
align_left_btn.grid(row=0,column=5,padx=4)
align_center_btn=ttk.Button(tool_bar,image=align_center_img)
align_center_btn.grid(row=0,column=6,padx=4)
align_right_btn=ttk.Button(tool_bar,image=align_right_img)
align_right_btn.grid(row=0,column=7,padx=4)

# FONT COLOR BUTON

font_color_icon=tk.PhotoImage(file=r'F:\python_tutorial\folder1\TextWithMe\icons2\font_color.png')
font_btn=ttk.Button(tool_bar,image=font_color_icon)
font_btn.grid(row=0,column=8,padx=4)



# **********************end toolbar***********************



# ************************Text editor***********************

text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(main_app)
scroll_bar.config(command=text_editor.yview)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.config(yscrollcommand=scroll_bar.set)

text_editor.pack(fill=tk.BOTH,expand=True)


# FONT FUNCTIONALITY

current_family='Arial'
current_size=12

text_editor.configure(font=('Arial','12'))

def font_change(main_app):
    global current_family

    current_family=font_var.get()
    current_size=size_var.get()
    text_editor.configure(font=(current_family,current_size))

font_box.bind("<<ComboboxSelected>>",font_change)

def fontsize_change(main_app):
    global current_size

    # current_family=font_var.get()
    current_size=size_var.get()
    text_editor.configure(font=(current_family,current_size))

font_size.bind("<<ComboboxSelected>>",fontsize_change)


# BUTTON FUNCTIONALITY

#BOLD BUTTON

def bold_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_family,current_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_family,current_size,'normal'))

bold_btn.configure(command=bold_button)
# bold_btn.bind("<<ButtonSelected>>",bold_button)

# italic button

def italic_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_family,current_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_family,current_size,'roman'))

italic_btn.configure(command=italic_button)

#UNDERLINE

def underline_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_family,current_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_family,current_size,'normal'))

underline_btn.configure(command=underline_button)

#font color changer

def change_font_color():
    font_color=tk.colorchooser.askcolor()
    text_editor.configure(fg=font_color[1])

font_btn.configure(command=change_font_color)


# alignment functionality

def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)


def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)


# **********************end Text editor***********************

# ************************STATUS bar*************************

status_bar=ttk.Label(main_app,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)


# status bar functionality
text_change=False
def change_status(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0, 'end-1c').split())
        character=len(text_editor.get(1.0, 'end-1c').replace(' ',''))
        status_bar.config(text=f'Character = {character} , Words = {word}')
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>",change_status)
# **********************end STATUS bar**********************




# *************main menu functionality***************

#file functionality

url=''
def new_file_fn(event=None):
    global url
    text_editor.delete(1.0, tk.END)
    url=''

# FILE COMMANDS
file.add_command(label='New file', image=new_file,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file_fn)
# file.add_command(label='New Folder',image=new_folder,compound=tk.LEFT,accelerator='ctrl+Shift+n')


#OPEN FUNCTION
def open_file_fn(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text Files','*.txt'),('ALL','*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))


file.add_command(label='Open',image=open_file,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file_fn)

# SAVE FUNCTIONALITY
def save_file_fn(event=None):
    global url
    try:
        if url:
            content=text_editor.get(1.0, tk.END) 
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('ALL','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
file.add_command(label='Save',image=save_file,compound=tk.LEFT,accelerator='ctrl+S', command=save_file_fn)

# SAVE AS FUNCTION

def save_as_fn(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('ALL','*.*')))
        content2=text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()
    except:
        return
file.add_command(label='Save As',image=save_as_file,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=save_as_fn)

# EXIT FUNCTIONS

def exit_fn(event=None):
    global url,text_change
    try:
        if text_change:
            m_box=messagebox.askyesnocancel('Warning','Do you want to save ?')
            if m_box is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                # url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('ALL','*.*')))
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text Files','*.txt'),('ALL','*.*')))
                    content2=text_editor.get(1.0,tk.END)
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif m_box is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return
                

file.add_command(label='Exit',image=exit,compound=tk.LEFT,accelerator='Ctrl+E',command=exit_fn)

#EDIT COMMANDS
edit.add_command(label='Cut',image=cut,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda : text_editor.event_generate("<Control x>"))
edit.add_command(label='Copy',image=copy,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda : text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda : text_editor.event_generate("<Control v>"))
edit.add_command(label='Clear All',image=clearall,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda : text_editor.delete(1.0,tk.END))


# find functionality

def find_fn(event=None):

    def find():
        word=find_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not True:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    
    
    def replace():
        word=find_entry.get()
        replace_item=replace_entry.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_item)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    
    
    
    find_dialog=tk.Toplevel()
    find_dialog.geometry('450x250+500+250')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    #frame
    find_frame=tk.LabelFrame(find_dialog,text='Find/Replace')
    find_frame.pack(pady=30)

    # label
    find_label=ttk.Label(find_frame,text='Find')
    replace_label=ttk.Label(find_frame,text='Replace')

    #entry
    find_entry=ttk.Entry(find_frame,width=40)
    replace_entry=ttk.Entry(find_frame,width=40)

    #buttons
    find_btn=ttk.Button(find_frame,text='Find',command=find)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)

    # grid
    find_label.grid(row=0,column=0,pady=10)
    replace_label.grid(row=1,column=0,pady=6)
    find_entry.grid(row=0,column=1)
    replace_entry.grid(row=1,column=1)
    find_btn.grid(row=2,column=0,padx=14,pady=6)
    replace_btn.grid(row=2,column=1)

    find_frame.mainloop()






edit.add_command(label='Find',image=find,compound=tk.LEFT,accelerator='Ctrl+F',command=find_fn)

# VIEW COMMANDS

statusbar_var=tk.BooleanVar()
statusbar_var.set(True)
toolbar_var=tk.BooleanVar()
toolbar_var.set(True)

def hide_statusbar():
    global statusbar_var
    if statusbar_var:
        status_bar.pack_forget()
        statusbar_var=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        statusbar_var=True
def hide_toolbar():
    global toolbar_var
    if toolbar_var:
        tool_bar.pack_forget()
        toolbar_var=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.BOTH)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        toolbar_var=True

view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=statusbar_var,image=statusbar,compound=tk.LEFT,command=hide_statusbar)
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=toolbar_var,image=tolbar,compound=tk.LEFT,command=hide_toolbar)

# COLOR COMMANDS

theme_choice=tk.StringVar()
color_icons=(light_default,light_plus,night_blue,red,monokai,dark)
counter=0
color_dict={
    'Light Default': ('#000000','#FFFFFF'),
    'Light Plus':('#474747','#e0e0e0'),
    'Night Blue':('#FFFFFF','#191970'),
    'Red':('#FFFFFF','#8b0000'),
    'Monokai':('#1f1fde','#a9a9a9'),
    'Dark':('#4d2c6f','#008b8b')
}

def change_theme():
    choosen_theme=theme_choice.get()
    color_tuple=color_dict.get(choosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(bg=bg_color,fg=fg_color)


for i in color_dict:
    color.add_radiobutton(label=i,compound=tk.LEFT,image=color_icons[counter],variable=theme_choice,command=change_theme)
    counter+=1



# *************end main menu functionality***********
main_app.bind("<Control-n>",new_file_fn)
main_app.bind("<Control-o>",open_file_fn)
main_app.bind("<Control-s>",save_file_fn)
main_app.bind("<Control-Shift-s>",save_as_fn)
main_app.bind("<Control-e>",exit_fn)

main_app.bind("<Control-f>",find_fn)
# main_app.bind("<Control-n>",new_file_fn)
# main_app.bind("<Control-n>",new_file_fn)
# main_app.bind("<Control-n>",new_file_fn)
# main_app.bind("<Control-n>",new_file_fn)


main_app.config(menu=main_menu)
main_app.mainloop()
