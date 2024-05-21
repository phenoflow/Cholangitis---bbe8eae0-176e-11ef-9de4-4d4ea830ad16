# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J661.00","system":"readv2"},{"code":"J661600","system":"readv2"},{"code":"J661200","system":"readv2"},{"code":"J661100","system":"readv2"},{"code":"J661300","system":"readv2"},{"code":"J661000","system":"readv2"},{"code":"J661z00","system":"readv2"},{"code":"J661400","system":"readv2"},{"code":"J620100","system":"readv2"},{"code":"J661500","system":"readv2"},{"code":"J661y00","system":"readv2"},{"code":"97670.0","system":"readv2"},{"code":"34753.0","system":"readv2"},{"code":"35667.0","system":"readv2"},{"code":"41470.0","system":"readv2"},{"code":"15425.0","system":"readv2"},{"code":"25341.0","system":"readv2"},{"code":"33339.0","system":"readv2"},{"code":"24866.0","system":"readv2"},{"code":"15678.0","system":"readv2"},{"code":"40416.0","system":"readv2"},{"code":"66226.0","system":"readv2"},{"code":"51530.0","system":"readv2"},{"code":"44791.0","system":"readv2"},{"code":"10431.0","system":"readv2"},{"code":"64412.0","system":"readv2"},{"code":"K83.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cholangitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cholangitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cholangitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cholangitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
