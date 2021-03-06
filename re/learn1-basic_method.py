# Mengimport library regular expression yaitu re
import re

sub_string1= 'jett'
sub_string2= 'revive'

string1= 'jett revive me jett'

# -------------- re.match(pattern, string):) ----------------
# Mengecek apakah substring merupakan awal dari sebuah string
match1= re.match(sub_string1, string1)
print(match1)
print(match1.group(0))
print(match1.start())
print(match1.end())

match2= re.match(sub_string2, string1)
print(match2)

# -------------- re.search(pattern, string) ----------------
# Mirip dengan match tapi search tidak terbatas pada kata pertama
search1= re.search(sub_string2, string1)
print(search1)

search2= re.search(sub_string1, string1)
print(search2)

# -------------- re.findall(pattern, string) ----------------
# Mirip dengan search tapi bisa menemukan lebih dari satu pattern
findall1= re.findall(sub_string2, string1)
print(findall1)

# -------------- re.sub(pattern, repl, string) ----------------
# Mengganti sub string pada suatu string dengan sub string yang lain
# Jika sub string yang dicari tidak ada, maka hanya akan mengembalikan string tersebut
change_substring= 'revive'
replace_substring= 'kill'

sub1= re.sub(change_substring, replace_substring, string1)
print(sub1)

# -------------- re.split(pattern, string) ----------------
split1= re.split(r'\.', '100.000.0.00') # kita juga bisa mendefinisikan maxsplit
print(split1)

# Split yang lebih kompleks, memisah titik atau koma atau minus
split2= re.split(r'[,.-]', '100.000,0-00')
print(split2)

# -------------- re.compile() ----------------
# Penjelasannya susah

# Pertama kita membuat variabel dengan memanggil method compile
# Yang parameternya string yang mau dicari atau pattern
pattern1= re.compile('jett')

# Lalu jika kita ingin memanggil method findall dengan pattern tersebut
# Kita tinggal melakukan seperti ini
compile1= pattern1.findall(string1)
print(compile1)

# Melakukan sub
compile2= pattern1.sub(r'sova', string1)
print(compile2)

# -------------- re.finditer(pattern, string) ----------------
# Mirip dengan findall tapi ini mengembalikan objek bukan list
string2= '''
jett
12312312313
kill joy raze recon noob kebab
'''

finditer1= re.finditer(r'e', string2)

for match in finditer1:
    print(match)

