from Tasks.qrcode_task import qrcodelibrary
import os


class BankProps:
    def __init__(self, sender_name, sender_surname, sender_middlename='', sm=100):
        self.Code = '1'
        self.Name = 'Someone'
        self.PersonalAcc = '40703810642020000114'
        self.BankName = 'Волго-Вятский  банк ПАО Сбербанк'
        self.BIC = '042202603'
        self.CorrespAcc = '30101810900000000603'
        self.PayeeINN = '5260138955'
        self.KPP = '526001001'
        self.LastName = sender_surname
        self.FirstName = sender_name
        self.MiddleName = sender_middlename
        self.Prpose = '001'
        self.РауеrАddress = ''
        self.Sm = sm

    def save_props(self, filename):
        with open(filename, 'w') as f:
            for prop_name, value in self.__dict__.items():
                f.write(f'{prop_name}={value}|')


payment = BankProps('Ivan', 'Ivanov')
payment.save_props('props.txt')

cur_dir = os.path.dirname(os.path.abspath(__file__))
path_to_qr = os.path.join(cur_dir, 'qr_output.jpg')
with open('props.txt', 'r') as f:
    qrcodelibrary.txt_to_qrcode(f.read().strip(), path_to_qr)
    print(path_to_qr)
