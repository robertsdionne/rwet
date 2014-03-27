## <f0.M> {}
# Last edited on 1998-12-12 04:15:23 by stolfi
#
# DIFFERENCES BETWEEN INTERLN.EVT AND THE PRESENT FILE
# By Jorge Stolfi since Sep 1997
#
# I made many changes to the format and comments
# of Gabriel's INTERLN.EVT, after fetching it on Sep/Oct 1997.
#
# * I converted the file to the EVA alphabet.  This step is
#   described in more detail in section <f0.V>.
#
# * I expanded lines with the "[|]" notation into line pairs
#   with different transcriber codes.  This step is described
#   in section <f0.U>.
#
# * I split the interlinear into many separate files: one file
#   for each page, containing only comments, and one file for each
#   "text unit" or "locus" (block of homogeneous-looking text) within
#   the page. This step is detailed in section <f0.S>.
#   
# * I replaced some non-FSG characters found in INTERLN.EVT by "*" or by
#   valid EVA characters, as it seemed appropriate, usually leaving the 
#   original as an {}-comment.
#   
# * I fixed many missing or bogus "-" and "=".
#
# * I fixed several line-breaking errors in INTERLN.EVT,
#   mostly cases where the last character of a line was omitted and
#   entered as a separate word on the following line. I tried to
#   record all these fixes in section <f0.W>.
#   
# * I reassigned the text unit codes  in a more consistent
#   manner across the manuscript.  Specifically, to each *set* of
#   labels in a text unit (e.g. all the stars, or all the spokes) I
#   assigned a single text unit code, e.g. "L1", "L2", etc..
#
# * I assigned also to the "anonymous" units (paragraph-formatted text) 
#   an explicit "P" code, or "P1", "P2", ... on pages where the
#   paragraphed text was broken by labels or other kinds of text.
#   (There are a few exceptions; for instance, on f66r (the three-way
#   table), I used "R" for the anonymous locus (the right-hand
#   column).
#
# * I added various new transcriptions, mainly by John Grove
#   and myself, plus some items by R. Zandbergen and R. Firth. 
#
# * I merged Takeshi Takahashi's complete transcription with the
#   interlinear.   See seection <f0.K>.
# 
# * I moved all comments relating to a specific text unit to the 
#   beginning of that unit. Sometimes this required splitting,
#   rearranging, or otherwise editing the comments.
#
# * I removed all comments of the form "# page NNN"  since that
#   numbering was inconsistent with the binding order. (For one thing,
#   the last page f116v, which should be even, was numbered 235).
# 
# * I replaced the word "folio" in comments by "panel" or "page", 
#   whenever it meant only one face of a folio (or one part of a
#   multi-part fold-out).
#   
# * I added many descriptive comments, and merged into the file 
#   several scattered databases (such as Jim Reeds's color usage
#   tables, Petersen's plant names, etc.)
#   
# * I fixed the line locators <...> of labels so that all 
#   transcriptions of the same label now have the same line locator.
#   I retained the original locators as {}-comments at the
#   end of each line.  
# 
# * I split multiline labels so that each line of each label 
#   is now entered in a separate line of the file, with a distinct
#   line locator. (Embedded "-"s should now be used only for intrusions of
#   a figure or a vellum defect in a single line of the manuscript.)
#
# * I appended a "=" to the end of each label and isolated text line.  
#   For multiline labels, I used "-" to terminate each line but the
#   last one.
#
# * I regularized the transcription of circular text, sometimes
#   shifting the starting point. I used an "=" terminator where the
#   starting poing is clearly marked, "-" where it is merely a
#   larger-than-normal gap, and "." where it is an arbitrarily chosen
#   word gap.
# 
# * I replaced all page header lines (containing only a page locator
#   <...> and no Voynich text) by special "#" comments, compatible 
#   with R. Zandbergen's VTX tool. These comments have the form
#
#       ## <fNNN>        {$I=i $Q=q $P=p $L=l $H=h $X=x}
#
#   where 
#     
#       "NNN" is a page f-number (folio, side, and division, e.g f86v3)
#       "i"   is the section code ("T" for text, "H" for herbal, etc.);
#       "q"   is the quire code, a letter in [A-T];
#       "p"   is a letter in [A-Z] identifying the panel within the quire;
#       "l"   is the "language" in Currier's sense, "A" or "B";
#       "h"   is the calligraphic "hand", a character in [1-5XY];
#       "x"   is a miscellaneous attribute (a letter). 
#
#   The "$L" and "$H" attributes are omitted when unknown. The "$X"
#   attribute is present only for page f17r, which is marked "$X=U"
#   (for the extraneous writing?).
#
#   Be warned that there are some discrepancies between these "$I"
#   attributes and the section recorded in Stolfi's UNITS file. The
#   UNITS file is more conservative, and assigns section "?" to some
#   text-only pages whose "$I"-codes were apparently assigned by
#   analogy with adjacent pages.  Moreover, the UNITS file does
#   not distinguish between "astro" and "cosmo" pages.
#     
# * I also added "unit header lines", similar to the page headers above,
#   at the start of each text unit within a page.  The format of 
#   these unit headers is 
#
#       ## <fNNN.UU>     {}
#
#   where <fNNN> is the page locator, and "UU" is the tag identifying
#   the unit ("locus") within the page. Note that unit headers are
#   distinguished from page headers by the "." in the locator. The
#   empty attribute list "{}" was added for uniformity and future
#   expansion.
#
# * I replaced purely alphabetic line numbers "a" and "b" by "0a" 
#   and "0b".  Now the line number always begins with digit, and the
#   unit code always begins with a letter.
#   
# * I created dummy files for all the missing pages (as deduced from 
#   the folio numbers in the VMs itself).  For that purpose, I assumed
#   each missing folio had only two panels (recto and verso), and
#   arbitrarily assigned them "$P"-codes higher than the "non-missing"
#   panels, and section "$I"-code "M" (for "missing").
#
# * I hereby apologize for using so many "I"s in this section.
#
