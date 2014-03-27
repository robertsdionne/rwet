## <f0.I> {}
# Last edited on 1998-12-19 23:29:34 by stolfi
#
# FILE INTERLN.EVT VERSION 1.6
# Original description by by Gabriel Landini, 27 Sep 1996.
#
# [ Amendments/additions by J. Stolfi in "[]" ]
# 
# This file [ INTERLN.EVT ] is an interlinear version of the Voynich
# manuscript transcriptions from:
#
# a) P. Currier + new additions by the VMS list members (Jim Gillogly,
#    Jim Reeds, Mike Roe 1990-1994)
# b) the First Study Group (W. Friedman 1945-1949)
# c) other pages transcriptions (Don Latham 1996, Mike Roe 1996,
#    John H. Tiltman 1951, Karl Kluge 1992, Jim Reeds 1996)
#
# Please report any problems to: G.Landini@bham.ac.uk or to the Voynich
# list: Voynich@rand.org
#
# To join the Voynich list, send e-mail to Voynich-request@rand.org
#
# I will be responsible for keeping this file corrected and updated,
# so if you find any corrections, please contact me so they can be
# included in the next version of this file. All credits and thanks to
# the members of the Voynich list who made the original transcriptions
# available on line.
#
# This file was produced for the EVMT project (European Voynich
# Manuscript Transcription) by G. Landini and R. Zandbergen. We intend
# to transcribe the whole manuscript from T. C. Petersen's hand
# transcription of a set of photostats (1931) and from previous
# transcriptions available in machine readable format. The
# transcription will use the EVA alphabet that will allow translation
# of the document into the three most common alphabets associated with
# the manuscript: FSG alphabet, Currier's alphabet and Frogguy (by
# Jacques Guy).
#
# INTERLN17.EVT is based on the files: voynich.now, FSG.NEW and
# tiltman.txt with some small corrections. The Currier version was
# originally coded in Currier's alphabet. I translated it to FSG
# "enhanced" alphabet using Jacques Guy's BITRANS program and a set of
# rules CUR2FSG2 based on a message by Jim Reeds to the Voynich
# mailing list.
#
# The FSG alphabet does not contain the Currier characters 6 and 7. To
# preserve these, characters 6 and 7 were kept unchanged in the resulting
# FSG version. Currier 6 usually corresponds to K in FSG, while 7 was
# transcribed as K or 8 by the FSG team.
#
# I added a few "end of line" - and "end of paragraph" = marks where missing
# to keep line lengths equal between versions.
# All double spaces ",," were replaced with single spaces.
#
# FORMAT OF THIS FILE
# -------------------
#
# Logical divisions
# -----------------
# 
# The file is divided into logical "pages", which are subdivided into 
# "units", so that each unit contains only one type of text (paragraphs,
# labels, circular lines, etc; see section <f0.S> for more details.
#
# 
# Locators
# --------
# 
# [ Locators are constructs used to identify a page, a logical text
# unit, or a line of the VMS. Locators usually ] appear in angle brackets <>.
#
# The format of a [ page locator ] is: "f" plus the folio number, plus
# "r" for "recto" or "v" for "verso", and sometimes a further number
# for complex folios, [ all within <> ]. Ex: <f1v> indicates folio 1
# verso; [ <f101r2> indicates the second page of the fold-out folio 101,
# recto. See Jim Reeds site for a complete list of folios and 
# their division into pages. ]
#
# [ A unit locator has the form <fNNN.UU> where <fNNN> is the page
# locator and UU is a tag that identifies the unit within the page:
# typically "P" or "P1", "P2",... for paragraph-formatted blocks,
# "L1", "L2", ... for labels, and so on. ]
#
# [ A line locator has the form <fNNN.UU.LL;T> where <fNNN.UU> is
# the unit locator; LL is the line number; and T is the transcriber's
# code.
#
# The line number is a non-negative integer, optionally followed by a
# lowercase letter { a ... e }. The transcriber code is an uppercase
# letter. ]
#
# In a few places there was a "first" line not present in one of the
# other versions. These lines were numbered [ "0", or "0a", "0b",
# etc... Examples: <f41v.T.0;C>, <f84v.P.0a;C>, <f84v.P.0b;F>. ]
#
# The unit tags and line numbers for labels and other non-paragraph
# text were standardized across versions, in all cases where there
# were conflicts. The original locators were usually retained as '{}'
# comments at the end of the line. ]
#
#
# Line format
# -----------
#
# [ Each line in the file can be 
#
#   (a) a /line comment/, identified by a "#" in column 1.
#  
#   (b) a /page header/ or /unit header/, containing a page or unit locator
#       in column 1, followed by "parsable information";
#  
#   (c) a /data line/, with a line locator in columns 1-19 plus one line of
#       Voynich text starting on column 20 (which may contain in-line comments).
#
# To simplify parsing by Unix tools, the page/unit header lines (b)
# were "passivated" by inserting "## " in front of them. These are the
# only lines that begin with "##". ]
#
# As in the original transcription files, text limited by curly brackets {}
# is a comment.
#
#
# Transcriber codes
# -----------------
#
# [ The following transcriber codes were inherited from INTERLN.EVT: ]
#
#   C: Currier's transcription plus new additions from members of the
#      voynich list as found in the file voynich.now.
#   F: First study group's (Friedman's) transcription including various
#      items as found in the file FSG.NEW.
#   T: John Tiltman's transcription of some pages.
#   L: Don Latham's recent transcription of some pages.
#   R: Mike Roe's recent transcription of some pages.
#   K: Karl Kluge's transcription of some labels from Petersen's copies.
#   J: Jim Reed's transcription of some previously unreadable characters.
#   
# [ The following codes were added by J. Stolfi after 05 Nov 1997,
# in the unfolding of "[|]" groups:
#
#   D: second choice from [|] in "C" lines.
#   G: second choice from [|] in "F" lines, mostly from [1609|16xx].
#   I: second choice from [|] in "J" lines.
#   Q: second choice from [|] in "K" lines.
#   M: second choice from [|] in "L" lines. 
#   
# The following codes were assigned by J. Stolfi for use in 
# "new" transcriptions:
#
#   H: Takeshi Takahashi's full transcription (see f0.K).
#   N: Gabriel Landini.
#   U: Jorge Stolfi.
#   V: John Grove.
#   P: Father Th. Petersen (a few readings reported by K. Kluge).
#   X: Denis V. Mardle.
#   Z: Rene Zandbergen.
# ]
#
# 
# Parsable information
# --------------------
#
# Rene Zandbergen has added the Parsable Information to this file:
#
# A special type of in-line comment appears after the [ page/unit
# locator in page/unit header lines (type b1) ]. We call this
# "parsable information". The information is coded in "variables" set
# to values specific for that [ page/unit ], to facilitate the parsing
# and filtering using VTT. The variable names are single characters
# preceded by the $ symbol and they take as value a single character:
#
#      $I = illustration type  (T,H,A,Z,B,C,P,S)
#           Text, Herbal, Astronomical, Zodiac, Biological, Cosmological,
#           Pharmaceutical or Stars.
#      $Q = Quire              (A-T)
#      $P = page in quire      (A-X)
#      $L = Currier's language (A,B)
#      $H = Currier's hand     (1,2,3,4,5,X,Y)
#      $N = has non-Voynich text   (Y)
#      $K = has key-like sequence  (Y)
#      $X = has extraneous writing (Y)
#
#    Ex:  <f5r> {$I=H $Q=A $P=I $L=A $H=1 $N=Y} indicates a Herbal page
#    in quire A, page I, Currier Language A, hand 1 and has non-Voynich
#    text. Refer to the VTT documentation for details on how to use the
#    parsable information.
#
#
# Filler characters
# -----------------
#
# [ The filler characters "!" and "%" are used to align the various
# version of the same line, with slightly different meanings. 
#
# The "%" filler is used for relatively long stretches (at least one
# full word, usually next to or across a line break) that were
# obviously skipped or lost in one particular transcription of a line.
# A "%" can be interpreted as "this transcription contains no
# information about this part of the VMS text." Thus a line that is
# omitted from a particular version is equivalent to a line full of
# "%"s.
#
# The "!" filler is used for all other purposes. It denotes a
# character or word break that was either skipped or lost, or that
# (according to the transcriber) does not exist. In particular "!" is
# generally used where other versions have {}-comments.
#
# It is always OK to insert a "!" anywhere in the Voynich text. It is
# also OK to use "!" instead of "%", although the latter is more
# informative, and can be handled differently when computing
# "majority" and "consensus" versions. That is, "%" means "no vote on
# this character" while "!" means "one vote for there being no
# character here".
#
# Note that the original INTERLN file used "%" and "!" as fillers
# with somewhat different meanings. ]
#
#
# Alternative versions
# --------------------
#
# The Friedman version (FSG.NEW) is composed of various items and
# therefore there are variations within FSG.NEW. [ In INTERLN.EVT,
# this variation was ] indicated as [A|B], meaning that one item has a
# character transcribed as an "A" and the other a "B". [ These '[|]'
# constructs were later unfolded into separate lines, identified by
# distinctive transcriber codes; see the table above. ]
#
# Because the brackets and the "or" symbol | also break the
# synchronism but do not indicate any Voynich characters in the
# sequence, the exclamation mark "!" was used to indicate that the
# other version has extra characters that do not code Voynich text. ]
#
# 
# Breaks and spaces
# -----------------
#
# [ Breaksin the text are indicated according to the EVA conventions:
#
#     ","  A dubious word break.
#
#     "."  A definite word break.
#
#     "-"  In line-final position: a line break within a paragraph.
#          Elsewhere: a major break in the text---an extra-wide
#          gap, an intruding figure, a vellum defect, etc..
#
#     "="  Always in line-final position: a paragraph break
#          (defined by extra interline space, use of <p> and <f> gallows,
#          incomplete previous line, end of page, etc.
# 
# The word breaks ("." and ",") are taken from the transcription. The
# figure, line, and paragraph breaks ("-" and "=") were inserted by
# the editord of the interlinear, by looking at the reproductions of
# the VMS, without regard for the transcriber's opinion. This should
# not matter much, since the line breaks are hardly in question, and
# most paragraph breaks are fairly obvious too.
#
# Every line must end with either "-" or "=", or, in the case of
# circular lines, with "." or ",". There should be at least one normal
# letter between two succesive break characters (",", ".", "-", or
# "=").
#
# ... ] 
#
