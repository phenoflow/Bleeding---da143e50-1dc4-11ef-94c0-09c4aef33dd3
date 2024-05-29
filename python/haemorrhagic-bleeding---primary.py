# Laura Pasea, Sheng-Chia Chung, Mar Pujades-Rodriguez, Anoop D. Shah, Samantha Alvarez-Madrazo, Victoria Allan, James T. Teo, Daniel Bean, Reecha Sofat, Richard Dobson, Amitava Banerjee, Riyaz S. Patel, Adam Timmis, Spiros Denaxas, Harry Hemingway, 2024.

import sys, csv, re

codes = [{"code":"F42y400","system":"readv2"},{"code":"G617.00","system":"readv2"},{"code":"G602.00","system":"readv2"},{"code":"G620.00","system":"readv2"},{"code":"G610.00","system":"readv2"},{"code":"S62..13","system":"readv2"},{"code":"SP21.00","system":"readv2"},{"code":"G61..00","system":"readv2"},{"code":"F42y100","system":"readv2"},{"code":"G61z.00","system":"readv2"},{"code":"G601.00","system":"readv2"},{"code":"G618.00","system":"readv2"},{"code":"F436100","system":"readv2"},{"code":"S627.00","system":"readv2"},{"code":"G613.00","system":"readv2"},{"code":"F4K2800","system":"readv2"},{"code":"G62z.00","system":"readv2"},{"code":"G614.00","system":"readv2"},{"code":"S628.00","system":"readv2"},{"code":"G623.00","system":"readv2"},{"code":"G60..00","system":"readv2"},{"code":"G615.00","system":"readv2"},{"code":"Gyu6200","system":"readv2"},{"code":"F404500","system":"readv2"},{"code":"G61..11","system":"readv2"},{"code":"F42y500","system":"readv2"},{"code":"G621.00","system":"readv2"},{"code":"FyuH400","system":"readv2"},{"code":"G605.00","system":"readv2"},{"code":"F42y300","system":"readv2"},{"code":"S62..12","system":"readv2"},{"code":"G61..12","system":"readv2"},{"code":"G682.00","system":"readv2"},{"code":"2BB8.00","system":"readv2"},{"code":"G606.00","system":"readv2"},{"code":"F42y.11","system":"readv2"},{"code":"F436000","system":"readv2"},{"code":"2BB5.00","system":"readv2"},{"code":"Gyu6100","system":"readv2"},{"code":"G62..00","system":"readv2"},{"code":"G612.00","system":"readv2"},{"code":"G60z.00","system":"readv2"},{"code":"G680.00","system":"readv2"},{"code":"15A1.00","system":"readv2"},{"code":"15A6.00","system":"readv2"},{"code":"H356","system":"readv2"},{"code":"I60","system":"readv2"},{"code":"T810","system":"readv2"},{"code":"I690","system":"readv2"},{"code":"H431","system":"readv2"},{"code":"S066","system":"readv2"},{"code":"I62","system":"readv2"},{"code":"I692","system":"readv2"},{"code":"H450","system":"readv2"},{"code":"I61","system":"readv2"},{"code":"S065","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bleeding-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["haemorrhagic-bleeding---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["haemorrhagic-bleeding---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["haemorrhagic-bleeding---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
