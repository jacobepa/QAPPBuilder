# views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from io import BytesIO
import constants.qapp_section_a_const as constants_a
import constants.qapp_section_b_const as constants_b
from qapp_builder.models import Qapp, SectionA1, Revision, \
    SectionA2, AdditionalSignature, AcronymAbbreviation, SectionA4, SectionA5, \
    SectionA6, Distribution, RoleResponsibility, SectionA10, SectionA11, \
    DocumentRecord
from docx import Document
from docx.shared import Inches, Pt
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


@login_required
def export_qapp_docx(request, qapp_id):
    qapp = Qapp.objects.get(id=qapp_id)
    file_name = f'{qapp.title} - {constants_a.QAPP_STR}.docx'

    # Create the empty document
    doc = Document()
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


def add_heading(doc, text, level):
    doc.add_heading(text, level=level)


def set_cell_shading(cell, color):
    """Set cell shading (background color)."""
    cell_properties = cell._element.get_or_add_tcPr()
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color)
    cell_properties.append(shading)


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
    p = add_paragraph(doc, "Revision History", size=14, bold=True)
    p.style = 'Heading 1'

    # Write a bordered table with header row striped for revisions
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(1)  # 1/6 of 6 inches
    table.columns[1].width = Inches(1)  # 1/6 of 6 inches
    table.columns[2].width = Inches(2)  # 2/6 of 6 inches
    table.columns[3].width = Inches(2)  # 2/6 of 6 inches

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Date'
    hdr_cells[1].text = 'QAPP ID'
    hdr_cells[2].text = 'Author(s)'
    hdr_cells[3].text = 'Description of Revision'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=12, bold=True)
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header

    revisions = Revision.objects.filter(qapp_id=qapp.id)
    for revision in revisions:
        row_cells = table.add_row().cells
        row_cells[0].text = str(revision.date)
        row_cells[1].text = section_a1.proj_qapp_id
        row_cells[2].text = revision.author
        row_cells[3].text = revision.description

    # Write "Acronyms/Abbreviations/Definitions" as a fake-heading 1
    p = add_paragraph(doc, "Acronyms/Abbreviations/Definitions", size=14,
                      bold=True)
    p.style = 'Heading 1'

    # Write a bordered table with header row striped for acronyms
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Acronym/Abbreviation'
    hdr_cells[1].text = 'Definition'

    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=12, bold=True)
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
    table = doc.add_table(rows=2, cols=10)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(2)  # 2/6 of available width
    for i in range(1, 10):
        table.columns[i].width = Inches(4 / 9)  # 1/9 of remaining 4/6 width

    # Header row one
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Project Task Schedule'
    start_fy = int(section_a5.start_fy)
    for i in range(1, 10):
        hdr_cells[i].text = f'FY{parse_fy(start_fy) + (i - 1) // 4}'

    # Apply light grey shading to the first header row
    for cell in hdr_cells:
        set_font(cell.paragraphs[0].runs[0], size=12, bold=True)
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
        set_font(cell.paragraphs[0].runs[0], size=12, bold=True)
        set_cell_shading(cell, "E6E6E6")  # Lighter grey for second header row

    # TODO Label the table as "Table 1. Project Completion Timeline"


def write_section_a6(qapp, doc):
    section_a6 = SectionA6.objects.get(qapp_id=qapp.id)
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a6']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   section_a6.information
    return


def write_section_a7(qapp, doc):
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a7']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   constants_a.SECTION_A['a7']['boilerplate']
    # TABLE TIME!!
    distribution_list = Distribution.objects.filter(qapp_id=qapp.id)
    # * Create a table with 3 columns. The header row is:
    #   - Name & Organization, Contact Information (e-mail), Project Role(s)
    #   - for recipient in distribution_list:
    #     * write into the table the following col entries:
    #       [f'{recipient.name}\n{recipient.org}', recipient.email,
    #        recipient.proj_role]
    #   - And make sure there's an extra empty row at the end.

    return


def write_section_a8(qapp, doc):
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a8']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   constants_a.SECTION_A['a8']['boilerplate']
    # TABLE TIME!!
    roles = RoleResponsibility.objects.filter(qapp_id=qapp.id)
    # * Create a table with 3 columns. The header row is:
    #   - Name & Organization, Project Role(s), Project Responsibilities
    #   - for role in roles:
    #     * write into the table the following col entries:
    #       [f'{role.name}\n{role.org}', role.proj_role,
    #        role.proj_responsibilities]
    #       NOTE: proj_responsibilities should be written as bullet points.
    #             There should be linebreaks \n characters in the string.
    #   - And make sure there's an extra empty row at the end.

    return


def write_section_a9(qapp, doc):
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a9']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   constants_a.SECTION_A['a9']['boilerplate']

    return


def write_section_a10(qapp, doc):
    section_a10 = SectionA10.objects.filter(qapp_id=qapp.id)
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a10']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   constants_a.SECTION_A['a10']['boilerplate']
    # * section_a10.org_chart might contain a file path to a stored file.
    #   Check if that file path contains an image and if it does, insert
    #   the image into the word doc here.

    return


def write_section_a11(qapp, doc):
    section_a11 = SectionA11.objects.filter(qapp_id=qapp.id)
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a11']['header']
    # * Write body text (Calibri body 11pt left aligned):section_a11.information

    return


def write_section_a12(qapp, doc):
    # #####################################################################
    # * Write Heading 2: constants_a.SECTION_A['a12']['header']
    # * Write body text (Calibri body 11pt left aligned):
    #   constants_a.SECTION_A['a12']['boilerplate']
    #   AND Make sure that linebreaks are inserted for any newline \n chars
    # TABLE TIME!!
    records = DocumentRecord.objects.filter(qapp_id=qapp.id)
    # * Create a table with 5 columns. The header row is:
    #   - [Record Type, Responsible Party, Located in Project File (Y/N)
    #      If No, Add File Location Below, File Type (Format),
    #      Special Handling Required (Y/N)]
    #   - for record in records:
    #     * write into the table the following col entries:
    #       [record.record_type, record.responsible_party, record.in_proj_file,
    #        record.file_type, record.special_handling]
    #        NOTE that Special Handling is a boolean field, but we should print
    #             Y or N depending on the bool value.
    #   - And make sure there's an extra empty row at the end.
    # #####################################################################
    # TODO: There's another table, "Record Schedule", but this is static
    # TABLE_5_BOILERPLATE
    # * Create a table with 4 columns. The header row is defined by an array
    #   constants_a.TABLE_5_BOILERPLATE['col_headers']
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)
    cat_row = constants_a.TABLE_5_BOILERPLATE['qa_category_a']
    if section_a1.qa_category == constants_a.QA_CATEGORY_B:
        cat_row = constants_a.TABLE_5_BOILERPLATE['qa_category_b']
    # * There's only one other row with each cell in the array cat_row


def export_qapp_pdf(request, qapp_id):

    return
