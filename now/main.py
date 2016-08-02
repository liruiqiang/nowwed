

import argparse
from core import AddressBook
from display import print_table


if __name__ =='__main__':
    book = AddressBook()
    book.load_data()
    parser = argparse.ArgumentParser(prog='python3 main.py',
                           description='我的通讯录')
    parser.add_argument('-a','--add',
                        nargs=2,type=str,
                        metavar=('姓名','电话号码'),
                        help='添加一个联系人')
    parser.add_argument('-q','--query',
                        nargs="?",
                        type=str,
                        const="",
                        metavar=("查询关键字",),
                        help='查询联系人')
    parser.add_argument('-d','--delete',
                        nargs=1,
                        type=int,
                        metavar=('联系人ID',),
                        help='删除联系人')
    args=parser.parse_args()
    if args.add is not None:
        book.add_record(args.add[0],args.add[1])
        print('添加成功')
    elif args.query is not None:
        records = book.query_record(args.query)
        print_table(records)
    elif args.delete is not None:
        book.delete_record(args.delete[0])
        print('删除成功')
    else:
        parser.print_help()

    book.save_data()
