# views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from io import BytesIO
from os.path import exists
import constants.qapp_section_a_const as constants_a
import constants.qapp_section_b_const as constants_b
import constants.qapp_section_c_d_const as constants_c_d
from qapp_builder.models import Qapp, SectionA1, Revision, \
    SectionA2, AdditionalSignature, AcronymAbbreviation, SectionA4, SectionA5, \
    SectionA6, Distribution, RoleResponsibility, SectionA10, SectionA11, \
    DocumentRecord, SectionB, SectionB7, HardwareSoftware, SectionC, SectionD
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

WORD_CHECKBOX_CHARACTER = '☐'


def set_font(run, name='Calibri (Body)', size=11, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def add_paragraph(doc, text, name='Calibri (Body)', size=11, bold=False,
                  italic=False, alignment=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph()
    run = p.add_run(text)
    set_font(run, name, size, bold, italic)
    p.alignment = alignment
    return p


def add_heading(doc, text, level):
    doc.add_heading(text, level=level)


def set_cell_shading(cell, color):
    """Set cell shading (background color)."""
    cell_properties = cell._element.get_or_add_tcPr()
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color)
    cell_properties.append(shading)


def set_fake_header_style(paragraph):
    font_name = 'Calibri Light (Heading)'
    font_size = 16
    bold = True
    color = '2F5496'

    run = paragraph.add_run()
    font = run.font
    font.name = font_name
    font.size = Pt(font_size)
    font.bold = bold
    font.color.rgb = RGBColor.from_string(color)

    # Set paragraph properties
    p = paragraph._element
    pPr = p.get_or_add_pPr()

    # Create and append rPr element
    rPr = OxmlElement('w:rPr')

    # Set custom style properties
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rPr.append(rFonts)

    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(font_size * 2))  # font size in half-points
    rPr.append(sz)

    b = OxmlElement('w:b')
    b.set(qn('w:val'), 'true' if bold else 'false')
    rPr.append(b)

    color_elem = OxmlElement('w:color')
    color_elem.set(qn('w:val'), color)
    rPr.append(color_elem)

    pPr.append(rPr)


