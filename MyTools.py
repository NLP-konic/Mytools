# -*- coding: utf-8 -*-
'''double shift 万能搜索 crtl+e 最近打开'''
from contextlib import  contextmanager
import xlrd,xlwt,xlutils
from xlutils.copy import copy
import fileinput

@contextmanager
def Writetxt(filepath):
    f= open(filepath,'w',encoding='utf-8')
    yield f
    f.close()




def ReadExcel(xls,index=0):
    '''excel读取工具函数，默认sheet_index为sheet1'''
    with xlrd.open_workbook(xls)as xls:

        sheet = xls.sheet_by_index(index)

        return sheet


class Excel():

    '''工具类EXCEL，可进行读取和修改excel表，默认参数是0，修改时可调整需要的表序号下标'''
    def __init__(self,xls,sheet_index=0):
        self.xls=xls
        self.sheet_index=sheet_index


    def ReadExcel(self):
        '''excel读取工具函数，默认sheet_index为sheet1'''
        with xlrd.open_workbook(self.xls)as xls:

            sheet = xls.sheet_by_index(self.sheet_index)
            rows=sheet.nrows
            self.rows = rows
            return sheet

    @contextmanager
    def ReviseExcel(self,sheet_index=None):
        '''修改EXCEL，可传一个参数为表的下标，如果不传的话，那么就与创建实例时的下标一致
        :param sheet_index: 下标
        '''

        excel= xlrd.open_workbook(self.xls)
        copy_xls=copy(excel)
        if sheet_index is None:
            #将参数默认值设为一个无关的变量，比如None，如果参数传入值则使用传入值，如果没有传入值则使用创建实例时的参数

            sheet_index=self.sheet_index

        sheet = copy_xls.get_sheet(sheet_index)

        yield sheet
        copy_xls.save(self.xls.split('.')[0] + '.xlsx')



