[section files]

make.conf.oldprofile: [
# These settings were set by the metro build script that automatically built this stage.
# Please consult /etc/portage/make.conf.example for a more detailed example.

ACCEPT_KEYWORDS="$[portage/ACCEPT_KEYWORDS:zap]"
FEATURES="$[portage/FEATURES:zap]"
CHOST="$[portage/CHOST:zap]"
CFLAGS="$[portage/CFLAGS:zap]"
CXXFLAGS="$[portage/CFLAGS:zap]"
LDFLAGS="$[portage/LDFLAGS:zap]"
USE="$[portage/USE:zap]"
]

make.conf.newprofile: [
# These settings were set by the metro build script that automatically built this stage.
# Please consult /etc/portage/make.conf.example for a more detailed example.

FEATURES="$[portage/FEATURES:zap]"
CFLAGS="$[portage/CFLAGS:zap]"
CXXFLAGS="$[portage/CFLAGS:zap]"
LDFLAGS="$[portage/LDFLAGS:zap]"
USE="$[portage/USE:zap]"

# Portage Tree
SYNC="https://github.com/fearedbliss/Funtoo-ARBOL.git"

# Portage Source Repository
GENTOO_MIRRORS="http://medd.homeip.net:3333/funtoo/releases/14.1/"

# Portage Binary Repository
PORTAGE_BINHOST="http://medd.homeip.net:3333/funtoo/releases/14.1/packages"

# Default Portage Options
EMERGE_DEFAULT_OPTS="--with-bdeps=y --binpkg-respect-use=n"
]

locale.gen: [
# /etc/locale.gen: list all of the locales you want to have on your system
#
# The format of each line:
# <locale> <charmap>
#
# Where <locale> is a locale located in /usr/share/i18n/locales/ and
# where <charmap> is a charmap located in /usr/share/i18n/charmaps/.
#
# All blank lines and lines starting with # are ignored.
#
# For the default list of supported combinations, see the file:
# /usr/share/i18n/SUPPORTED
#
# Whenever glibc is emerged, the locales listed here will be automatically
# rebuilt for you.  After updating this file, you can simply run `locale-gen`
# yourself instead of re-emerging glibc.

en_US.UTF-8 UTF-8
]

proxyenv: [
<?python
for x in ["http_proxy","ftp_proxy","RSYNC_PROXY"]:
	if os.environ.has_key(x):
		print x+"=\""+os.environ[x]+"\""
	else:
		print "# "+x+" is not set"
?>
]

[section files]

motd: [
$[[files/motd/extra:lax]]

 >>> Release:                       $[target/base]
 >>> Version:                       $[target/version]
 >>> Build:			    $[target/count]
 >>> Created by:                    $[release/author]
$[[files/motd/trailer:lax]]

 NOTE: This message can be removed by deleting /etc/motd.

]
