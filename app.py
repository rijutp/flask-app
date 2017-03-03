from flask import Flask,request,jsonify
import MySQLdb
import datetime
from dateutil import parser
import time
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = ''
API_KEY = 'secretkey'

connection = MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE)
cursor = connection.cursor()

app = Flask(__name__)


# if __name__ == "__main__":
#     app.run(debug=True)
@app.route("/get_all_accounts/")
def hello():
    if request.args.get('api_key') and request.args.get('api_key') == API_KEY:
        if request.args.get('table') == "accounts_group":
            cursor.execute("select * from accounts_group")
            accounts_group = []
            for item in cursor.fetchall():
                accounts_group.append({"slno":item[0],"id":item[1],"name":item[2],"parent_group":item[3]})
            return jsonify(accounts_group=accounts_group)
        elif request.args.get('table') == "allsalesbills":
            cursor.execute("select * from  allsalesbills")
            allsalesbills = []
            for item in cursor.fetchall():
                allsalesbills.append({"id":item[0],"Bill_No":item[1],"Order_No":item[2],"Bill_Item_Serial":item[3],"item_name":item[4],"item_group":item[5],"Price":item[6],"Quantity":item[7],"Discount":item[8],"Bill_Discount":item[9]," Sub_total":item[10],"Add_on_With":item[11]," Date":item[12],"PaymentMode":item[13],"ServiceMode":item[14],"DiscountRefer":item[15],"Naarration":item[16]," VAT":item[17],"PAX":item[18],"ServiceTax":item[19],"Attended":item[20],"Delivered":item[21],"timestamp":item[22]})
            return jsonify(allsalesbills=allsalesbills)
            # select * from allsalesbills and return
        elif request.args.get('table') == "allvouchers":
            cursor.execute("select * from  allvouchers")
            allvouchers = []
            for item in cursor.fetchall():
                allvouchers.append({"id":item[0],"Date":item[1],"Voucher_Type":item[2],"ledger_name":item[3],"Amount":item[4],"Narration":item[5]}) 
            return jsonify(allvouchers=allvouchers)
        elif request.args.get('table') == "cheque_details":
            cursor.execute("select * from  cheque_details")
            cheque_details = []
            for item in cursor.fetchall():
                cheque_details.append({"_id":item[0],"transaction_id":item[1],"ledger_id":item[2],"amount":item[3],"bank_name":item[4],"branch_name":item[5],"cheque_number":item[6]}) 
            return jsonify(cheque_details=cheque_details)
        elif request.args.get('table') == "company_info":
            cursor.execute("select * from  company_info")
            company_info = []
            for item in cursor.fetchall():
                company_info.append({"_id":item[0],"company_name":item[1],"company_address":item[2],"tin":item[3],"phone":item[4],"manager_name":item[5]}) 
            return jsonify(company_info=company_info) 
        elif request.args.get('table') == "config":
            cursor.execute("select * from  config")
            config = []
            for item in cursor.fetchall():
                config.append({"Bill_no":item[0],"baseBill_no":item[1],"EmailList":item[2]}) 
            return jsonify(config=config)
        elif request.args.get('table') == "daily_shift":
            cursor.execute("select * from  daily_shift")
            daily_shift = []
            for item in cursor.fetchall():
                daily_shift.append({"_id":item[0],"ShiftDate":item[1],"StartVoucherNo":item[2],"StopVoucherNo":item[3],"OpeningBalance":item[4],"CardAmount":item[5],"CashInCounter":item[6],"CashTaken":item[7],"ShiftStaffName":item[8],"Narration":item[9],"timestamp":item[10]}) 
            return jsonify(daily_shift=daily_shift)   
        elif request.args.get('table') == "deleted_kot":
            cursor.execute("select * from  deleted_kot")
            deleted_kot = []
            for item in cursor.fetchall():
                deleted_kot.append({"_id":item[0],"sales_Voucher_Id":item[1],"Item_Name":item[2],"Quantity":item[3],"Rate_per":item[4],"Item_Discount":item[5],"Amount":item[6],"Vat":item[7],"Narration":item[8],"Voucher_Prefix":item[9],"Voucher_Date":item[10],"Totat_Discount":item[11],"Service_tax":item[12],"table_name":item[13],"isPrinted":item[14],"isSaved":item[15],"timestamp":item[16]}) 
            return jsonify(deleted_kot=deleted_kot)   
        elif request.args.get('table') == "employee":
            cursor.execute("select * from  employee")
            employee = []
            for item in cursor.fetchall():
                employee.append({"_id":item[0],"Name":item[1],"Barcode":item[2],"Designation":item[3],"Rank":item[4],"Basic_Salary":item[5],"Overtime ":item[6]}) 
            return jsonify(employee=employee)
        elif request.args.get('table') == "ingredients":
            cursor.execute("select * from  ingredients")
            ingredients = []
            for item in cursor.fetchall():
                ingredients.append({"_id":item[0],"sales_item":item[1],"sales_item_qty":item[2],"purchase_item":item[3],"purchase_item_qty":item[4]}) 
            return jsonify(ingredients=ingredients)
        elif request.args.get('table') == "intent_entry":
            cursor.execute("select * from  intent_entry")
            intent_entry = []
            for item in cursor.fetchall():
                intent_entry.append({"serialnumber":item[0],"purchase_item":item[1],"intent_group":item[2],"request_count":item[3],"issue_count":item[4],"entry_date":item[5],"Timestamp":item[6]}) 
            return jsonify(intent_entry=intent_entry)
        elif request.args.get('table') == "intent_group":
            cursor.execute("select * from  intent_group")
            intent_group = []
            for item in cursor.fetchall():
                intent_group.append({"serialnumber":item[0]," Name":item[1],"Timestamp":item[2]}) 
            return jsonify(intent_group=intent_group)
        elif request.args.get('table') == "inventory":
            cursor.execute("select * from  inventory")
            inventory = []
            for item in cursor.fetchall():
                inventory.append({"Item_ID":item[0],"Item_Name":item[1],"Item_Group":item[2],"Item_Description":item[3],"Item_Price":item[4],"Item_Quantity":item[5],"alias":item[6],"Narration":item[7],"Service_Tax":item[8],"VAT":item[9],"barcode":item[10]}) 
            return jsonify(inventory=inventory)   
        elif request.args.get('table') == "journal_details":
            cursor.execute("select * from  journal_details")
            journal_details = []
            for item in cursor.fetchall():
                journal_details.append({"_id":item[0],"Journal_Voucher_Id":item[1],"Item_Name":item[2],"AmountDr":item[3],"AmountDr":item[4],"Narration":item[5],"Voucher_Prefix":item[6],"Voucher_Date":item[7]}) 
            return jsonify(journal_details=journal_details) 
        elif request.args.get('table') == "ledger_master":
            cursor.execute("select * from  ledger_master")
            ledger_master = []
            for item in cursor.fetchall():
                ledger_master.append({"sl_no":item[0],"_id":item[1],"Ledger_Name":item[2],"Ledger_Type":item[3],"Group_Name":item[4],"Opening_Balance":item[5],"Ledger_Narration":item[6],"Mailing_Address_1":item[7],"Alias":item[8],"Mailing_Address_2":item[9],"City":item[10],"Date_Of_Birth":item[11],"State":item[12],"PIN_Code":item[13],"Contact_Person_Name":item[14],"Contact_Person_Number":item[15],"Phone_no":item[16],"EMail":item[17],"TIN":item[18],"VAT":item[19],"contact_person_lastname":item[20],"nationality":item[21],"company_name":item[22],"prod_date":item[23],"expiry_date":item[24]})
            return jsonify(ledger_master=ledger_master) 
        elif request.args.get('table') == "log":
            cursor.execute("select * from  log")
            log = []
            for item in cursor.fetchall():
                log.append({"_id":item[0],"timestamp":item[1],"data":item[2],"action":item[2],"status":item[2]}) 
            return jsonify(log=log)
        elif request.args.get('table') == "old_kot_details":
            cursor.execute("select * from  old_kot_details")
            old_kot_details = []
            for item in cursor.fetchall():
                old_kot_details.append({"_id":item[0],"sales_Voucher_Id":item[1],"Item_Name":item[2],"Quantity":item[3],"Rate_per":item[4],"Item_Discount":item[5],"Amount":item[6],"Vat":item[7],"Narration":item[8],"Voucher_Prefix":item[9],"Voucher_Date":item[10],"Totat_Discount":item[11],"Service_tax":item[12],"table_name":item[13],"isPrinted":item[14],"isSaved":item[15]}) 
            return jsonify(old_kot_details=old_kot_details)    
        elif request.args.get('table') == "old_kot_voucher":
            cursor.execute("select * from  old_kot_voucher")
            old_kot_voucher = []
            for item in cursor.fetchall():
                old_kot_voucher.append({"_id":item[0],"Invoice_No":item[1],"Voucher_Date":item[2],"Date_Created":item[3],"Bill_Date":item[4],"Timestamp":item[5],"Ledger_Name":item[6],"Billing_Name":item[7],"Total":item[8],"Narration":item[9],"Voucher_Prefix":item[10],"Hidden_Row":item[11],"Discount_Amount":item[12],"table_name":item[13]}) 
            return jsonify(old_kot_voucher=old_kot_voucher)
        # else:
        #     return jsonify(error="please provide a valid table name")  
        elif request.args.get('table') == "payment_details":
            cursor.execute("select * from payment_details")
            payment_details = []
            for item in cursor.fetchall():
                payment_details.append({"_id": item[0], "Payment_Voucher_Id": item[1],  "Item_Name": item[2], "Amount": item[3], "Narration": item[4], "Voucher_Prefix": item[5], "Voucher_Date": item[6], "Mode_Of_Pay": item[7]})
            return jsonify(payment_details=payment_details)
        elif request.args.get('table') == "payment_voucher":
            cursor.execute("select * from payment_voucher")
            payment_voucher = []
            for item in cursor.fetchall():
                payment_voucher.append({"_id": item[0], "Voucher_Date": item[1], "Date_Created": item[2], "TimeStamp": item[3], "Ledger_Name": item[4], "Total": item[5], "Mode_Of_Pay": item[6], "Narration": item[7], "Voucher_Prefix": item[8], "Hidden_Row": item[9]})
            return jsonify(payment_voucher=payment_voucher)
        elif request.args.get('table') == "purchase_details":
            cursor.execute("select * from purchase_details")
            purchase_details = []
            for item in cursor.fetchall():
                purchase_details.append({"_id": item[0], "sales_Voucher_Id": item[1], "Item_Name": item[2], "Quantity": item[3], "Rate_Per": item[4], "Item_Discount": item[5], "Amount": item[6], "Vat": item[7], "Narration": item[8], "Voucher_Prefix": item[9], "Voucher_Date": item[10], "Totat_Discount": item[11], "Ledger_Name": item[12]})
            return jsonify(purchase_details=purchase_details)
        elif request.args.get('table') == "purchase_inventory_group":
            cursor.execute("select * from purchase_inventory_group")
            purchase_inventory_group = []
            for item in cursor.fetchall():
                purchase_inventory_group.append({"sl_no": item[0], "_id": item[1], "Group_Name": item[2], "Parent_Group": item[3]})
            return jsonify(purchase_inventory_group=purchase_inventory_group)
        elif request.args.get('table') == "purchase_inventory_item":
            cursor.execute("select * from purchase_inventory_item")
            purchase_inventory_item = []
            for item in cursor.fetchall():
               purchase_inventory_item.append({"_id": item[0], "Name": item[1], "Code": item[2], "Alias": item[3], "Group_Name": item[4], "Unit_Of_Measurement": item[5], "Rate_Of_VAT": item[6], "Opening_Balance": item[7], "Price": item[8], "Default_Sales_Ledger": item[9], "Default_Purchase_Ledger": item[10], "Favourite": item[11], "Narration": item[12]})
            return jsonify(purchase_inventory_item=purchase_inventory_item)
        elif request.args.get('table') == "purchase_voucher":
            cursor.execute("select * from purchase_voucher")
            purchase_voucher = []
            for item in cursor.fetchall():
               purchase_voucher.append({"_id": item[0], "Invoice_No": item[1], "Voucher_Date": item[2], "Date_Created": item[3], "Bill_Date": item[4], "Timestamp": item[5], "Ledger_Name": item[6], "Billing_Name": item[7], "Total": item[8], "Narration": item[9], "voucher_Prefix": item[10], "Hidden_Row": item[11]})
            return jsonify(purchase_voucher=purchase_voucher)
        elif request.args.get('table') == "receipt_details":
            cursor.execute("select * from receipt_details")
            receipt_details = []
            for item in cursor.fetchall():
               receipt_details.append({"_id": item[0], "Receipt_Voucher_Id": item[1],  "Item_Name": item[2], "Amount": item[3], "Narration": item[4], "Voucher_Prefix": item[5], "Voucher_Date": item[6], "Mode_Of_Pay": item[7]})
            return jsonify(receipt_details=receipt_details)
        elif request.args.get('table') == "receipt_voucher":
             cursor.execute("select * from receipt_voucher")
             receipt_voucher = []
             for item in cursor.fetchall():
                receipt_voucher.append({"_id": item[0], "Voucher_Date": item[1], "Date_Created": item[2], "TimeStamp": item[3], "Ledger_Name": item[4], "Total": item[5], "Mode_Of_Pay": item[6], "Narration": item[7], "Voucher_Prefix": item[8], "Hidden_Row": item[9]})
             return jsonify(receipt_voucher=receipt_voucher)
        elif request.args.get('table') == "sales_details":
             cursor.execute("select * from sales_details")
             sales_details = []
             for item in cursor.fetchall():
                sales_details.append({"_id": item[0], "sales_Voucher_Id": item[1], "Item_Name": item[2], "Quantity": item[3], "Rate_Per": item[4], "Item_Discount": item[5], "Amount": item[6], "Vat": item[7], "Narration": item[8], "Voucher_Prefix": item[9], "Voucher_Date": item[10], "Total_Discount": item[11], "Service_tax": item[12], "kot_num": item[13], "Ledger_Name": item[14]})
             return jsonify(sales_details=sales_details)
        elif request.args.get('table') == "sales_inventory_group":
             cursor.execute("select * from sales_inventory_group")
             sales_inventory_group = []
             for item in cursor.fetchall():
                sales_inventory_group.append({"sl_no": item[0], "_id": item[1], "Group_Name": item[2], "Parent_Group": item[3]})
             return jsonify(sales_inventory_group=sales_inventory_group)
        elif request.args.get('table') == "sales_inventory_item":
             cursor.execute("select * from sales_inventory_item")
             sales_inventory_item = []
             for item in cursor.fetchall():
                sales_inventory_item.append({"_id": item[0], "Name": item[1], "Code": item[2], "Alias": item[3], "Group_Name": item[4], "Unit_Of_Measurement": item[5], "Rate_Of_VAT": item[6], "Opening_Balance": item[7], "Price": item[8], "Default_Sales_Ledger": item[9], "Default_Purchase_Ledger": item[10], "Favourite": item[11], "Narration": item[12]})
             return jsonify(sales_inventory_item=sales_inventory_item)
        elif request.args.get('table') == "sales_voucher":
             cursor.execute("select * from sales_voucher")
             sales_voucher = []
             for item in cursor.fetchall():
                sales_voucher.append({"_id": item[0], "Invoice_No": item[1], "Voucher_Date": item[2], "Date_Created": item[3], "Bill_Date": item[4], "Timestamp": item[5], "Ledger_Name": item[6], "Billing_Name": item[7], "Total": item[8], "Narration": item[9], "voucher_Prefix": item[10], "Hidden_Row": item[11], "Discount_Amount": item[12], "table_name": item[13], "deliver_add": item[14]})
             return jsonify(sales_voucher=sales_voucher)
        elif request.args.get('table') == "shifttable":
             cursor.execute("select * from shifttable")
             shifttable = []
             for item in cursor.fetchall():
                shifttable.append({"_id": item[0], "ShiftDate": item[1], "StartVoucherNo": item[2], "StopVoucherNo": item[3], "SalesValue": item[4], "OpeningBalance": item[5], "CardAmount": item[6], "CashInCounter": item[7], "CashTaken": item[8], "TiltDifference": item[9], "ShiftStaffName": item[10], "Narration": item[11], "timestamp": item[12]})
             return jsonify(shifttable=shifttable)
        elif request.args.get('table') == "stock_entry":
             cursor.execute("select * from stock_entry")
             stock_entry = []
             for item in cursor.fetchall():
                stock_entry.append({"_id": item[0], "Date": item[1], "Date_Created": item[2], "Timestamp": item[3], "Name": item[4], "Narration": item[5]})
             return jsonify(stock_entry=stock_entry)
        elif request.args.get('table') == "stock_entry_details":
             cursor.execute("select * from stock_entry_details")
             stock_entry_details = []
             for item in cursor.fetchall():
                stock_entry_details.append({"_id": item[0], "Entry_id": item[1], "Item_Name": item[2], "Quantity": item[3], "Defective": item[4]})
             return jsonify(stock_entry_details=stock_entry_details)
        elif request.args.get('table') == "tempbill":
             cursor.execute("select * from tempbill")
             tempbill = []
             for item in cursor.fetchall():
                tempbill.append({"_id": item[0], "itemname": item[1], "groupname": item[2], "price": item[3], "quantity": item[4], "addons": item[5], "order_Number": item[6], "ipaddress": item[7], "orderstatus": item[8], "reference": item[9], "Kot_Number": item[10]})
             return jsonify(tempbill=tempbill)
        elif request.args.get('table') == "temp_sales_details":
             cursor.execute("select * from temp_sales_details")
             temp_sales_details = []
             for item in cursor.fetchall():
                temp_sales_details.append({"_id": item[0], "sales_Voucher_Id": item[1], "Item_Name": item[2], "Quantity": item[3], "Rate_Per": item[4], "Item_Discount": item[5], "Amount": item[6], "Vat": item[7], "Narration": item[8], "Voucher_Prefix": item[9], "Voucher_Date": item[10], "Total_Discount": item[11], "Service_tax": item[12], "table_name": item[13], "isPrinted": item[14], "isSaved": item[15], "kot_num": item[16]})
             return jsonify(temp_sales_details=temp_sales_details)
        elif request.args.get('table') == "temp_sales_voucher":
             cursor.execute("select * from temp_sales_voucher")
             temp_sales_voucher = []
             for item in cursor.fetchall():
                temp_sales_voucher.append({"_id": item[0], "Invoice_No": item[1], "Voucher_Date": item[2], "Date_Created": item[3], "Bill_Date": item[4], "Timestamp": item[5], "Ledger_Name": item[6], "Billing_Name": item[7], "Total": item[8], "Narration": item[9], "voucher_Prefix": item[10], "Hidden_Row": item[11], "Discount_Amount": item[12], "table_name": item[13], "deliver_add": item[14]})
             return jsonify(temp_sales_voucher=temp_sales_voucher)
        elif request.args.get('table') == "transcation_helper":
             cursor.execute("select * from transcation_helper")
             transcation_helper = []
             for item in cursor.fetchall():
                transcation_helper.append({"_id": item[0], "date": item[1], "transactionAmount": item[2], "voucherType": item[3], "voucherId": item[4], "debitLedgerID": item[5], "creditLedgerID": item[6], "narration": item[7], "voucher_Prefix": item[8]})
             return jsonify(transcation_helper=transcation_helper)
        
        else:
            return jsonify(error="please provide a valid table name")
    else:
        return jsonify(error="invalid api key") 


