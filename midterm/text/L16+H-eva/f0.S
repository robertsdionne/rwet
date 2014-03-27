## <f0.S> {}
# Last edited on 1998-12-12 04:14:45 by stolfi
#
# SPLITTING LANDINI'S INTERLINEAR INTO TEXT UNITS
# J. Stolfi 12 Oct 1997
# 
# Overview
# 
#   To simplify(?) the handling and editing of the interlinear
#   file, I split each page into what I called "textual units".
# 
#   I defined a textual unit as a maximal subset of a page that 
#   is contiguous in "normal" reading order, and has 
#   homogeneous "text type"; which is one of:
# 
#     "parags"      
# 
#       Apparently prose, in multi-line paragraphs. The last line in
#       each paragraph ends with "=", other lines end with "-".
#       Paragraph boundaries are guessed from line spacing,
#       right-margin justification, and presence of <p> and <f>
#       gallows.
# 
#     "starred-parags"    
# 
#       Like parags, but with a star-like symbol in front of each
#       paragraph.
# 
#     "itemized-parags"
# 
#       Like parags, but with a single Voynich letter or symbol 
#       in front of each paragraph.  Here the letters are indicated in
#       "{}" comments; they are also listed separately as a "letters" unit.
# 
#     "circular-lines"
# 
#       Text where each line is written around a circle in some
#       diagram.  The lines are terminated by "=", "-", or "."
#       depending on how well is the starting point marked.
# 
#     "radial-lines"
# 
#       Text where each line is written along a ray in some diagram.
#       Each line is terminated by "=".
# 
#     "titles"
# 
#       Text where each line is a title for a page or figure.
#       This type includes John Grove's "titles" or "signatures",
#       non-justified lines found below some paragraphs.
#       Each title is terminated by "=".
# 
#     "itemized-lines"
# 
#       The right-hand column of an itemized list ("key-like
#       sequence").  Here each line of text is an "item" of the list,
#       and is terminated by "=".
# 
#     "labels"
# 
#       List of labels attached to parts of figures.
#       Also the column of words from the table in f66r (page 117).
#       Here each label is terminated by "=", and multiple
#       lines of the same label are separated by "-".
# 
#     "letters"
# 
#       The single-letter labels in itemized lists. Also the column of
#       single letters in f66r (page 117). Letter sequences written
#       horizontally are transcribed all on the same line, with "-"
#       separators. Other sequences are transcribed one letter per
#       line, with "=" terminators.
# 
#     "-"
#     
#       This "text type" is used for files or units that contain
#       no Voynich text, only comments.
#       
#     "?"
#     
#       This text type is used for units that (presumably) contain
#       Voynich text of unknown type (e.g. missing pages).
# 
# Unit numbering and file names
# 
#   Each unit is stored as a separate file named "fNNN.UU", where
#   "NNN" is the folio-based page number (folio, side, and division,
#   e.g. f85r2), and UU is the unit code within the page.
#   
#   Descriptive comments that apply to a whole panel are stored in a
#   separate file named "fNNN" (without location code). General
#   comments about the VMS were moved to files <f0.*>.
#   
#   Note that it was sometimes necessary to split a page with N
#   distinct text types into *more* than N units, in order to preserve
#   the "natural" ordering of the text. For example, the transcribed
#   "pharma" pages have blocks of normal text alternating with rows of
#   labels; each block of text and each row of labels have therefore
#   been made into a separate unit.
#   
#   Note that any logical page or textual unit that spans multiple panels
#   gets its page number from its first full-size panel, in "normal" reading
#   order.  So a page that spans panels f101r1 and f101r2 would be numbered
#   <f101r1>; whereas one that spans f101v1 and f101v2 would be numbered
#   <f101v2>.
#   
# Detailed description of files
# 
#   A detailed description of the splitting can be found in 
#   the "UNITS" file. Each line of UNITS describes one of the 
#   textual units above; it contains 8 fields separated by ":"
#   
#     [1] a 4-digit sequence number, which can be used to sort the
#         units in their "natural" reading order.
#       
#     [2] the file name (fNNN or fNNN.UU).
#     
#     [3] the "section", or apparent subject matter: "herbal", "bio", "cosmo", 
#         "pharma", "stars", "?" if unknown, or "-" if the file 
#         contains no text.
#       
#     [4] the "language" in Currier's sense ("A", "B", "?" if unknown, "-" if no text).
#     
#     [5] the "hand" ("1..5", "X", "Y", "?", or "-")
#     
#     [6] the type of text ("parags", "labels", etc.; see list above)
#
#     [7] a sequential page number ("p001".. "p234"), in binding order;
#         or "-" for files that are place-holders for missing folios.
#     
#     [8] other comments
#     
#   Any field may be followed by "?" denoting uncertainty.
#
