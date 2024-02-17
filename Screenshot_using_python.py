import pyscreenshot
image=pyscreenshot.grab()
input_taken=input("Please enter the file name")
image.show()
image.save(input_taken)
