me = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ«»؟،؛ءآأؤإئااًبةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٓٔٱٹپچڈڑژکڭگںھۀہۂۃۆۇۈۋیېےۓە"
org = "0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ٠١٢٣٤٥٦٧٨٩«»؟،؛ءآأؤإئااًبةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٓٔٱٹپچڈڑژکڭگںھۀہۂۃۆۇۈۋیېےۓە"

# for ch in me:
#     print(ch)

# for ch in org:
#     print(ch)

for ch in me:
    print(ch, " ", ch in org)
