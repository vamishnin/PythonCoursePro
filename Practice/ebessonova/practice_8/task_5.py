from Tasks.qrcode_task import qrcodelibrary
import os
import re


class BankProps:
    def __init__(self):
        with open('../../../Tasks/qrcode_task/реквизиты.txt', 'r', encoding='utf-8') as f:
            recs = f.read()
            attr_name = re.compile(r'\'(.*=)(_.*)\|\'')
            attr_name_ru = re.compile(r'\'(.*)\': \'(_.*)\'')
            attr_value = re.compile(r'(.*): (.*)')
            attr_name_list = re.findall(attr_name, recs)
            attr_name_ru_list = re.findall(attr_name_ru, recs)
            attr_value_list = re.findall(attr_value, recs)

        attr_list = list()
        for attr in attr_value_list:
            for attr_code in attr_name_ru_list:

                if attr[0].lower() == attr_code[0].lower():
                    attr_list.append((attr[1], attr_code[1]))

        attr_dict = list()
        for attr in attr_name_list:
            prop_name_added = False
            for attr_code in attr_list:

                if attr[1] == attr_code[1]:
                    attr_dict.append((attr[0], attr_code[0]))
                    prop_name_added = True
            if not prop_name_added:
                attr_dict.append((attr[0], ''))

        self.__attr_dict = attr_dict

    def save_props(self, filename):
        with open(filename, 'w') as f_qr:
            for attr in self.__attr_dict:
                f_qr.write(f'{attr[0]}{attr[1]}|')


if __name__ == '__main__':
    payment = BankProps()
    payment.save_props('props.txt')

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_qr = os.path.join(cur_dir, 'qr_output.jpg')
    with open('props.txt', 'r') as f:
        qrcodelibrary.txt_to_qrcode(f.read().strip(), path_to_qr)
        print(path_to_qr)
