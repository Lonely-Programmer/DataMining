from sys import setswitchinterval
import wx
import os
import re
from wx.lib.wordwrap import wordwrap
import  wx.lib.dialogs
import Search

sort_tag = ["Date","Size"]
mode_tag = ["Normal","Distance","Paragraph","Bracket"]
class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(4000,3000))
        font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.style = wx.RESIZE_BORDER
        self.size = (4000,3000)
        self.contents = wx.TextCtrl (self,style=wx.TE_MULTILINE | wx.HSCROLL )
        self.contents.SetBackgroundColour(wx.WHITE)
        self.coder = wx.TextCtrl (self,style=wx.TE_MULTILINE | wx.HSCROLL )
        self.coder.SetBackgroundColour(wx.WHITE)

        self.msgFont = self.contents.GetFont()
        self.msgColour = wx.BLACK
        self.contents.SetFont(font)
        self.coderFont = self.coder.GetFont()
        self.coderColour = wx.BLACK
        self.coder.SetFont(font)
        self.flag = 0
        self.findData = wx.FindReplaceData()
        self.search = Search.Search()
        self.search.load(2013)
        #self.mode = 0
        """创建状态栏"""
        #self.CreateStatusBar()   
        '''
        """file菜单布局"""
        filemenu = wx.Menu()
        menuNew = filemenu.Append(wx.ID_NEW  ,"&New\tCtrl+N","New a file 新建")
        menuOpen = filemenu.Append(wx.ID_OPEN ,"&Open\tCtrl+O","Open a file 打开")
        menuSave = filemenu.Append(wx.ID_SAVE  ,"&Save\tCtrl+S","Save the file 保存")

        """菜单分隔线"""
        filemenu.AppendSeparator()   
        menuExit = filemenu.Append(wx.ID_EXIT   ,"E&xit\tCtrl+Q","Tenminate the program 退出")

        """格式菜单布局"""
        formatmenu = wx.Menu ()
        menuMsgFont = formatmenu.Append(wx.ID_ANY ,"&msg Font","Set the message font 设置输入字体")
        menuCoderFont = formatmenu.Append(wx.ID_ANY ,"&coder Font","Set the coder font 设置输出字体")        

        """帮助菜单布局"""
        helpmenu = wx.Menu ()
             
        """菜单栏布局"""
        menuBar = wx.MenuBar ()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(formatmenu,"&Setup")
        menuBar.Append(helpmenu,"&Help")
        #self.SetMenuBar(menuBar)'''

        """创建按钮"""        
        self.SortButton = wx.Button (self,label = 'Date')
        SearchButton = wx.Button (self,label = 'Search')
        #self.ModeButton = wx.Button(self,label = 'Normal')
              
        """函数绑定"""
        '''self.Bind(wx.EVT_MENU,self.OnExit,menuExit)
        self.Bind(wx.EVT_MENU,self.OnOpen,menuOpen)
        
        self.Bind(wx.EVT_MENU,self.OnSelectFont,menuMsgFont)'''
               
        self.Bind(wx.EVT_BUTTON,self.OnSearch,SearchButton)
        self.Bind(wx.EVT_BUTTON,self.OnSwitch,self.SortButton)
        #self.Bind(wx.EVT_BUTTON,self.OnMode,self.ModeButton)        
        
        """布局"""
        self.sizer0 = wx.BoxSizer (wx.HORIZONTAL )
                
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2.Add(self.SortButton, 1, wx.EXPAND)
        #self.sizer2.Add(self.ModeButton,1,wx.EXPAND)
        self.sizer2.Add(SearchButton, 1, wx.EXPAND)
            
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer0, 0, wx.EXPAND)
        self.sizer.Add(self.contents, 1, wx.EXPAND)
        self.sizer.Add(self.coder, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        """显示布局"""
        self.Show(True)   
    def OnSearch(self,evt):
        self.coder.Clear()
        msg = self.contents.GetValue()
        self.Output(self.search.normal_search(msg,self.flag))
    def OnSwitch(self,evt):
        self.flag = 1 - self.flag
        self.SortButton.SetLabel(sort_tag[self.flag])

    def OnSelectFont(self, evt):
        msg = self.contents.GetValue()
        data = wx.FontData()
        data.EnableEffects(True)
        data.SetColour(self.msgColour)         # set colour
        data.SetInitialFont(self.msgFont)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            colour = data.GetColour()
            self.msgFont = font
            self.msgColour = colour
            self.contents.SetFont(self.msgFont)
            self.contents.SetForegroundColour(self.msgColour)
        dlg.Destroy()
    '''def OnMode(self,evt):
        self.mode+=1
        self.mode%=4
        self.ModeButton.SetLabel(mode_tag[self.mode])'''
    def OnExit(self):
        self.Close(True)
    def Output(self,Res):
        msg = Res[1]
        docs = Res[0]
        if(len(docs)==0):
            msg+="No Results"
        else:
            for i in docs:
                if len(i[1])==0:
                    continue
                msg+=i[0]
                msg+="\n"
                msg+=i[1]+"\n"
        self.coder.write(msg)
        # print(msg)
app = wx.App(False)
frame = MainWindow(None,"Search")
app.MainLoop()

