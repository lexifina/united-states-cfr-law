# Appendix G to Subpart G of Part 1—Numeric Identifiers
Numeric identifier | Definition | Comments and format | Mandatory (M) or optional (O)
<110> | Applicant | If Applicant is inventor, then preferably max. of 10 names; one name per line; preferable format: Surname, Other Names and/or Initials | M.
<120> | Title of Invention | | M.
<130> | File Reference | Personal file reference | M when filed prior to assignment or appl. number.
<140> | Current Application Number | Specify as: US 09/999,999 or PCT/US09/99999 | M, if available.
<141> | Current Filing Date | Specify as: yyyy-mm-dd | M, if available.
<150> | Prior Application Number | Specify as: US 09/999,999 or PCT/US09/99999 | M, if applicable include priority documents under 35 U.S.C. 119 and 120.
<151> | Prior Application Filing Date | Specify as: yyyy-mm-dd | M, if applicable.
<160> | Number of SEQ ID NOs | Count includes total number of SEQ ID NOs | M.
<170> | Software | Name of software used to create the "Sequence Listing" | O.
<210> | SEQ ID NO:#: | Response shall be an integer representing the SEQ ID NO shown | M.
<211> | Length | Respond with an integer expressing the number of bases or amino acid residues | M.
<212> | Type | Whether presented sequence molecule is DNA, RNA, or PRT (protein). If a nucleotide sequence contains both DNA and RNA fragments, the type shall be "DNA." In addition, the combined DNA/RNA molecule shall be further described in the <220> to <223> feature section | M.
<213> | Organism | Scientific name, i.e., Genus/species, Unknown or Artificial Sequence. In addition, the "Unknown" or "Artificial Sequence" organisms shall be further described in the <220> to <223> feature section | M.
<220> | Feature | Leave blank after <220>. <221-223> provide for a description of points of biological significance in the sequence | M, under the following conditions: If "n," "Xaa," or a modified or unusual L-amino acid or modified base was used in a sequence; if ORGANISM is "Artificial Sequence" or "Unknown"; if molecule is combined DNA/RNA.
<221> | Name/Key | Provide appropriate identifier for feature, from WIPO Standard ST.25 (2009), Appendices E and F to this subpart | M, under the following conditions: If "n," "Xaa," or a modified or unusual L-amino acid or modified base was used in a sequence.
<222> | Location | Specify location within sequence; where appropriate, state number of first and last bases/amino acids in feature | M, under the following conditions: If "n," "Xaa," or a modified or unusual L-amino acid or modified base was used in a sequence.
<223> | Other Information | Other relevant information; four lines maximum | M, under the following conditions: If "n," "Xaa," or a modified or unusual L-amino acid or modified base was used in a sequence; if ORGANISM is "Artificial Sequence" or "Unknown"; if molecule is combined DNA/RNA.
<300> | Publication Information | Leave blank after <30> | O.
<301> | Authors | Preferably max. of 10 named authors of publication; specify one name per line; preferable format: Surname, Other Names and/or Initials | O.
<302> | Title | | O.
<303> | Journal | | O.
<304> | Volume | | O.
<305> | Issue | | O.
<306> | Pages | | O.
<307> | Date | Journal date on which data published; specify as yyyy-mm-dd, MMM-yyyy or Season-yyyy | O.
<308> | Database Accession Number | Accession number assigned by database, including database name | O.
<309> | Database Entry Date | Date of entry in database; specify as yyyy-mm-dd or MMM-yyyy | O.
<310> | Patent Document Number | Document number; for patent-type citations only. Specify as, for example, US 09/999,999 | O.
<311> | Patent Filing Date | Document filing date, for patent-type citations only; specify as yyyy-mm-dd | O.
<312> | Publication Date | Document publication date, for patent-type citations only; specify as yyyy-mm-dd | O.
<313> | Relevant Residues | FROM (position) TO (position) | O.
<400> | Sequence | SEQ ID NO should follow the numeric identifier and should appear on the line preceding the actual sequence | M.
