# Laura Pasea, Sheng-Chia Chung, Mar Pujades-Rodriguez, Anoop D. Shah, Samantha Alvarez-Madrazo, Victoria Allan, James T. Teo, Daniel Bean, Reecha Sofat, Richard Dobson, Amitava Banerjee, Riyaz S. Patel, Adam Timmis, Spiros Denaxas, Harry Hemingway, 2024.

import sys, csv, re

codes = [{"code":"7J01300","system":"readv2"},{"code":"7H22600","system":"readv2"},{"code":"7M0U400","system":"readv2"},{"code":"SP21.12","system":"readv2"},{"code":"SP21.11","system":"readv2"},{"code":"SP21200","system":"readv2"},{"code":"SP21100","system":"readv2"},{"code":"T032","system":"readv2"},{"code":"V032","system":"readv2"},{"code":"T301","system":"readv2"},{"code":"Y321","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bleeding-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bleeding-postop---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bleeding-postop---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bleeding-postop---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
