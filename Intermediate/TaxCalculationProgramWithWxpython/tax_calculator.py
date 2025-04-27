import wx
import pandas as pd
from datetime import datetime
import os

# Path for the Excel file
FILE_PATH = "tax_records.xlsx"

class TaxCalculatorApp(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 400))
        self.init_ui()
        self.init_excel_file()

    def init_ui(self):
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Input fields
        input_sizer = wx.FlexGridSizer(3, 2, 10, 10)
        input_sizer.AddGrowableCol(1)

        input_sizer.Add(wx.StaticText(panel, label="คำอธิบาย:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.description = wx.TextCtrl(panel)
        input_sizer.Add(self.description, 1, wx.ALL | wx.EXPAND, 5)

        input_sizer.Add(wx.StaticText(panel, label="จำนวนเงินก่อนหักภาษี:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.total_amount = wx.TextCtrl(panel)
        input_sizer.Add(self.total_amount, 1, wx.ALL | wx.EXPAND, 5)

        input_sizer.Add(wx.StaticText(panel, label="จำนวนเงินที่ถูกหัก:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.deducted_amount = wx.TextCtrl(panel)
        input_sizer.Add(self.deducted_amount, 1, wx.ALL | wx.EXPAND, 5)

        main_sizer.Add(input_sizer, 0, wx.ALL | wx.EXPAND, 10)

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        calculate_button = wx.Button(panel, label="ดูผลลัพธ์")
        calculate_button.Bind(wx.EVT_BUTTON, self.calculate_tax)
        button_sizer.Add(calculate_button, 0, wx.ALL, 5)

        save_button = wx.Button(panel, label="บันทึก")
        save_button.Bind(wx.EVT_BUTTON, self.save_record)
        button_sizer.Add(save_button, 0, wx.ALL, 5)

        cancel_button = wx.Button(panel, label="ยกเลิก")
        cancel_button.Bind(wx.EVT_BUTTON, self.cancel_entry)
        button_sizer.Add(cancel_button, 0, wx.ALL, 5)

        main_sizer.Add(button_sizer, 0, wx.CENTER, 10)

        # Display records
        self.records_list = wx.ListBox(panel, style=wx.LB_SINGLE)
        self.load_records()
        main_sizer.Add(self.records_list, 1, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(main_sizer)

    def init_excel_file(self):
        if not os.path.exists(FILE_PATH):
            df = pd.DataFrame(columns=["คำอธิบาย", "จำนวนเงินก่อนหักภาษี", "จำนวนเงินที่ถูกหัก", "จำนวนเงินคงเหลือ", "% ที่ถูกหัก", "วันที่/เวลา"])
            df.to_excel(FILE_PATH, index=False)

    def calculate_tax(self, event):
        try:
            total = float(self.total_amount.GetValue())
            deducted = float(self.deducted_amount.GetValue())

            if total < deducted:
                wx.MessageBox("จำนวนเงินที่ถูกหักไม่สามารถมากกว่าจำนวนเงินทั้งหมดได้", "Error", wx.ICON_ERROR)
                return

            remaining = total - deducted
            percent = (deducted / total) * 100

            wx.MessageBox(f"จำนวนเงินคงเหลือ: {remaining:.2f} บาท\nถูกหัก: {percent:.2f}%", "ผลลัพธ์", wx.ICON_INFORMATION)
        except ValueError:
            wx.MessageBox("กรุณากรอกข้อมูลให้ถูกต้อง", "Error", wx.ICON_ERROR)

    def save_record(self, event):
        try:
            description = self.description.GetValue()
            total = float(self.total_amount.GetValue())
            deducted = float(self.deducted_amount.GetValue())

            if total < deducted:
                wx.MessageBox("จำนวนเงินที่ถูกหักไม่สามารถมากกว่าจำนวนเงินทั้งหมดได้", "Error", wx.ICON_ERROR)
                return

            remaining = total - deducted
            percent = (deducted / total) * 100
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save to Excel
            df = pd.read_excel(FILE_PATH)
            new_record = pd.DataFrame([{
                "คำอธิบาย": description,
                "จำนวนเงินก่อนหักภาษี": total,
                "จำนวนเงินที่ถูกหัก": deducted,
                "จำนวนเงินคงเหลือ": remaining,
                "% ที่ถูกหัก": percent,
                "วันที่/เวลา": timestamp
            }])
            df = pd.concat([df, new_record], ignore_index=True)
            df.to_excel(FILE_PATH, index=False)

            wx.MessageBox("บันทึกรายการสำเร็จ", "Success", wx.ICON_INFORMATION)
            self.load_records()  # Refresh the records list
        except ValueError:
            wx.MessageBox("กรุณากรอกข้อมูลให้ถูกต้อง", "Error", wx.ICON_ERROR)

    def cancel_entry(self, event):
        self.description.SetValue("")
        self.total_amount.SetValue("")
        self.deducted_amount.SetValue("")

    def load_records(self):
        # Load records from the Excel file and update the list
        if os.path.exists(FILE_PATH):
            df = pd.read_excel(FILE_PATH)
            records = [self.format_record(r) for r in df.to_dict(orient="records")]
            self.records_list.Set(records)

    def format_record(self, record):
        return (f"{record['วันที่/เวลา']} - {record['คำอธิบาย']} - "
                f"ก่อนหัก {record['จำนวนเงินก่อนหักภาษี']:.2f} บาท - "
                f"หัก {record['จำนวนเงินที่ถูกหัก']:.2f} บาท - "
                f"คงเหลือ {record['จำนวนเงินคงเหลือ']:.2f} บาท - "
                f"หัก {record['% ที่ถูกหัก']:.2f}%")

if __name__ == "__main__":
    app = wx.App()
    frame = TaxCalculatorApp(None, title="โปรแกรมคำนวณภาษี")
    frame.Show()
    app.MainLoop()
