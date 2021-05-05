# CPALMS-CertificateSpoofer
Spoofs CPALMS Certificate creation system

Reverse engineered the encryption system to make custom encrypted data that the certificate site reads to produce the certificate information.
Relatively easy to see what it does if you look at the source, all the important stuff is on line 17, but beware if you modify that section since some of the values like the hours and minutes I've left unassigned to variables and are static, as I do not know how they work and seemingly valid numbers come out invalid.

If the site says a 404 or something, add it to issues and enter what data you put into it and whether you modified the script.
