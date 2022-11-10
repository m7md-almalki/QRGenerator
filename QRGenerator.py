

from base64 import b64encode, b64decode
import datetime
import pyqrcode



class Invoice:

    time = datetime.datetime.now()

    Year = str(time.year)
    Month = str(time.month)
    Day = str(time.day)
    Hour = str(time.hour)
    Minute = str(time.minute)
    Second = str(time.second)

    if len(Year) < 4:
        Year = "0"+Year

    if len(Month) < 2:
        Month = "0"+Month

    if len(Day) < 2:
        Day = "0"+Day

    if len(Hour) < 2:
        Hour = "0"+Hour

    if len(Minute) < 2:
        Minute = "0"+Minute

    if len(Second) < 2:
        Second = "0"+Second

    NameOfSeller = "Mohammed Almalki"
    VatRNumber = "123456789012345"
    RealTime = "{}-{}-{}T{}:{}:{}Z".format(Year,Month,Day,Hour,Minute,Second)
    InvoiceTWVat = "10000.00"
    VatTotal = "150.00"

    AllOfInvoice = []
    FinalCode = ""

    def __init__(self):
        def NameOFSellerGenerator():
            if self.NameOfSeller.isascii():
                if len(hex(len(self.NameOfSeller)).lstrip("0x")) == 1:
                    NameOfSellerPART = "010{}".format(hex(len(self.NameOfSeller)).lstrip("0x"))
                    self.AllOfInvoice.append(NameOfSellerPART)
                else:
                    NameOfSellerPART = "01{}".format(hex(len(self.NameOfSeller)).lstrip("0x"))
                    self.AllOfInvoice.append(NameOfSellerPART)

                self.AllOfInvoice.append(self.NameOfSeller.encode("utf-8").hex())
            else:
                self.NameOfSeller = bytes(self.NameOfSeller.encode())
                print(self.NameOfSeller)

                if len(hex(len(self.NameOfSeller)).lstrip("0x")) == 1:
                    NameOfSellerPART = "010{}".format(hex(len(self.NameOfSeller)).lstrip("0x"))
                    self.AllOfInvoice.append(NameOfSellerPART)
                else:
                    NameOfSellerPART = "01{}".format(hex(len(self.NameOfSeller)).lstrip("0x"))
                    self.AllOfInvoice.append(NameOfSellerPART)

                self.AllOfInvoice.append(bytes(self.NameOfSeller).hex())
                print(self.NameOfSeller)


        def VatRNumberGenerator():
            if len(hex(len(self.VatRNumber)).lstrip("0x")) == 1:
                VatRNumberPART = "020{}".format(hex(len(self.VatRNumber)).lstrip("0x"))
                self.AllOfInvoice.append(VatRNumberPART)
            else:
                VatRNumberPART = "02{}".format(hex(len(self.VatRNumber)).lstrip("0x"))
                self.AllOfInvoice.append(VatRNumberPART)

            self.AllOfInvoice.append(self.VatRNumber.encode("utf-8").hex())



        def RealTimeGenerator():
            if len(hex(len(self.RealTime)).lstrip("0x")) == 1:
                RealTimePART = "030{}".format(hex(len(self.RealTime)).lstrip("0x"))
                self.AllOfInvoice.append(RealTimePART)
            else:
                RealTimePART = "03{}".format(hex(len(self.RealTime)).lstrip("0x"))
                self.AllOfInvoice.append(RealTimePART)

            self.AllOfInvoice.append(self.RealTime.encode("utf-8").hex())



        def InvoiceTWVatGenerator():
            if len(hex(len(self.InvoiceTWVat)).lstrip("0x")) == 1:
                InvoiceTWVatPART = "040{}".format(hex(len(self.InvoiceTWVat)).lstrip("0x"))
                self.AllOfInvoice.append(InvoiceTWVatPART)
            else:
                InvoiceTWVatPART = "04{}".format(hex(len(self.InvoiceTWVat)).lstrip("0x"))
                self.AllOfInvoice.append(InvoiceTWVatPART)

            self.AllOfInvoice.append(self.InvoiceTWVat.encode("utf-8").hex())


        def VatTotalGenerator():
            if len(hex(len(self.VatTotal)).lstrip("0x")) == 1:
                VatTotalPART = "050{}".format(hex(len(self.VatTotal)).lstrip("0x"))
                self.AllOfInvoice.append(VatTotalPART)
            else:
                VatTotalPART = "05{}".format(hex(len(self.VatTotal)).lstrip("0x"))
                self.AllOfInvoice.append(VatTotalPART)

            self.AllOfInvoice.append(self.VatTotal.encode("utf-8").hex())


        NameOFSellerGenerator()
        VatRNumberGenerator()
        RealTimeGenerator()
        InvoiceTWVatGenerator()
        VatTotalGenerator()


        def EncodeToBase64(HexCode):
            self.FinalCode = b64encode(bytes.fromhex(HexCode)).decode()

        EncodeToBase64("".join(self.AllOfInvoice))


        QR = pyqrcode.create(self.FinalCode)

        QR.svg("QR.svg", scale=8)

        QR.png('QR.png', scale=8)

Invoice()
