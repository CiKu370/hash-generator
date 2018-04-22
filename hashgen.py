import sys , hashlib , zlib , time , random , os , time

"""
__Author__  = Ci Ku ~ debby anggraini a.k.a xnver404
__Name__    = hash generator
__version__ = 3.4.1
__Code__    = python
__Github__  = https://github.com/ciku370
__Date__    = 21 - 4 - 2018
__Team__    = Blackhole Security
__License__ = GNU General Public License V.3

(c) debby anggraini 2018

"""

if sys.platform == "linux2" or sys.platform == "linux":
	B = "\033[34;1m"
	W = "\033[0m"
	C = "\033[36;1m"
	G = "\033[32;1m"
	R = "\033[31;1m"
	Y = "\033[33;1m"
	X = "\033[35;1m"

	rand = (B,C,G,R,Y,X)
	P = random.choice(rand)

elif sys.platform == "win32":
	B = ''
	W = ''
	C = ''
	G = ''
	R = ''
	P = ''
	Y = ''
	X = ''

try:
	import passlib , progressbar
except ImportError:
	print (R+"\n["+W+"!"+R+"] "+G+"module "+W+"passlib or progressbar"+G+"not installed"+W+"\n")
	sys.exit()

os.system("clear")
print (P+"\n....................................................................")
print (P+".##.....##....###.....######..##.....##..######...########.##....##.")
print (P+".##.....##...##.##...##....##.##.....##.##....##..##.......###...##.")
print (P+'.##.....##..##...##..##.......##.....##.##........##.......####..##.')
print (P+".#########.##.....##..######..#########.##...####.######...##.##.##.")
print (P+".##.....##.#########.......##.##.....##.##....##..##.......##..####.")
print (P+".##.....##.##.....##.##....##.##.....##.##....##..##.......##...###.")
print (P+".##.....##.##.....##..######..##.....##..######...########.##....##.")
print (P+"........................."+W+" Hash Generator "+P+"...........................\n")

try:
	x = raw_input(B+"["+W+"+"+B+"] "+G+"String "+B+": "+W)
except NameError:
	print (R+"\n["+W+"!"+R+"] "+G+"use "+W+"python2.7\n")
	quit()

print (B+"["+W+"!"+B+"] "+G+"Generate Hash "+W+". . . ."+G+" Please Wait !!!"+W)
time.sleep(0.5)

# mysql1323
from passlib.hash import mysql323
mysql1323 = mysql323.encrypt(x)
print (R+"\n["+W+"01"+R+"] "+G+"MySQL 3.2.3         "+B+": "+W+mysql1323)

# mysql141
from passlib.hash import mysql41
mysql141 = mysql41.encrypt(x)
print (R+"["+W+"02"+R+"] "+G+"MySQL 4.1           "+B+": "+W+mysql141)

# mssql2000
from passlib.hash import mssql2000 as m20
mssql2000 = m20.encrypt(x)
print (R+"["+W+"03"+R+"] "+G+"MSSQL 2000          "+B+": "+W+mssql2000)

# mssql2005
from passlib.hash import mssql2005 as m25
mssql2005 = m25.encrypt(x)
print (R+"["+W+"04"+R+"] "+G+"MSSQL 2005          "+B+": "+W+mssql2005)

# md4
m = hashlib.new("md4")
m.update(x)
md4 = m.hexdigest()
print (R+"["+W+"05"+R+"] "+G+"MD4                 "+B+": "+W+md4)

# md5
m = hashlib.new("md5")
m.update(x)
md5 = m.hexdigest()
print (R+"["+W+"06"+R+"] "+G+"MD5                 "+B+": " +W+md5)

# sha1
m = hashlib.new("sha1")
m.update(x)
sha1 = m.hexdigest()
print (R+"["+W+"07"+R+"] "+G+"SHA1                "+B+": "+W+sha1)

# Sha224
m = hashlib.new("sha224")
m.update(x)
sha224 = m.hexdigest()
print (R+"["+W+"08"+R+"] "+G+"SHA224              "+B+": "+W+sha224)

# Sha256
m = hashlib.new("sha256")
m.update(x)
sha256 = m.hexdigest()
print (R+"["+W+"09"+R+"] "+G+"SHA256              "+B+": "+W+sha256)

# Sha384
m = hashlib.new("sha384")
m.update(x)
sha384 = m.hexdigest()
print (R+"["+W+"10"+R+"] "+G+"SHA384              "+B+": "+W+sha384)

# Sha512
m = hashlib.new("sha512")
m.update(x)
sha512 = m.hexdigest()
print (R+"["+W+"11"+R+"] "+G+"SHA512              "+B+": "+W+sha512)

# Ripemd160
m = hashlib.new("ripemd160")
m.update(x)
ripemd160 = m.hexdigest()
print (R+"["+W+"12"+R+"] "+G+"RIPEMD160           "+B+": "+W+ripemd160)

# Whirlpool
m = hashlib.new("whirlpool")
m.update(x)
whirlpool = m.hexdigest()
print (R+"["+W+"13"+R+"] "+G+"WHIRLPOOL           "+B+": "+W+whirlpool)

# crc32
h = zlib.crc32(x)
crc32 = '%08X' % (h & 0xffffffff,)
print (R+"["+W+"14"+R+"] "+G+"CRC32               "+B+": "+W+crc32.lower())

# adler32
h = zlib.adler32(x)
adler32 = '%08X' % (h & 0xffffffff,)
print (R+"["+W+"15"+R+"] "+G+"ADLER32             "+B+": "+W+adler32.lower())

# des
from passlib.hash import des_crypt
des = des_crypt.encrypt(x)
print (R+"["+W+"16"+R+"] "+G+"DES Crypt           "+B+": "+W+des)

