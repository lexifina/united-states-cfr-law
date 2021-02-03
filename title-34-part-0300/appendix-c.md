# Appendix C to Part 300—National Instructional Materials Accessibility Standard (NIMAS)
Under sections 612(a)(23)(A) and 674(e)(4) of the Individuals with Disabilities Education Act, as amended by the Individuals with Disabilities Education Improvement Act of 2004, the Secretary of Education establishes the NIMAS. Under section 674(e)(4) of the Act, the NIMAS applies to print instructional materials published after July 19, 2006. The purpose of the NIMAS is to help increase the availability and timely delivery of print instructional materials in accessible formats to blind or other persons with print disabilities in elementary and secondary schools.
Technical Specifications—The Baseline Element Set
The Baseline Element Set details the minimum requirement that must be delivered to fulfill the NIMAS. It is the responsibility of publishers to provide this NIMAS-conformant XML content file, a package file (OPF), a PDF-format copy of the title page (or whichever page(s) contain(s) ISBN and copyright information), and a full set of the content's images. All of the images included within a work must be provided in a folder and placeholders entered in the relevant XML document indicating their location (all images must be included). The preferred image type is SVG, next is either PNG or JPG format. Images should be rendered in the same size/proportion as their originals at 300 dpi. Images should be named with relative path filenames in XML files (example: img id="staricon4" src="./images/U10C02/staricon4.jpg" alt="star icon").
NIMAS-conformant content must be valid to the NIMAS 1.1 [see ANSI/NISO Z39.86 2005 or subsequent revisions]. In addition, files are required to use the tags from the Baseline Element Set when such tags are appropriate. Publishers are encouraged to augment the required Baseline Element Set with tags from the Optional Element Set (elements not included in the Standard) as applicable. For the purposes of NIMAS, appropriate usage of elements, both baseline and optional, is defined by the DAISY Structure Guidelines. Files that do not follow these guidelines in the selection and application of tags are not conformant to this Standard. Both optional elements and appropriate structure guidelines may be located within Z39.86-2002 and Z39.86-2005 available from http://www.daisy.org/z3986/. Use of the most current standard is recommended.
The Baseline Element Set
Element | Description
a. Document-level tags
dtbook | The root element in the Digital Talking Book DTD. <dtbook>contains metadata in <head>and the contents itself in <book>.
head | Contains metainformation about the book but no actual content of the book itself, which is placed in <book>.
book | Surrounds the actual content of the document, which is divided into <frontmatter>, <bodymatter>, and <rearmatter>. <head>, which contains metadata, precedes <book>.
meta | Indicates metadata about the book. It is an empty element that may appear repeatedly only in <head>. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
b. Structure and Hierarchy
frontmatter | Usually contains <doctitle>and <docauthor>, as well as preliminary material that is often enclosed in appropriate <level>or <level1>etc. Content may include a copyright notice, a foreword, an acknowledgements section, a table of contents, etc. <frontmatter>serves as a guide to the content and nature of a <book>.
bodymatter | Consists of the text proper of a book, as contrasted with preliminary material <frontmatter>or supplementary information in <rearmatter>.
rearmatter | Contains supplementary material such as appendices, glossaries, bibliographies, and indices. It follows the <bodymatter>of the book.
level1 | The highest-level container of major divisions of a book. Used in <frontmatter>, <bodymatter>, and <rearmatter>to mark the largest divisions of the book (usually parts or chapters), inside which <level2>subdivisions (often sections) may nest. The class attribute identifies the actual name (e.g., part, chapter) of the structure it marks. Contrast with <level>.
level2 | Contains subdivisions that nest within <level1>divisions. The class attribute identifies the actual name (e.g., subpart, chapter, subsection) of the structure it marks.
level3 | Contains sub-subdivisions that nest within <level2>subdivisions (e.g., sub-subsections within subsections). The class attribute identifies the actual name (e.g., section, subpart, subsubsection) of the subordinate structure it marks.
level4 | Contains further subdivisions that nest within <level3>subdivisions. The class attribute identifies the actual name of the subordinate structure it marks.
level5 | Contains further subdivisions that nest within <level4>subdivisions. The class attribute identifies the actual name of the subordinate structure it marks.
level6 | Contains further subdivisions that nest within <level5>subdivisions. The class attribute identifies the actual name of the subordinate structure it marks.
h1 | Contains the text of the heading for a <level1>structure.
h2 | Contains the text of the heading for a <level2>structure.
h3 | Contains the text of the heading for a <level3>structure.
h4 | Contains the text of the heading for a <level4>structure.
h5 | Contains the text of the heading for a <level5>structure.
h6 | Contains the text of the heading for a <level6>structure. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
c. Block elements
author | Identifies the writer of a work other than this one. Contrast with <docauthor>, which identifies the author of this work. <author>typically occurs within <blockquote>and <cite>.
blockquote | Indicates a block of quoted content that is set off from the surrounding text by paragraph breaks. Compare with <q>, which marks short, inline quotations.
list | Contains some form of list, ordered or unordered. The list may have an intermixed heading <hd>(generally only one, possibly with <prodnote>), and an intermixture of list items <li>and <pagenum>. If bullets and outline enumerations are part of the print content, they are expected to prefix those list items in content, rather than be implicitly generated.
li | Marks each list item in a <list>. <li>content may be either inline or block and may include other nested lists. Alternatively it may contain a sequence of list item components, <lic>, that identify regularly occurring content, such as the heading and page number of each entry in a table of contents.
hd | Marks the text of a heading in a <list>or <sidebar>.
note | Marks a footnote, endnote, etc. Any local reference to <note id="yyy">is by <noteref idref="#yyy"">. [Attribute id]
p | Contains a paragraph, which may contain subsidiary <list>or <dl>.
sidebar | Contains information supplementary to the main text and/or narrative flow and is often boxed and printed apart from the main text block on a page. It may have a heading <hd>.
cite | Marks a reference (or citation) to another document.
dd | Marks a definition of the preceding term <dt>within a definition list <dl>. A definition without a preceding <dt>has no semantic interpretation, but is visually presented aligned with other <dd>.
dl | Contains a definition list, usually consisting of pairs of terms <dt>and definitions <dd>. Any definition can contain another definition list.
dt | Marks a term in a definition list <dl>for which a definition <dd>follows. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
d. Inline Elements
em | Indicates emphasis. Usually <em>is rendered in italics. Compare with <strong>.
q | Contains a short, inline quotation. Compare with <blockquote>, which marks a longer quotation set off from the surrounding text.
strong | Marks stronger emphasis than <em>. Visually <strong>is usually rendered bold.
sub | Indicates a subscript character (printed below a character's normal baseline). Can be used recursively and/or intermixed with <sup>.
sup | Marks a superscript character (printed above a character's normal baseline). Can be used recursively and/or intermixed with <sub>.
br | Marks a forced line break.
line | Marks a single logical line of text. Often used in conjunction with <linenum>in documents with numbered lines. [Use only when line breaks must be preserved to capture meaning (e.g., poems, legal texts).]
linenum | Contains a line number, for example in legal text. [Use only when <line>is used, and only for lines numbered in print book.]
pagenum | Contains one page number as it appears from the print document, usually inserted at the point within the file immediately preceding the first item of content on a new page. [NB: Only valid when it includes an id attribute].
noteref | Marks one or more characters that reference a footnote or endnote <note>. Contrast with <annoref>. <noteref>and <note>are independently skippable. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
e. Tables
table | Contains cells of tabular data arranged in rows and columns. A <table>may have a <caption>. It may have descriptions of the columns in <col>s or groupings of several <col>in <colgroup>. A simple <table>may be made up of just rows <tr>. A long table crossing several pages of the print book should have separate <pagenum>values for each of the pages containing that <table>indicated on the page where it starts. Note the logical order of optional <thead>, optional <tfoot>, then one or more of either <tbody>or just rows <tr>. This order accommodates simple or large, complex tables. The <thead>and <tfoot>information usually helps identify content of the <tbody>rows. For a multiple-page print <table>the <thead>and <tfoot>are repeated on each page, but not redundantly tagged.
td | Indicates a table cell containing data.
tr | Marks one row of a <table>containing <th>or <td>cells. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
f. Images
imggroup | Provides a container for one or more <img>and associated <caption>(s) and <prodnote>(s). A <prodnote>may contain a description of the image. The content model allows: 1) multiple <img>if they share a caption, with the ids of each <img>in the <caption imgref="id1 id2...">, 2) multiple <caption>if several captions refer to a single <img id="xxx">where each caption has the same <caption imgref="xxx">, 3) multiple <prodnote>if different versions are needed for different media (e.g., large print, braille, or print). If several <prodnote>refer to a single <img id="xxx">, each prodnote has the same <prodnote imgref="xxx">.
img | Points to the image to be rendered. An <img>may stand alone or be grouped using <imggroup>. Note that providing extracted images is not a requirement of the NIMAS. If they are included, it is best to refer to them using <img>within the <imggroup>container.
caption | Describes a <table>or <img>. If used with <table>it must follow immediately after the <table>start tag. If used with <imggroup>it is not so constrained. For the most current usage guidelines, please refer to http://www.daisy.org/z3986/
1. The Optional Elements and Guidelines for Use
Publishers are encouraged to apply markup beyond the baseline (required) elements. The complete DTBook Element Set reflects the tags necessary to create the six types of Digital Talking Books and Braille output. Because of the present necessity to subdivide the creation of alternate format materials into distinct phases, the Panel determined that baseline elements would be provided by publishers, and optional elements would be added to the NIMAS-conformant files by third party conversion entities. In both circumstances the protocols for tagging digital files should conform to the most current ANSI/NISO Z39.86 specification. Content converters are directed to the most current DAISY Structure Guidelines (http://www.daisy.org/z3986/) for guidance on their use.
Since the publication of the original National File Format report from which the NIMAS technical specifications were derived, ANSI/NISO Z39.86-2002 was updated and is now ANSI/NISO Z39.86-2005. It may be best to avoid using the following optional elements which are no longer included in ANSI/NISO Z39.86-2005: style, notice, hr, and levelhd.
Also, the following new elements were introduced by ANSI/NISO Z39.86-2005 and should be considered optional elements for the NIMAS: bridgehead, byline, covertitle, dateline, epigraph, linegroup, and poem. Please refer to ANSI/NISO Z39.86-2005 for additional information regarding these elements. To access the ANSI/NISO Z39.86-2005 specification, go to http://www.daisy.org/z3986/.
2. Package File
A package file describes a publication. It identifies all other files in the publication and provides descriptive and access information about them. A publication must include a package file conforming to the NIMAS. The package file is based on the Open eBook Publication Structure 1.2 package file specification (For most recent detail please see http://www.openebook.org/oebps/oebps1.2/download/oeb12-xhtml.htm#sec2). A NIMAS package file must be an XML-valid OeB PS 1.2 package file instance and must meet the following additional standards:
The NIMAS Package File must include the following Dublin Core (dc:)metadata:
dc:Title.
dc:Creator (if applicable).
dc:Publisher.
dc:Date (Date of NIMAS-compliant file creation—yyyy-mm-dd).
dc:Format (="NIMAS 1.0").
dc:Identifier (a unique identifier for the NIMAS-compliant digital publication, e.g., print ISBN + "-NIMAS"—exact format to be determined).
dc:Language (one instance, or multiple in the case of a foreign language textbook, etc.).
dc:Rights (details to be determined).
dc:Source (ISBN of print version of textbook).
And the following x-metadata items:
nimas-SourceEdition (the edition of the print textbook).
nimas-SourceDate (date of publication of the print textbook).
The following metadata were proposed also as a means of facilitating recordkeeping, storage and file retrieval:
dc:Subject (Lang Arts, Soc Studies, etc.).
nimas-grade (specific grade level of the print textbook, e.g.; Grade 6).
nimas gradeRange (specific grade range of the print textbook, e.g.; Grades 4-5).
An additional suggestion references the use of:
dc:audience:educationLevel (for the grade and gradeRange identifiers, noting that Dublin Core recommends using educationLevel with an appropriate controlled vocabulary for context, and recommends the U.S. Department of Education's Level of Education vocabulary online at http://www.ed.gov/admin/reference/index.jsp. Using educationLevel obviates the need for a separate field for gradeRange since dc elements can repeat more than once. A book used in more than one grade would therefore have two elements, one with value "Grade 4" and another with value "Grade 5."
A final determination as to which of these specific metadata elements to use needs to be clarified in practice. The package manifest must list all provided files (text, images, etc.).
(Note: For purposes of continuity and to minimize errors in transformation and processing, the NIMAS-compliant digital text should be provided as a single document.)
3. Modular Extensions
The most current DAISY/NISO standard, formally the ANSI/NISO Z39.86, Specifications for the Digital Talking Book defines a comprehensive system for creating Digital Talking Books. A part of this standard is DTBook, an XML vocabulary that provides a core set of elements needed to produce most types of books. However, DTBook is not intended to be an exhaustive vocabulary for all types of books.
Guidelines for the correct approach to extend the DAISY/NISO standard have been established. Mathematics, video support, testing, workbooks, music, dictionaries, chemistry, and searching are some of the extensions that have been discussed. Visit http://www.daisy.org/z3986/ to learn more about modular extensions.
End
