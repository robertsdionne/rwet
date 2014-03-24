## <f0.V> {}
# Last edited on 1998-12-05 11:25:59 by stolfi
#
# CONVERSION OF INTERLN.EVT TO THE EVA ENCODING
# Jorge Stolfi 05 Nov 1997 (Corrected 31 Mar 1998)
#
# This step was done with "fsg2eva", an AWK
# script. The main part of the script follows:
#
#   function fsg_to_eva(txt)
#   {
#     # Converts a chunk of comment-free FSG text to EVA
#
#     # We discard  "%" and "!" since the conversion
#     # will destroy synchronism anyway.
#     gsub(/[% !]/, "", txt);
#
#     # Now convert
#     gsub(/IIIE/, "iiil",  txt);
#     gsub(/IIIK/, "iiim",  txt);
#     gsub(/IIIL/, "iiin",  txt);
#     gsub(/IIIR/, "iiir",  txt);
#     gsub(/IIE/,  "iil",   txt);
#     gsub(/IIK/,  "iim",   txt);
#     gsub(/IIL/,  "iin",   txt);
#     gsub(/IIR/,  "iir",   txt);
#     gsub(/IE/,   "il",    txt);
#     gsub(/IK/,   "im",    txt);
#     gsub(/IL/,   "in",    txt);
#     gsub(/IR/,   "ir",    txt);
#     gsub(/HZ/,   "cth",   txt);
#     gsub(/PZ/,   "cph",   txt);
#     gsub(/DZ/,   "ckh",   txt);
#     gsub(/FZ/,   "cfh",   txt);
#     gsub(/2/,    "s",     txt);
#     gsub(/4/,    "q",     txt);
#     gsub(/6/,    "g",     txt);
#     gsub(/7/,    "j",     txt);
#     gsub(/8/,    "d",     txt);
#     gsub(/A/,    "a",     txt);
#     gsub(/C/,    "e",     txt);
#     gsub(/D/,    "k",     txt);
#     gsub(/E/,    "l",     txt);
#     gsub(/F/,    "f",     txt);
#     gsub(/G/,    "y",     txt);
#     gsub(/H/,    "t",     txt);
#     gsub(/I/,    "i",     txt);
#     gsub(/K/,    "m",     txt);
#     gsub(/L/,    "n",     txt);
#     gsub(/M/,    "iin",   txt);
#     gsub(/N/,    "in",    txt);
#     gsub(/O/,    "o",     txt);
#     gsub(/P/,    "p",     txt);
#     gsub(/R/,    "r",     txt);
#     gsub(/S/,    "sh",    txt);
#     gsub(/T/,    "ch",    txt);
#     gsub(/V/,    "v",     txt);
#     gsub(/Y/,    "x",     txt);
#
#     return txt
#   }
#
# This procedure was applied to the Voynich text proper, preserving
# the '#' and '{}' comments as well as the location codes.
#
# I had to edit manually some '{}' comments that contained Voynich
# characters in FSG or Currier notation.  The units affected by this bug 
# were
#
#   f100r.P1  f100r.m  f100v.M  f103r.P  f104r.P  f49v.P  f65v.P
#   f66r.R    f76r.R   f89r1.b  f89r2.b
#
# Note: The 05 Nov 1997 version of this script incorrectly mapped "IK"
# to "ik" instead of "im". This error affected 79 lines of INTERLN.EVT
# representing about 50 distinct words. The error was corrected on 31
# Mar 1998, by manually editing the EVA translation of those lines.
# The endings "IIIK", "IIK", and "K" were not affected by this error.
#
