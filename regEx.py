# import re

# s = "asdf from Felix ITs"

# ans = re.search("^Hello", s)

# if ans:
#     print('Success')
    
# else:
#     print('Faild')



# import re

# s = "Hello from python"

# ans = re.findall("[a-m]", s)

# print(ans)





# ends with


# import re

# s = "Hello from nohtyp"


# ans = re.findall("on$", s)


# if ans : 
#     print('end with on')
# else : 
#     print('does not ents with on')


# from reportlab.pdfgen import canvas
# from reportlab_qr_code import qr_draw

from reportlab.pdfgen import canvas
from reportlab_qr_code import qr_draw

c = canvas.Canvas("felix2.pdf")
qr_draw(c, "https://www.felix-its.com/", x="1cm", y="1cm", size="10cm", bg="#eeeeee" , )

c.save()