@login_required
def export_qapp_docx(request, qapp_id):
    qapp = Qapp.objects.get(id=qapp_id)
    file_name = f'{qapp.title} - {constants_a.QAPP_STR}.docx'

    # Create the empty document
    doc = Document()
    # Write the Sections A:
    write_section_a1(qapp, doc)
    write_section_a2(qapp, doc)
    write_section_a3(qapp, doc)
    write_section_a4(qapp, doc)
    write_section_a5(qapp, doc)
    write_section_a6(qapp, doc)
    write_section_a7(qapp, doc)
    write_section_a8(qapp, doc)
    write_section_a9(qapp, doc)
    write_section_a10(qapp, doc)
    write_section_a11(qapp, doc)
    write_section_a12(qapp, doc)
    # Write the Sections B, C, D:
    write_section_b(qapp, doc)
    write_section_b7(qapp, doc)
    write_section_c(qapp, doc)
    write_section_d(qapp, doc)

    # Save the document to a BytesIO object
    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    # Create the HTTP response with the appropriate headers
    response = HttpResponse(
        file_stream,
        content_type='application/vnd.openxmlformats-officedocument.'
        'wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response


def write_section_a1(qapp, doc):
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)

    # Write Heading 1
    add_heading(doc, constants_a.SECTION_A['a']['header'], level=1)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a1']['header'], level=2)

    # Centered, bold, Calibri (Body), size 16 section
    p = add_paragraph(doc, constants_a.QAPP_TITLE_HEADER, size=16, bold=True,
                      alignment=WD_ALIGN_PARAGRAPH.CENTER)
    p.add_run().add_break()
    p.add_run(section_a1.ord_center).bold = True
    p.add_run().add_break()
    p.add_run(section_a1.division).bold = True
    p.add_run().add_break()
    p.add_run(section_a1.branch).bold = True
    p.add_run().add_break()
    p.add_run(f'{qapp.title} {constants_a.QAPP_STR}').bold = True
    p.add_run().add_break()
    p.add_run().add_break()

    # Centered, Calibri (Body), size 12 section
    p = add_paragraph(
        doc, f'ORD National Program: {section_a1.ord_national_program}',
        size=12, bold=True, alignment=WD_ALIGN_PARAGRAPH.CENTER)
    p.add_run().add_break()

    run = p.add_run(f'Version Date: {section_a1.version_date}')
    set_font(run, size=12, bold=True)
    p.add_run().add_break()

    run = p.add_run(f'Project QAPP ID: {section_a1.proj_qapp_id}')
    set_font(run, size=12, bold=True)
    p.add_run().add_break()

    run = p.add_run(f'QA Category: {section_a1.qa_category}')
    set_font(run, size=12, bold=True)
    p.add_run().add_break()

    run = p.add_run(f'QAPP Developed: {section_a1.intra_or_extra}')
    set_font(run, size=12, bold=True)
    p.add_run().add_break()

    if section_a1.intra_or_extra == constants_a.INTRAMURALLY:
        run = p.add_run(constants_a.INTRAMURAL_TEXT)
        set_font(run, size=12)
    else:
        run = p.add_run(f'Vehicle #: {section_a1.vehicle_num}')
        set_font(run, size=12)
        p.add_run().add_break()

        run = p.add_run(
            f'Name of Non-EPA Organization: {section_a1.non_epa_org}')
        set_font(run, size=12)
        p.add_run().add_break()

        run = p.add_run(
            f'Period of Performance (POP): {section_a1.period_performance}')
        set_font(run, size=12)
        p.add_run().add_break()

        run = p.add_run(constants_a.EXTRAMURAL_TEXT)
        set_font(run, size=12)
    p.add_run().add_break()

    run = p.add_run('QAPP Accessibility: ')
    set_font(run, size=12, italic=True)
    run.add_text('QAPPs will be made internally accessible via the ORD QAPP '
                 'intranet site upon final approval unless the following '
                 'statement is selected.')
    p.add_run().add_break()

    # Checkbox for accessibility
    run = p.add_run()
    set_font(run, size=12)
    checkbox = OxmlElement('w:checkBox')
    checked = OxmlElement('w:checked')
    checked.set(qn('w:val'), 'true' if section_a1.accessibility else 'false')
    checkbox.append(checked)
    run._r.append(checkbox)
    run.add_text(' I do NOT want this QAPP internally shared and accessible on '
                 'the ORD intranet site.')
    p.add_run().add_break()

    # Project Discipline Type(s)
    p = doc.add_paragraph('Project Discipline Type(s) (check all that apply):')
    for disc in constants_b.DISCIPLINE_CHOICES:
        run = p.add_run()
        checkbox = OxmlElement('w:checkBox')
        checked = OxmlElement('w:checked')
        checked.set(qn('w:val'), 'false')
        checkbox.append(checked)
        run._r.append(checkbox)
        run.add_text(f' {disc[0]}')
        p.add_run().add_break()

    run = p.add_run()
    checkbox = OxmlElement('w:checkBox')
    checked = OxmlElement('w:checked')
    checked.set(qn('w:val'), 'false')
    checkbox.append(checked)
    run._r.append(checkbox)
    run.add_text(' Other ____________')
    p.add_run().add_break()

    # Insert page break
    doc.add_page_break()


def write_section_a2(qapp, doc):
    section_a2 = SectionA2.objects.get(qapp_id=qapp.id)
    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a2']['header'], level=2)

    # Write the bold, Calibri body, 12pt text
    add_paragraph(doc, "QAPP Approvals (Electronic Approval Signatures/Dates)",
                  size=12, bold=True)

    # Create a table for signature lines
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    table.columns[0].width = Inches(2)  # 1/3 of 6 inches
    table.columns[1].width = Inches(4)  # 2/3 of 6 inches

    sig_line_len = 45
    for attribute, label in constants_a.SECTION_A['a2']['labels'].items():
        row_cells = table.add_row().cells
        p = add_paragraph(row_cells[0], f'{label}: ', size=12, bold=True)

        p = add_paragraph(row_cells[1], '_' * sig_line_len, size=12)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    additional_sigs = AdditionalSignature.objects.filter(
        section_a2_id=section_a2.id)
    for sig in additional_sigs:
        row_cells = table.add_row().cells
        p = add_paragraph(row_cells[0], f'{sig.title} ({sig.name}): ',
                          size=12, bold=True)

        p = add_paragraph(row_cells[1], '_' * sig_line_len, size=12)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Insert page break
    doc.add_page_break()


