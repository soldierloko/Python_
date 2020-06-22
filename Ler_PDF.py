import tabula as tb

#Lê o Arquivo PDF
arq = tb.read_pdf("C:\\Users\\bruno\\Downloads\\tabela Pr.pdf",pages="all")

#Transforma o PDF em CSV
tb.convert_into("C:\\Users\\bruno\\Downloads\\tabela Pr.pdf","C:\\Users\\bruno\\Downloads\\tabela Pr.csv",output_format= "csv", pages="all")

#print(arq)