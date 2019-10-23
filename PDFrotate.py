import PyPDF4

while True:
    name = input('请输入文件名：')
    try:
        minutesFile = open(name, 'rb')
        break
    except FileNotFoundError:
        print('文件未找到！')

pdfReader = PyPDF4.PdfFileReader(minutesFile, strict=False)
while True:
    try:
        pgnum = input('请输入要旋转的页码（第一页为0）：')
        page = pdfReader.getPage(int(pgnum))
        break
    except IndexError:
        print('页码超出范围！')
        continue

print('请选择旋转方向：1）顺时针 2）逆时针')
while True:
    pgdirect = input('请输入：')
    if int(pgdirect) == 1:
        while True:
            try:
                pgangle = input('请输入旋转角度（90度的整数倍）：')
                page.rotateClockwise(int(pgangle))
                break
            except AssertionError:
                print('角度请输入90整数倍！')
                continue
        break
    elif int(pgdirect) == 2:
        while True:
            try:
                pgangle = input('请输入旋转角度（90度的整数倍）：')
                page.rotateCounterClockwise(int(pgangle))
                break
            except AssertionError:
                print('角度请输入90整数倍！')
                continue
        break
    else:
        print('请输入1或2')

pdfWriter = PyPDF4.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
print('转换完成')
minutesFile.close()