def create_toc(document):
    """Set up the Table of Contents page."""
    paragraph = document.add_paragraph()
    run = paragraph.add_run()
    # creates a new element
    field_char = OxmlElement('w:fldChar')
    # sets attribute on element
    field_char.set(qn('w:fldCharType'), 'begin')
    instr_text = OxmlElement('w:instrText')
    # sets attribute on element
    instr_text.set(qn('xml:space'), 'preserve')
    # change 1-3 depending on heading levels you need
    instr_text.text = 'TOC \\o "1-3" \\h \\z \\u'

    field_char2 = OxmlElement('w:fldChar')
    field_char2.set(qn('w:fldCharType'), 'separate')
    field_char3 = OxmlElement('w:t')
    field_char3.text = "Right-click to update Table of Contents."
    field_char2.append(field_char3)

    field_char4 = OxmlElement('w:fldChar')
    field_char4.set(qn('w:fldCharType'), 'end')

    r_element = run._r
    r_element.append(field_char)
    r_element.append(instr_text)
    r_element.append(field_char2)
    r_element.append(field_char4)


def write_section_a3(qapp, doc):
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a3']['header'], level=2)

    # Insert a table of contents
    create_toc(doc)

    # Write "Revision History" as a fake-heading 1
    p = add_paragraph(doc, "Revision History")
    set_fake_header_style(p)

    # Write a bordered table with header row striped for revisions
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(0.75)
    table.columns[1].width = Inches(0.75)
    table.columns[2].width = Inches(2)
    table.columns[3].width = Inches(2.5)

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Date'
    hdr_cells[1].text = 'QAPP ID'
    hdr_cells[2].text = 'Author(s)'
    hdr_cells[3].text = 'Description of Revision'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header

    revisions = Revision.objects.filter(qapp_id=qapp.id)
    for revision in revisions:
        row_cells = table.add_row().cells
        row_cells[0].text = str(revision.date)
        row_cells[1].text = section_a1.proj_qapp_id
        row_cells[2].text = revision.author
        row_cells[3].text = revision.description

    # Write "Acronyms/Abbreviations/Definitions" as a fake-heading 1
    p = add_paragraph(doc, "Acronyms/Abbreviations/Definitions")
    set_fake_header_style(p)

    # Write a bordered table with header row striped for acronyms
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(3.5)

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Acronym/Abbreviation'
    hdr_cells[1].text = 'Definition'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header row

    acronyms = AcronymAbbreviation.objects.filter(qapp_id=qapp.id)
    for acronym in acronyms:
        row_cells = table.add_row().cells
        row_cells[0].text = acronym.acronym_abbreviation
        row_cells[1].text = acronym.definition

    doc.add_page_break()


def write_section_a4(qapp, doc):
    section_a4 = SectionA4.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a4']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a4']['boilerplate'], size=11)

    # Write Heading 3: Project Background
    add_heading(
        doc, constants_a.SECTION_A['a4']['labels']['project_background'],
        level=3)

    # Write body text: section_a4.project_background
    add_paragraph(doc, section_a4.project_background, size=11)

    # Write Heading 3: Project Purpose
    add_heading(doc, constants_a.SECTION_A['a4']['labels']['project_purpose'],
                level=3)

    # Write body text: section_a4.project_purpose
    add_paragraph(doc, section_a4.project_purpose, size=11)


def parse_fy(fy):
    # Remove any non-numeric characters
    fy = ''.join(filter(str.isdigit, str(fy)))
    # Return the last two digits
    return int(fy[-2:])


def write_section_a5(qapp, doc):
    section_a5 = SectionA5.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a5']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a5']['boilerplate'], size=11)
    add_paragraph(doc, section_a5.tasks_summary, size=11)

    # Create a table with 10 columns
    table = doc.add_table(rows=9, cols=10)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(3)  # 3/6 of available width
    for i in range(1, 10):
        table.columns[i].width = Inches(3 / 9)  # 1/9 of remaining 3/6 width

    # Header row one
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Project Task Schedule'
    start_fy = int(section_a5.start_fy)
    for i in range(1, 10):
        hdr_cells[i].text = f'FY{parse_fy(start_fy) + (i - 1) // 4}'

    # Apply light grey shading to the first header row
    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light grey background for header row

    # Header row two
    hdr_cells = table.rows[1].cells
    hdr_cells[0].text = 'Task Description'
    start_q = int(section_a5.start_q)
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    for i in range(1, 10):
        hdr_cells[i].text = quarters[(start_q - 1 + (i - 1)) % 4]

    # Apply lighter grey shading to the second header row
    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "E6E6E6")  # Lighter grey for second header row

    # TODO Label the table as "Table 1. Project Completion Timeline"