# Bsdi Crypt
from passlib.hash import bsdi_crypt
bsdi = bsdi_crypt.encrypt(x)
print (R+"["+W+"17"+R+"] "+G+"BSDi Crypt          "+B+": "+W+bsdi)

# Bigcrypt
from passlib.hash import bigcrypt
big = bigcrypt.encrypt(x)
print (R+"["+W+"18"+R+"] "+G+"BIGCrypt            "+B+": "+W+big)

# Crypt16
from passlib.hash import crypt16
crypt16 = crypt16.encrypt(x)
print (R+"["+W+"19"+R+"] "+G+"Crypt16             "+B+": "+W+crypt16)

# Md5 crypt
from passlib.hash import md5_crypt as mc
md5_crypt = mc.encrypt(x)
print (R+"["+W+"20"+R+"] "+G+"MD5 Crypt           "+B+": "+W+md5_crypt)

# Sha1 Crypt
from passlib.hash import sha1_crypt as mc
sha1_crypt = mc.encrypt(x)
print (R+"["+W+"21"+R+"] "+G+"SHA1 Crypt          "+B+": "+W+sha1_crypt)

# Sha256 Crypt
from passlib.hash import sha256_crypt as mc
sha256_crypt = mc.encrypt(x)
print (R+"["+W+"22"+R+"] "+G+"SHA256 Crypt        "+B+": "+W+sha256_crypt)

# Sha512 crypt
from passlib.hash import sha512_crypt as mc
sha512_crypt = mc.encrypt(x)
print (R+"["+W+"23"+R+"] "+G+"SHA512 Crypt        "+B+": "+W+sha512_crypt)

# Sun md5 crypt
from passlib.hash import sun_md5_crypt as mc
sun_md5_crypt = mc.encrypt(x)
print (R+"["+W+"24"+R+"] "+G+"Sun MD5 Crypt       "+B+": "+W+sun_md5_crypt)

# apache's md5 crypt
from passlib.hash import apr_md5_crypt as mc
apr_md5_crypt = mc.encrypt(x)
print (R+"["+W+"25"+R+"] "+G+"Apr MD5 Crypt       "+B+": "+W+apr_md5_crypt)

# phppass
from passlib.hash import phpass as mc
phpass = mc.encrypt(x)
print (R+"["+W+"26"+R+"] "+G+"PHPASS              "+B+": "+W+phpass)

# Cryptacular's PBDF2
from passlib.hash import cta_pbkdf2_sha1 as mc
cta_pbkdf2_sha1 = mc.encrypt(x)
print (R+"["+W+"27"+R+"] "+G+"CTA PBKDF2 SHA1     "+B+": "+W+cta_pbkdf2_sha1)

# Dwine PBDF2
from passlib.hash import dlitz_pbkdf2_sha1 as mc
dlitz_pbkdf2_sha1 = mc.encrypt(x)
print (R+"["+W+"28"+R+"] "+G+"Dlitz PBDKF2 SHA1   "+B+": "+W+dlitz_pbkdf2_sha1)

# Atlassian's PBKDF2 Hash
from passlib.hash import cta_pbkdf2_sha1 as mc
atl_pbkdf2_sha1 = mc.encrypt(x)
print (R+"["+W+"29"+R+"] "+G+"Atlassian's PBKDF2  "+B+": "+W+atl_pbkdf2_sha1)

# Django sha1
from passlib.hash import django_pbkdf2_sha1 as m25
django_sha1 = m25.encrypt(x)
print (R+"["+W+"30"+R+"] "+G+"Django PBKDF2 SHA1  "+B+": "+W+django_sha1)

# django sha256
from passlib.hash import django_pbkdf2_sha256 as m25
django_sha256 = m25.encrypt(x)
print (R+"["+W+"31"+R+"] "+G+"Django PBKDF2 SHA256"+B+": "+W+django_sha256)

# grup pbkdf2
from passlib.hash import grub_pbkdf2_sha512 as m25
grup_pbkdf2_sha512 = m25.encrypt(x)
print (R+"["+W+"32"+R+"] "+G+"Grub's PBKDF2       "+B+": "+W+grup_pbkdf2_sha512)

# SCRAM
from passlib.hash import scram as mc
scram = mc.encrypt(x)
print (R+"["+W+"33"+R+"] "+G+"SCRAM Hash          "+B+": "+W+scram)

# FreeBSD nthash
from passlib.hash import bsd_nthash as mc
bsd_nthash = mc.encrypt(x)
print (R+"["+W+"34"+R+"] "+G+"BSD nthash          "+B+": "+W+bsd_nthash)

# oracle11
from passlib.hash import oracle11 as m25
oracle11 = m25.encrypt(x)
print (R+"["+W+"35"+R+"] "+G+"Oracle11            "+B+": "+W+oracle11)

# lanManager
from passlib.hash import lmhash as m25
lmhash = m25.encrypt(x)
print (R+"["+W+"36"+R+"] "+G+"LanManager Hash     "+B+": "+W+lmhash)

# nthash
from passlib.hash import nthash as m25
nthash = m25.encrypt(x)
print (R+"["+W+"37"+R+"] "+G+"Windows NT-Hash     "+B+": "+W+nthash)

# cisco type 7
from passlib.hash import cisco_type7 as m25
cisco = m25.encrypt(x)
print (R+"["+W+"38"+R+"] "+G+"Cisco Type 7        "+B+": "+W+cisco)

# fhsp
from passlib.hash import fshp as m25
fhsp = m25.encrypt(x)
print (R+"["+W+"39"+R+"] "+G+"FHSP                "+B+": "+W+fhsp+"\n")

print (B+"["+W+"!"+B+"] "+G+"Success generate all hash "+W+"^^")