@app.route("/insert/")
def insert():
    if request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "accounts_group":
        id = request.args.get("_id")
        name = request.args.get("name")
        parentgroup = request.args.get("parent_group")
        if all([id,name,parentgroup]):
            cursor.execute("insert into accounts_group(_id,name,parent_group) values (%s,%s,%s)",(id,name,parentgroup))
            connection.commit()
            result={'_id':id,'name':name,'parent_group':parentgroup}
            print result
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "employee":
        name = request.args.get("Name")
        barcode = request.args.get("Barcode")
        designation = request.args.get("Designation")
        rank = request.args.get("Rank")
        basic_salary = request.args.get("Basic_Salary")
        overtime = request.args.get("Overtime")
        if all([name,barcode,designation,rank,basic_salary,overtime]):
            cursor.execute("insert into employee(Name,Barcode,Designation,Rank,Basic_Salary,Overtime) values (%s,%s,%s,%s,%s,%s)",(name,barcode,designation,rank,basic_salary,overtime))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "intent_group":
        # serialnumber = request.args.get("serialnumber")
        Name = request.args.get("Name")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if all([Name,timestamp]):
            cursor.execute("insert into intent_group(Name,Timestamp) values (%s,%s)",(Name,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "config":
        Bill_no = request.args.get("Bill_no")
        baseBill_no = request.args.get("baseBill_no")
        EmailList = request.args.get("EmailList")
        if all([Bill_no,baseBill_no,EmailList]):
            cursor.execute("insert into config(Bill_no,baseBill_no,EmailList) values (%s,%s,%s)",(Bill_no,baseBill_no,EmailList))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    # elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "employee":
    #     name = request.args.get("name")
    #     barcode = request.args.get("barcode")
    #     designation = request.args.get("designation")
    #     rank = request.args.get("rank")
    #     basic_salary = request.args.get("basic_salary")
    #     overtime = request.args.get("overtime")
    #     if all([name,barcode,designation,rank,basic_salary,overtime]):
    #         cursor.execute("insert into employee(Name,Barcode,Designation,Rank,Basic_Salary,Overtime) values (%s,%s,%s,%s,%s,%s)",(name,barcode,designation,rank,basic_salary,overtime))
    #         connection.commit()
    #         return jsonify(response="inserted")
    #     else:
    #         return jsonify(error="please provide necessary arguments")
    #     return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "allsalesbills":
        bill_no = request.args.get("Bill_No")
        order_no = request.args.get("Order_No")
        bill_item_serial = request.args.get("Bill_Item_Serial")
        item_name = request.args.get("item_name")
        item_group = request.args.get("item_group")
        price = request.args.get("Price")
        quantity = request.args.get("Quantity")
        discount = request.args.get("Discount")
        bill_discount = request.args.get("Bill_Discount")
        sub_total = request.args.get("Sub_total")
        add_on_with = request.args.get("Add_on_With")
        date = request.args.get("Date")
        date = parser.parse(date)
        payment_mode = request.args.get("PaymentMode")
        service_mode = request.args.get("ServiceMode")
        discount_refer = request.args.get("DiscountRefer")
        naarration = request.args.get("Naarration")
        vat = request.args.get("VAT")
        pax = request.args.get("PAX")
        service_tax = request.args.get("ServiceTax")
        attended = request.args.get("Attended")
        delivered = request.args.get("Delivered")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if all([bill_no,order_no,bill_item_serial,item_name,item_group,price,quantity,discount,bill_discount,sub_total,add_on_with,date,payment_mode,service_mode,discount_refer,naarration,vat,pax,service_tax,attended,delivered,timestamp]):
            cursor.execute("insert into allsalesbills(Bill_No,Order_No,Bill_Item_Serial,item_name,item_group,Price,Quantity,Discount,Bill_Discount, Sub_total,Add_on_With,Date,PaymentMode,ServiceMode,DiscountRefer,Naarration,VAT,PAX,ServiceTax,Attended,Delivered,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(bill_no,order_no,bill_item_serial,item_name,item_group,price,quantity,discount,bill_discount,sub_total,add_on_with,date,payment_mode,service_mode,discount_refer,naarration,vat,pax,service_tax,attended,delivered,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "allvouchers":
        date = request.args.get("date")
        date = parser.parse(date)
        voucher_type = request.args.get("voucher_type")
        ledger_name = request.args.get("ledger_name")
        amount = request.args.get("amount")
        naarration = request.args.get("naarration")
        if all([date,voucher_type,ledger_name,amount,naarration]):
            cursor.execute("insert into allvouchers(Date,Voucher_Type,ledger_name,Amount,Narration) values (%s,%s,%s,%s,%s)",(date,voucher_type,ledger_name,amount,naarration))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "cheque_details":
        transaction_id = request.args.get("transaction_id")
        ledger_id = request.args.get("ledger_id")
        amount = request.args.get("amount")
        bank_name = request.args.get("bank_name")
        branch_name = request.args.get("branch_name")
        cheque_number = request.args.get("cheque_number")
        if all([transaction_id,ledger_id,amount,bank_name,branch_name,cheque_number]):
            cursor.execute("insert into cheque_details(transaction_id,ledger_id,amount,bank_name,branch_name,cheque_number) values (%s,%s,%s,%s,%s,%s)",(transaction_id,ledger_id,amount,bank_name,branch_name,cheque_number))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")        
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "company_info":
        company_name = request.args.get("company_name")
        company_address = request.args.get("company_address")
        tin = request.args.get("tin")
        phone = request.args.get("phone")
        manager_name = request.args.get("manager_name")
        if all([company_name,company_address,tin,phone,manager_name]):
            cursor.execute("insert into company_info(company_name,company_address,tin,phone,manager_name) values (%s,%s,%s,%s,%s)",(company_name,company_address,tin,phone,manager_name))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "daily_shift":
        ShiftDate = request.args.get("ShiftDate")
        ShiftDate = parser.parse(ShiftDate)
        StartVoucherNo = request.args.get("StartVoucherNo")
        StopVoucherNo = request.args.get("StopVoucherNo")
        OpeningBalance = request.args.get("OpeningBalance")
        CardAmount = request.args.get("CardAmount")
        CashInCounter = request.args.get("CashInCounter")
        CashTaken = request.args.get("CashTaken")
        ShiftStaffName = request.args.get("ShiftStaffName")
        Narration = request.args.get("Narration")        
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if all([ShiftDate,StartVoucherNo,StopVoucherNo,OpeningBalance,CardAmount,CashInCounter,CashTaken,ShiftStaffName,Narration,timestamp]):
            cursor.execute("insert into daily_shift(ShiftDate,StartVoucherNo,StopVoucherNo,OpeningBalance,CardAmount,CashInCounter,CashTaken,ShiftStaffName,Narration,timestamp)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ShiftDate,StartVoucherNo,StopVoucherNo,OpeningBalance,CardAmount,CashInCounter,CashTaken,ShiftStaffName,Narration,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "deleted_kot":
        sales_Voucher_Id  = request.args.get("sales_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Quantity  = request.args.get("Quantity")
        Rate_per = request.args.get("Rate_per")
        Item_Discount  = request.args.get("Item_Discount")
        Amount = request.args.get("Amount")
        Vat = request.args.get("Vat")
        Narration  = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Voucher_Date  = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Totat_Discount  = request.args.get("Totat_Discount")
        Service_tax   = request.args.get("Service_tax")
        table_name = request.args.get("table_name")
        isPrinted  = request.args.get("isPrinted")
        isSaved = request.args.get("isSaved")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if all([sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,timestamp]):
            cursor.execute("insert into deleted_kot(sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "ingredients":
        sales_item  = request.args.get("sales_item")
        sales_item_qty  = request.args.get("sales_item_qty")
        purchase_item  = request.args.get("purchase_item")
        purchase_item_qty = request.args.get("purchase_item_qty")
        if all([sales_item,sales_item_qty,purchase_item,purchase_item_qty]):
            cursor.execute("insert into ingredients(sales_item,sales_item_qty,purchase_item,purchase_item_qty) values (%s,%s,%s,%s)",(sales_item,sales_item_qty,purchase_item,purchase_item_qty))
            connection.commit()
            return jsonify(response="inserted")  
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "intent_entry":
        purchase_item = request.args.get("purchase_item")
        intent_group = request.args.get("intent_group")
        request_count = request.args.get("request_count")
        issue_count = request.args.get("issue_count")
        entry_date= request.args.get("entry_date")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        if all([purchase_item,intent_group,request_count,issue_count,entry_date,timestamp]):
            cursor.execute("insert into intent_entry(purchase_item,intent_group,request_count,issue_count,entry_date,Timestamp) values (%s,%s,%s,%s,%s,%s)",(purchase_item,intent_group,request_count,issue_count,entry_date,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "inventory":
        Item_Name  = request.args.get("Item_Name")
        Item_Group  = request.args.get("Item_Group")
        Item_Description  = request.args.get("Item_Description")
        Item_Price = request.args.get("Item_Price")
        Item_Quantity = request.args.get("Item_Quantity")
        alias  = request.args.get("alias")
        Narration = request.args.get("Narration")
        Service_Tax = request.args.get("Service_Tax")
        VAT  = request.args.get("VAT")
        barcode   = request.args.get("barcode")
        
        if all([Item_Name,Item_Group,Item_Description,Item_Price,Item_Quantity,alias,Narration,Service_Tax,VAT,barcode]):
            cursor.execute("insert into inventory(Item_Name,Item_Group,Item_Description,Item_Price,Item_Quantity,alias,Narration,Service_Tax,VAT,barcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Item_Name,Item_Group,Item_Description,Item_Price,Item_Quantity,alias,Narration,Service_Tax,VAT,barcode))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "journal_details":
        Journal_Voucher_Id = request.args.get("Journal_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        AmountDr = request.args.get("AmountDr")
        AmountCr = request.args.get("AmountCr")
        Narration  = request.args.get("Narration")
        Voucher_Prefix   = request.args.get("Voucher_Prefix")
        Voucher_Date  = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        if all([Journal_Voucher_Id,Item_Name,AmountDr,AmountCr,Narration,Voucher_Prefix,Voucher_Date]):
            cursor.execute("insert into journal_details(Journal_Voucher_Id,Item_Name,AmountDr,AmountCr,Narration,Voucher_Prefix,Voucher_Date) values (%s,%s,%s,%s,%s,%s,%s)",(Journal_Voucher_Id,Item_Name,AmountDr,AmountCr,Narration,Voucher_Prefix,Voucher_Date))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "journal_voucher":
        Voucher_Date = request.args.get("Voucher_Date")       
        Date_Created = request.args.get("Date_Created")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Ledger_Name = request.args.get("Ledger_Name")
        Total = request.args.get("Total")
        Mode_of_pay  = request.args.get("Mode_of_pay")
        Narration  = request.args.get("Narration")
        Voucher_Prefix  = request.args.get("Voucher_Prefix")
        Hidden_Row  = request.args.get("Hidden_Row")
        if all([Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_of_pay,Narration,Voucher_Prefix,Hidden_Row]):
            cursor.execute("insert into journal_voucher(Voucher_Date,Date_Created,Timestamp,Ledger_Name,Total,Mode_of_pay,Narration,Voucher_Prefix,Hidden_Row) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_of_pay,Narration,Voucher_Prefix,Hidden_Row))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "ledger_master":
        _id = request.args.get("_id")       
        Ledger_Name = request.args.get("Ledger_Name")
        Ledger_Type = request.args.get("Ledger_Type")
        Group_Name = request.args.get("Group_Name")
        Opening_Balance = request.args.get("Opening_Balance")
        Ledger_Narration = request.args.get("Ledger_Narration")
        Mailing_Address_1 = request.args.get("Mailing_Address_1")
        Alias = request.args.get("Alias")
        Mailing_Address_2 = request.args.get("Mailing_Address_2")
        City = request.args.get("City")
        Date_Of_Birth = request.args.get("Date_Of_Birth")
        State = request.args.get("State")
        PIN_Code  = request.args.get("PIN_Code")
        Contact_Person_Name = request.args.get("Contact_Person_Name")
        Contact_Person_Number = request.args.get("Contact_Person_Number")
        Phone_no = request.args.get("Phone_no")
        EMail = request.args.get("EMail")
        TIN = request.args.get("TIN")
        VAT = request.args.get("VAT")
        contact_person_lastname = request.args.get("contact_person_lastname")
        nationality = request.args.get("nationality")
        company_name  = request.args.get("company_name")
        prod_date = request.args.get("prod_date")
        expiry_date  = request.args.get("expiry_date")
        if all([_id,Ledger_Name,Ledger_Type,Group_Name,Opening_Balance,Ledger_Narration,Mailing_Address_1,Alias,Mailing_Address_2,City,Date_Of_Birth,State,PIN_Code,Contact_Person_Name,Contact_Person_Number,Phone_no,EMail,TIN,VAT,contact_person_lastname,nationality,company_name,prod_date,expiry_date]):
            cursor.execute("insert into ledger_master(_id,Ledger_Name,Ledger_Type,Group_Name,Opening_Balance,Ledger_Narration,Mailing_Address_1,Alias,Mailing_Address_2,City,Date_Of_Birth,State,PIN_Code,Contact_Person_Name,Contact_Person_Number,Phone_no,EMail,TIN,VAT,contact_person_lastname,nationality,company_name,prod_date,expiry_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(_id,Ledger_Type,Ledger_Name,Group_Name,Opening_Balance,Ledger_Narration,Mailing_Address_1,Alias,Mailing_Address_2,City,Date_Of_Birth,State,PIN_Code,Contact_Person_Name,Contact_Person_Number,Phone_no,EMail,TIN,VAT,contact_person_lastname,nationality,company_name,prod_date,expiry_date))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "log":
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        data = request.args.get("data")
        action = request.args.get("action")
        status= request.args.get("status")
        if all([timestamp,data,action,status]):
            cursor.execute("insert into log(timestamp,data,action,status) values (%s,%s,%s,%s)",(timestamp,data,action,status))
            connection.commit()
            return jsonify(response="inserted")  
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "old_kot_details":
        sales_Voucher_Id  = request.args.get("sales_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Quantity  = request.args.get("Quantity")
        Rate_per = request.args.get("Rate_per")
        Item_Discount  = request.args.get("Item_Discount")
        Amount = request.args.get("Amount")
        Vat = request.args.get("Vat")
        Narration  = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Voucher_Date  = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Totat_Discount  = request.args.get("Totat_Discount")
        Service_tax   = request.args.get("Service_tax")
        table_name = request.args.get("table_name")
        isPrinted  = request.args.get("isPrinted")
        isSaved = request.args.get("isSaved")
        if all([sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved]):
            cursor.execute("insert into old_kot_details(sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key')== API_KEY and request.args.get('table')== "old_kot_voucher":
        _id = request.args.get("_id") 
        Invoice_No = request.args.get("Invoice_No")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        Bill_Date = request.args.get("Bill_Date")
        Bill_Date = parser.parse(Bill_Date)
        timestamp = request.args.get("Timestamp")
        timestamp = parser.parse(timestamp)
        Ledger_Name = request.args.get("Ledger_Name")
        Billing_Name  = request.args.get("Billing_Name")
        Total = request.args.get("Total")
        Narration  = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Hidden_Row  = request.args.get("Hidden_Row")
        Discount_Amount  = request.args.get("Discount_Amount")
        table_name = request.args.get("table_name")
        if all([_id,Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,Narration,Voucher_Prefix,Hidden_Row,Discount_Amount,table_name]):
            cursor.execute("insert into old_kot_voucher(_id,Invoice_No,Voucher_Date,Date_Created,Bill_Date,Timestamp,Ledger_Name,Billing_Name,Total,Narration,Voucher_Prefix,Hidden_Row,Discount_Amount,table_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(_id,Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,Narration,Voucher_Prefix,Hidden_Row,Discount_Amount,table_name))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted") 





    # else:
    #     return jsonify(error="invalid api key")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')== "payment_details":
        # id = request.args.get("_id")
        Payment_Voucher_Id = request.args.get("Payment_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Amount= request.args.get("Amount")
        Narration = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Mode_Of_Pay = request.args.get("Mode_Of_Pay")
        if all([Payment_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_Of_Pay]):
            cursor.execute("insert into payment_details(Payment_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_Of_Pay) values (%s,%s,%s,%s,%s,%s,%s)",(Payment_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_Of_Pay))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="succesfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')== "payment_voucher":
        # id = request.args.get("_id")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Ledger_Name = request.args.get("Ledger_Name")
        Total= request.args.get("Total")
        Mode_Of_Pay= request.args.get("Mode_Of_Pay")
        Narration = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Hidden_Row = request.args.get("Hidden_Row")
        if all([Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row]):
            cursor.execute("insert into payment_voucher(Voucher_Date,Date_Created,Timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')== "purchase_details":
        # id = request.args.get("_id")
        Purchase_Voucher_Id = request.args.get("Purchase_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Quantity = request.args.get("Quantity")
        Rate_per = request.args.get("Rate_per")
        Item_Discount = request.args.get("Item_Discount")
        Amount = request.args.get("Amount")
        Vat = request.args.get("Vat")
        Narration = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Totat_Discount = request.args.get("Totat_Discount")
        Ledger_Name = request.args.get("Ledger_Name")
        if all([Purchase_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Ledger_Name]):
            cursor.execute("insert into purchase_details(Purchase_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Ledger_Name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Purchase_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Ledger_Name))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')=="purchase_inventory_group":
        id = request.args.get("_id")
        groupname = request.args.get("Group_Name")
        parentgroup = request.args.get("Parent_Group")
        if all([id,groupname,parentgroup]):
            cursor.execute("insert into purchase_inventory_group(_id,GroupName,Parent_Group) values (%s,%s,%s)",(id,groupname,parentgroup))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')=="purchase_inventory_item":
        # id = request.args.get("_id")
        Name = request.args.get("Name")
        Code = request.args.get("Code")
        Alias = request.args.get("Alias")
        Group_Name = request.args.get("Group_Name")
        Unit_Of_Measurement= request.args.get("Unit_Of_Measurement")
        Rate_Of_VAT= request.args.get("Rate_Of_VAT")
        Opening_Balance = request.args.get("Opening_Balance")
        Price= request.args.get("Price")
        Default_Sales_Ledger = request.args.get("Default_Sales_Ledger")
        Default_Purchase_Ledger = request.args.get("Default_Purchase_Ledger")
        Favourite = request.args.get("Favourite")
        Narration = request.args.get("Narration")
        if all([Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration]):
            cursor.execute("insert into purchase_inventory_item(Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table')== "purchase_voucher":
        # id = request.args.get("_id")
        Invoice_No = request.args.get("Invoice_No")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        Bill_Date = request.args.get("Bill_Date")
        Bill_Date = parser.parse(Bill_Date)
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Ledger_Name= request.args.get("Ledger_Name")
        Billing_Name = request.args.get("Billing_Name")
        Total = request.args.get("Total")
        narration = request.args.get("narration")
        voucher_Prefix= request.args.get("voucher_Prefix")
        Hidden_Row = request.args.get("Hidden_Row")

        if all([Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row]):
            cursor.execute("insert into purchase_voucher(Invoice_No,Voucher_Date,Date_Created,Bill_Date,Timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "receipt_details" :
        # print request.args
        # id = request.args.get("_id")
        Receipt_Voucher_Id = request.args.get("Receipt_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Amount= request.args.get("Amount")
        Narration = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Mode_of_pay = request.args.get("Mode_of_pay")
        if all([Receipt_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_of_pay]):
            cursor.execute("insert into receipt_details(Reciept_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_of_pay) values (%s,%s,%s,%s,%s,%s,%s)",(Receipt_Voucher_Id,Item_Name,Amount,Narration,Voucher_Prefix,Voucher_Date,Mode_of_pay))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "receipt_voucher":
        # id = request.args.get("_id")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Ledger_Name = request.args.get("Ledger_Name")
        Total= request.args.get("Total")
        Mode_Of_Pay= request.args.get("Mode_Of_Pay")
        Narration = request.args.get("Narration")
        Voucher_Prefix = request.args.get("Voucher_Prefix")
        Hidden_Row = request.args.get("Hidden_Row")
        if all([Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row]):
            cursor.execute("insert into receipt_voucher(Voucher_Date,Date_Created,Timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Voucher_Date,Date_Created,timestamp,Ledger_Name,Total,Mode_Of_Pay,Narration,Voucher_Prefix,Hidden_Row))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "sales_details":
        # id = request.args.get("_id")
        sales_Voucher_Id = request.args.get("sales_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Quantity = request.args.get("Quantity")
        Rate_Per = request.args.get("Rate_Per")
        Item_Discount= request.args.get("Item_Discount")
        Amount= request.args.get("Amount")
        Vat = request.args.get("Vat")
        narration = request.args.get("narration")
        Voucher_Prefix= request.args.get("Voucher_Prefix")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Totat_Discount = request.args.get("Totat_Discount")
        Service_tax = request.args.get("Service_tax")
        kot_num = request.args.get("kot_num")
        Ledger_Name = request.args.get("Ledger_Name")
        if all([sales_Voucher_Id,Item_Name,Quantity,Rate_Per,Item_Discount,Amount,Vat,narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,kot_num,Ledger_Name]):
            cursor.execute("insert into sales_details(sales_Voucher_Id,Item_Name,Quantity,Rate_per,Item_Discount,Amount,Vat,Narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,kot_num,Ledger_Name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sales_Voucher_Id,Item_Name,Quantity,Rate_Per,Item_Discount,Amount,Vat,narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,kot_num,Ledger_Name))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    # elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "sales_inventory_group":
    #     id = request.args.get("_id")
    #     groupname = request.args.get("Group_Name")
    #     parentgroup = request.args.get("Parent_Group")
    #     if all([id, groupname, parentgroup]):
    #         cursor.execute("insert into accounts_group(_id,Group_Name,Parent_Group) values (%s,%s,%s)",(id, groupname, parentgroup))
    #         connection.commit()
    #         return jsonify(response="inserted")
    #     else:
    #         return jsonify(error="please provide necessary arguments")
    #     return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "sales_inventory_item":
        # id = request.args.get("_id")
        Name = request.args.get("Name")
        Code = request.args.get("Code")
        Alias = request.args.get("Alias")
        Group_Name = request.args.get("Group_Name")
        Unit_Of_Measurement= request.args.get("Unit_Of_Measurement")
        Rate_Of_VAT= request.args.get("Rate_Of_VAT")
        Opening_Balance = request.args.get("Opening_Balance")
        Price= request.args.get("Price")
        Default_Sales_Ledger = request.args.get("Default_Sales_Ledger")
        Default_Purchase_Ledger = request.args.get("Default_Purchase_Ledger")
        Favourite = request.args.get("Favourite")
        Narration = request.args.get("Narration")
        if all([Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration]):
            cursor.execute("insert into sales_inventory_item(Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name,Code,Alias,Group_Name,Unit_Of_Measurement,Rate_Of_VAT,Opening_Balance,Price,Default_Sales_Ledger,Default_Purchase_Ledger,Favourite,Narration))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "sales_voucher":
        # id = request.args.get("_id")
        Invoice_No = request.args.get("Invoice_No")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        Bill_Date = request.args.get("Bill_Date")
        Bill_Date = parser.parse(Bill_Date)
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Ledger_Name= request.args.get("Ledger_Name")
        Billing_Name = request.args.get("Billing_Name")
        Total = request.args.get("Total")
        narration = request.args.get("narration")
        voucher_Prefix= request.args.get("voucher_Prefix")
        Hidden_Row = request.args.get("Hidden_Row")
        Discount_Amount = request.args.get("Discount_Amount")
        mod_of_pay = request.args.get("mod_of_pay")
        mod_of_service = request.args.get("mod_of_service")
        discount_perc = request.args.get("discount_perc")
        deliver_add = request.args.get("deliver_add")
        if all([Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,mod_of_pay,mod_of_service,discount_perc,deliver_add]):
            cursor.execute("insert into sales_voucher(Invoice_No,Voucher_Date,Date_Created,Bill_Date,Timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,mod_of_pay,mod_of_service,discount_perc,deliver_add) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,mod_of_pay,mod_of_service,discount_perc,deliver_add))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "shifttable":
        # id = request.args.get("_id")
        ShiftDate = request.args.get("ShiftDate")
        ShiftDate = parser.parse(ShiftDate)
        StartVoucherNo = request.args.get("StartVoucherNo")
        StopVoucherNo = request.args.get("StopVoucherNo")
        SalesValue = request.args.get("SalesValue")
        OpeningBalance= request.args.get("OpeningBalance")
        CardAmount= request.args.get("CardAmount")
        CashInCounter = request.args.get("CashInCounter")
        CashTaken= request.args.get("CashTaken")
        TiltDifference = request.args.get("TiltDifference")
        ShiftStaffName = request.args.get("ShiftStaffName")
        Narration = request.args.get("Narration")
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if all([ShiftDate,StartVoucherNo,StopVoucherNo,SalesValue,OpeningBalance,CardAmount,CashInCounter,CashTaken,TiltDifference,ShiftStaffName,Narration, timestamp]):
            cursor.execute("insert into shifttable(ShiftDate,StartVoucherNo,StopVoucherNo,SalesValue,OpeningBalance,CardAmount,CashInCounter,CashTaken,TiltDifference,ShiftStaffName,Narration,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ShiftDate,StartVoucherNo,StopVoucherNo,SalesValue,OpeningBalance,CardAmount,CashInCounter,CashTaken,TiltDifference,ShiftStaffName,Narration,timestamp))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "stock_entry":
        Date = request.args.get("Date")
        Date = parser.parse(Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        Name = request.args.get("Name")
        Narration = request.args.get("Narration")
        if all([Date,Date_Created,timestamp,Name,Narration]):
            cursor.execute("insert into stock_entry(Date,Date_Created,timestamp,Name,Narration) values (%s,%s,%s,%s,%s)",(Date,Date_Created,timestamp,Name,Narration))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "stock_entry_details":
        Entry_id = request.args.get("Entry_id")
        Item_Name = request.args.get("Item_Name")
        Quantity = request.args.get("Quantity")
        Defective = request.args.get("Defective")
        Date = request.args.get("Date")
        Date = parser.parse(Date)
        if all([Entry_id,Item_Name,Quantity,Defective,Date]):
            cursor.execute("insert into stock_entry_details(Entry_id,Item_Name,Quantity,Defective,Date) values (%s,%s,%s,%s,%s)",(Entry_id,Item_Name,Quantity,Defective,Date))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "tempbill":
        # id = request.args.get("_id")
        itemname = request.args.get("itemname")
        groupname = request.args.get("groupname")
        price = request.args.get("price")
        quantity = request.args.get("quantity")
        addons= request.args.get("addons")
        order_Number= request.args.get("order_Number")
        ipaddress = request.args.get("ipaddress")
        orderstatus= request.args.get("orderstatus")
        reference = request.args.get("reference")
        Kot_Number = request.args.get("Kot_Number")
        if all([itemname,groupname,price,quantity,addons,order_Number,ipaddress,orderstatus,reference,Kot_Number]):
            cursor.execute("insert into tempbill(itemname,groupname,price,quantity,addons,order_Number,ipaddress,orderstatus,reference,Kot_Number) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(itemname,groupname,price,quantity,addons,order_Number,ipaddress,orderstatus,reference,Kot_Number))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "temp_sales_details":
        # id = request.args.get("_id")
        sales_Voucher_Id = request.args.get("sales_Voucher_Id")
        Item_Name = request.args.get("Item_Name")
        Quantity = request.args.get("Quantity")
        Rate_Per = request.args.get("Rate_Per")
        Item_Discount= request.args.get("Item_Discount")
        Amount= request.args.get("Amount")
        Vat = request.args.get("Vat")
        narration = request.args.get("narration")
        Voucher_Prefix= request.args.get("Voucher_Prefix")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Totat_Discount = request.args.get("Totat_Discount")
        Service_tax = request.args.get("Service_tax")
        table_name = request.args.get("table_name")
        isPrinted = request.args.get("isPrinted")
        isSaved = request.args.get("isSaved")
        kot_num = request.args.get("kot_num")
        if all([sales_Voucher_Id,Item_Name,Quantity,Rate_Per,Item_Discount,Amount,Vat,narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,kot_num]):
            cursor.execute("insert into temp_sales_details(sales_Voucher_Id,Item_Name,Quantity,Rate_Per,Item_Discount,Amount,Vat,narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,kot_num) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sales_Voucher_Id,Item_Name,Quantity,Rate_Per,Item_Discount,Amount,Vat,narration,Voucher_Prefix,Voucher_Date,Totat_Discount,Service_tax,table_name,isPrinted,isSaved,kot_num))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "temp_sales_voucher":
        # id = request.args.get("_id")
        Invoice_No = request.args.get("Invoice_No")
        Voucher_Date = request.args.get("Voucher_Date")
        Voucher_Date = parser.parse(Voucher_Date)
        Date_Created = request.args.get("Date_Created")
        Date_Created = parser.parse(Date_Created)
        Bill_Date = request.args.get("Bill_Date")
        Bill_Date = parser.parse(Bill_Date)
        timestamp = request.args.get("timestamp")
        timestamp = parser.parse(timestamp)
        Ledger_Name= request.args.get("Ledger_Name")
        Billing_Name = request.args.get("Billing_Name")
        Total = request.args.get("Total")
        narration = request.args.get("narration")
        voucher_Prefix= request.args.get("voucher_Prefix")
        Hidden_Row = request.args.get("Hidden_Row")
        Discount_Amount = request.args.get("Discount_Amount")
        table_name = request.args.get("table_name")
        deliver_add = request.args.get("deliver_add")
        if all([Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,table_name,deliver_add]):
            cursor.execute("insert into temp_sales_voucher(Invoice_No,Voucher_Date,Date_Created,Bill_Date,Timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,table_name,deliver_add) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Invoice_No,Voucher_Date,Date_Created,Bill_Date,timestamp,Ledger_Name,Billing_Name,Total,narration,voucher_Prefix,Hidden_Row,Discount_Amount,table_name,deliver_add))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    elif request.args.get('api_key') and request.args.get('api_key') == API_KEY and request.args.get('table') == "transcation_helper":
        date = request.args.get("date")
        date = parser.parse(date)
        transactionAmount = request.args.get("transactionAmount")
        voucherType = request.args.get("voucherType")
        voucherId = request.args.get("voucherId")
        debitLedgerID= request.args.get("debitLedgerID")
        creditLedgerID= request.args.get("creditLedgerID")
        narration = request.args.get("narration")
        voucher_Prefix= request.args.get("voucher_Prefix")
        if all([date,transactionAmount,voucherType,voucherId,debitLedgerID,creditLedgerID,narration,voucher_Prefix]):
            cursor.execute("insert into transcation_helper(date,transactionAmount,voucherType,voucherId,debitLedgerID,creditLedgerID,narration,voucher_Prefix) values (%s,%s,%s,%s,%s,%s,%s,%s)",(date,transactionAmount,voucherType,voucherId,debitLedgerID,creditLedgerID,narration,voucher_Prefix))
            connection.commit()
            return jsonify(response="inserted")
        else:
            return jsonify(error="please provide necessary arguments")
        return jsonify(response="successfully inserted")
    else:
        return jsonify(error="invalid api key")     



@app.route("/delete/")
def delete():
    if request.args.get('api_key') and request.args.get('api_key') == API_KEY:  
        id = request.args.get("id")
        if id:
            cursor.execute("delete from accounts_group where _id="+id)
            connection.commit()
            return jsonify(responce="succesfully deleted")
        else:
            return jsonify(error="please provide id") 
    else:
        return jsonify(error="invalid api key") 
      

if __name__ == "__main__":
    app.run(debug=True)