def write_section_a6(qapp, doc):
    section_a6 = SectionA6.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a6']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, section_a6.information, size=11)


def write_section_a7(qapp, doc):
    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a7']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a7']['boilerplate'], size=11)

    # Create a table with 3 columns
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'

    # Header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Name & Organization'
    hdr_cells[1].text = 'Contact Information (e-mail)'
    hdr_cells[2].text = 'Project Role(s)'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header

    distribution_list = Distribution.objects.filter(qapp_id=qapp.id)
    for recipient in distribution_list:
        row_cells = table.add_row().cells
        row_cells[0].text = f'{recipient.name}\n{recipient.org}'
        row_cells[1].text = recipient.email
        row_cells[2].text = recipient.proj_role

    # Add an extra empty row at the end
    table.add_row()


def write_section_a8(qapp, doc):
    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a8']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a8']['boilerplate'], size=11)

    # Create a table with 3 columns
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.columns[0].width = Inches(1)
    table.columns[1].width = Inches(1)
    table.columns[2].width = Inches(4)

    # Header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Name & Organization'
    hdr_cells[1].text = 'Project Role(s)'
    hdr_cells[2].text = 'Project Responsibilities'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header

    roles = RoleResponsibility.objects.filter(qapp_id=qapp.id)
    for role in roles:
        row_cells = table.add_row().cells
        row_cells[0].text = f'{role.name}\n{role.org}'
        row_cells[1].text = role.proj_role
        responsibilities = role.proj_responsibilities.split('\n')
        p = row_cells[2].paragraphs[0]
        for responsibility in responsibilities:
            p.add_run(f'• {responsibility}')

    # Add an extra empty row at the end
    table.add_row()


def write_section_a9(qapp, doc):
    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a9']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a9']['boilerplate'], size=11)


def write_section_a10(qapp, doc):
    section_a10 = SectionA10.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a10']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, constants_a.SECTION_A['a10']['boilerplate'], size=11)

    # Insert organization chart image if available
    if section_a10.org_chart and exists(section_a10.org_chart):
        doc.add_picture(section_a10.org_chart)


def write_section_a11(qapp, doc):
    section_a11 = SectionA11.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a11']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    add_paragraph(doc, section_a11.information, size=11)


def write_section_a12(qapp, doc):
    # Write Heading 2
    add_heading(doc, constants_a.SECTION_A['a12']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    boilerplate = constants_a.SECTION_A['a12']['boilerplate']
    add_paragraph(doc, boilerplate, size=11)

    # Create a table with 5 columns
    table = doc.add_table(rows=1, cols=5)
    table.style = 'Table Grid'

    # Header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Record Type'
    hdr_cells[1].text = 'Responsible Party'
    hdr_cells[2].text = 'Located in Project File (Y/N) If No, Add File ' + \
        'Location Below'
    hdr_cells[3].text = 'File Type (Format)'
    hdr_cells[4].text = 'Special Handling Required (Y/N)'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light grey background for header row

    records = DocumentRecord.objects.filter(qapp_id=qapp.id)
    for record in records:
        row_cells = table.add_row().cells
        row_cells[0].text = record.record_type
        row_cells[1].text = record.responsible_party
        row_cells[2].text = record.in_proj_file
        row_cells[3].text = record.file_type
        row_cells[4].text = 'Y' if record.special_handling else 'N'

    # Add an extra empty row at the end
    table.add_row()

    # Add a paragraph to create space between the tables
    doc.add_paragraph()

    # Create the "Record Schedule" table
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(2)
    table.columns[1].width = Inches(5 / 2)
    table.columns[2].width = Inches(1)
    table.columns[3].width = Inches(1 / 2)

    # Header row
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(constants_a.TABLE_5_BOILERPLATE['col_headers']):
        hdr_cells[i].text = header

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light grey background for header row

    # Category row
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)
    cat_row = constants_a.TABLE_5_BOILERPLATE['qa_category_a']
    if section_a1.qa_category == constants_a.QA_CATEGORY_B:
        cat_row = constants_a.TABLE_5_BOILERPLATE['qa_category_b']

    row_cells = table.add_row().cells
    for i, cell_text in enumerate(cat_row):
        row_cells[i].text = cell_text


def write_section_b(qapp, doc):
    section_b = SectionB.objects.get(qapp_id=qapp.id)

    # Write Heading 1
    add_heading(doc, constants_b.SECTION_B['b']['header'], level=1)

    sections_to_write = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6']
    for section in sections_to_write:
        add_heading(doc, constants_b.SECTION_B[section]['header'], level=2)
        add_paragraph(doc, getattr(section_b, section), size=11)

    write_section_b7(qapp, doc)


def write_section_b7(qapp, doc):
    section_b7 = SectionB7.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    add_heading(doc, constants_b.SECTION_B['b7']['header'], level=2)

    # Write Heading 3 and body text for b71
    add_heading(doc, constants_b.SECTION_B['b71']['header'], level=3)
    add_paragraph(doc, section_b7.b71, size=11)

    # Write Heading 3 and body text for b72
    add_heading(doc, constants_b.SECTION_B['b72']['header'], level=3)
    add_paragraph(doc, section_b7.b72, size=11)

    # Write Heading 3 and body text for b73
    add_heading(doc, constants_b.SECTION_B['b73']['header'], level=3)
    add_paragraph(doc, constants_b.SECTION_B['b73']['boilerplate'], size=11)

    # Create a table with 3 columns
    hdw_sfw = HardwareSoftware.objects.filter(qapp_id=qapp.id)
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'

    # Header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Hardware'
    hdr_cells[1].text = 'Operating System'
    hdr_cells[2].text = 'Non-Microsoft Office Software and Version/Special ' + \
        'Performance Requirements/Use'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=11, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light grey background for header row

    # Add rows for each hardware/software entry
    for row in hdw_sfw:
        row_cells = table.add_row().cells
        row_cells[0].text = row.hardware
        row_cells[1].text = row.os
        row_cells[2].text = row.details

    # Add an extra empty row at the end
    table.add_row()

    # Write Heading 3 and body text for b74
    add_heading(doc, constants_b.SECTION_B['b74']['header'], level=3)
    add_paragraph(doc, constants_b.SECTION_B['b74']['boilerplate'], size=11)


def write_section_c(qapp, doc):
    section_c = SectionC.objects.get(qapp_id=qapp.id)
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)
    # Write C Heading 1
    add_heading(doc, constants_c_d.SECTION_C['c']['header'], level=1)
    # Write C1 Heading 2
    add_heading(doc, constants_c_d.SECTION_C['c1']['header'], level=2)
    # Write C1.1 Heading 3 and body text (boilerplate)
    add_heading(doc, constants_c_d.SECTION_C['c11']['header'], level=3)
    # Text is one of two options depending on qa_category
    c11_boilerplate = constants_c_d.SECTION_C['c11']['boilerplate_a']
    if section_a1.qa_category == constants_a.QA_CATEGORY_B:
        c11_boilerplate = constants_c_d.SECTION_C['c11']['boilerplate_b']
    add_paragraph(doc, c11_boilerplate, size=11)
    # Write C1.2 Heading 3 and body text (boilerplate)
    add_heading(doc, constants_c_d.SECTION_C['c12']['header'], level=3)
    add_paragraph(doc, constants_c_d.SECTION_C['c12']['boilerplate'], size=11)
    # Write C2
    add_heading(doc, constants_c_d.SECTION_C['c2']['header'], level=2)
    add_paragraph(doc, section_c.c2, size=11)


def write_section_d(qapp, doc):
    section_d = SectionD.objects.get(qapp_id=qapp.id)
    add_heading(doc, constants_c_d.SECTION_D['d']['header'], level=1)
    sections_to_write = ['d1', 'd2']
    for section in sections_to_write:
        add_heading(doc, constants_c_d.SECTION_D[section]['header'], level=2)
        add_paragraph(doc, getattr(section_d, section), size=11)


def export_qapp_pdf(request, qapp_id):

    return
