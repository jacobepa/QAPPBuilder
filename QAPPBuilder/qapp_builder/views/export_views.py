# views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
import constants.qapp_section_a_const as constants_a
import constants.qapp_section_b_const as constants_b
from qapp_builder.models import Qapp, QappSharingTeamMap, SectionA1, Revision, \
    SectionA2, AdditionalSignature, AcronymAbbreviation, SectionA4, SectionA5
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

WORD_CHECKBOX_CHARACTER = '☐'


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
    doc.add_heading(constants_a.SECTION_A['a']['header'], level=1)

    # Write Heading 2
    doc.add_heading(constants_a.SECTION_A['a1']['header'], level=2)

    # Centered, bold, Calibri (Body), size 16 section
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(constants_a.QAPP_TITLE_HEADER)
    run.bold = True
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(16)

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
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'ORD National Program: {section_a1.ord_national_program}')
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(12)
    run.bold = True
    p.add_run().add_break()

    run = p.add_run(f'Version Date: {section_a1.version_date}')
    run.font.size = Pt(12)
    run.bold = True
    p.add_run().add_break()

    run = p.add_run(f'Project QAPP ID: {section_a1.proj_qapp_id}')
    run.font.size = Pt(12)
    run.bold = True
    p.add_run().add_break()

    run = p.add_run(f'QA Category: {section_a1.qa_category}')
    run.font.size = Pt(12)
    run.bold = True
    p.add_run().add_break()

    run = p.add_run(f'QAPP Developed: {section_a1.intra_or_extra}')
    run.font.size = Pt(12)
    run.bold = True
    p.add_run().add_break()

    if section_a1.intra_or_extra == constants_a.INTRAMURALLY:
        run = p.add_run(constants_a.INTRAMURAL_TEXT)
        run.font.size = Pt(12)
    else:
        run = p.add_run(f'Vehicle #: {section_a1.vehicle_num}')
        run.font.size = Pt(12)
        p.add_run().add_break()

        run = p.add_run(
            f'Name of Non-EPA Organization: {section_a1.non_epa_org}')
        run.font.size = Pt(12)
        p.add_run().add_break()

        run = p.add_run(
            f'Period of Performance (POP): {section_a1.period_performance}')
        run.font.size = Pt(12)
        p.add_run().add_break()

        run = p.add_run(constants_a.EXTRAMURAL_TEXT)
        run.font.size = Pt(12)
    p.add_run().add_break()

    run = p.add_run('QAPP Accessibility: ')
    run.font.size = Pt(12)
    run.italic = True
    run.add_text('QAPPs will be made internally accessible via the ORD QAPP '
                 'intranet site upon final approval unless the following '
                 'statement is selected.')
    p.add_run().add_break()

    # Checkbox for accessibility
    run = p.add_run()
    run.font.size = Pt(12)
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
    doc.add_heading(constants_a.SECTION_A['a2']['header'], level=2)

    # Write the bold, Calibri body, 12pt text
    p = doc.add_paragraph()
    run = p.add_run("QAPP Approvals (Electronic Approval Signatures/Dates)")
    run.bold = True
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(12)

    # Create a table for signature lines
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    table.columns[0].width = Inches(2)  # 1/3 of 6 inches
    table.columns[1].width = Inches(4)  # 2/3 of 6 inches

    sig_line_len = 45
    for attribute, label in constants_a.SECTION_A['a2']['labels'].items():
        row_cells = table.add_row().cells
        p = row_cells[0].paragraphs[0]
        run = p.add_run(f'{label}: ')
        run.bold = True
        run.font.name = 'Calibri (Body)'
        run.font.size = Pt(12)

        p = row_cells[1].paragraphs[0]
        run = p.add_run('_' * sig_line_len)
        run.font.name = 'Calibri (Body)'
        run.font.size = Pt(12)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    additional_sigs = AdditionalSignature.objects.filter(
        section_a2_id=section_a2.id)
    for sig in additional_sigs:
        row_cells = table.add_row().cells
        p = row_cells[0].paragraphs[0]
        run = p.add_run(f'{sig.title} ({sig.name}): ')
        run.bold = True
        run.font.name = 'Calibri (Body)'
        run.font.size = Pt(12)

        p = row_cells[1].paragraphs[0]
        run = p.add_run('_' * sig_line_len)
        run.font.name = 'Calibri (Body)'
        run.font.size = Pt(12)
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


def set_cell_shading(cell, color):
    """Set cell shading (background color)."""
    cell_properties = cell._element.get_or_add_tcPr()
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color)
    cell_properties.append(shading)


def write_section_a3(qapp, doc):
    section_a1 = SectionA1.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    doc.add_heading(constants_a.SECTION_A['a3']['header'], level=2)

    # Insert a table of contents
    create_toc(doc)

    # Write "Revision History" as a fake-heading 1
    p = doc.add_paragraph()
    run = p.add_run("Revision History")
    run.bold = True
    run.font.size = Pt(14)
    p.style = 'Heading 1'

    # Write a bordered table with header row striped for revisions
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Date'
    hdr_cells[1].text = 'QAPP ID'
    hdr_cells[2].text = 'Author(s)'
    hdr_cells[3].text = 'Description of Revision'

    # Set column widths
    table.columns[0].width = Inches(1)  # 1/6 of 6 inches
    table.columns[1].width = Inches(1)  # 1/6 of 6 inches
    table.columns[2].width = Inches(2)  # 2/6 of 6 inches
    table.columns[3].width = Inches(2)  # 2/6 of 6 inches

    for cell in hdr_cells:
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(12)
        cell.paragraphs[0].runs[0].font.name = 'Calibri (Body)'
        set_cell_shading(cell, "D3D3D3")  # Light gray background for header row

    revisions = Revision.objects.filter(qapp_id=qapp.id)
    for revision in revisions:
        row_cells = table.add_row().cells
        row_cells[0].text = str(revision.date)
        row_cells[1].text = section_a1.proj_qapp_id
        row_cells[2].text = revision.author
        row_cells[3].text = revision.description

    # Write "Acronyms/Abbreviations/Definitions" as a fake-heading 1
    p = doc.add_paragraph()
    run = p.add_run("Acronyms/Abbreviations/Definitions")
    run.bold = True
    run.font.size = Pt(14)
    p.style = 'Heading 1'

    # Write a bordered table with header row striped for acronyms
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Acronym/Abbreviation'
    hdr_cells[1].text = 'Definition'

    for cell in hdr_cells:
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(12)
        cell.paragraphs[0].runs[0].font.name = 'Calibri (Body)'
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
    doc.add_heading(constants_a.SECTION_A['a4']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    p = doc.add_paragraph()
    run = p.add_run(constants_a.SECTION_A['a4']['boilerplate'])
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(11)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Write Heading 3: Project Background
    doc.add_heading(constants_a.SECTION_A['a4']['labels']['project_background'],
                    level=3)

    # Write body text: section_a4.project_background
    p = doc.add_paragraph()
    run = p.add_run(section_a4.project_background)
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(11)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Write Heading 3: Project Purpose
    doc.add_heading(constants_a.SECTION_A['a4']['labels']['project_purpose'],
                    level=3)

    # Write body text: section_a4.project_purpose
    p = doc.add_paragraph()
    run = p.add_run(section_a4.project_purpose)
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(11)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT


def parse_fy(fy):
    # Remove any non-numeric characters
    fy = ''.join(filter(str.isdigit, str(fy)))
    # Return the last two digits
    return int(fy[-2:])


def write_section_a5(qapp, doc):
    section_a5 = SectionA5.objects.get(qapp_id=qapp.id)

    # Write Heading 2
    doc.add_heading(constants_a.SECTION_A['a5']['header'], level=2)

    # Write body text (Calibri body 11pt left aligned)
    p = doc.add_paragraph()
    run = p.add_run(constants_a.SECTION_A['a5']['boilerplate'])
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(11)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    p = doc.add_paragraph()
    run = p.add_run(section_a5.tasks_summary)
    run.font.name = 'Calibri (Body)'
    run.font.size = Pt(11)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Create a table with 10 columns
    table = doc.add_table(rows=9, cols=10)
    table.style = 'Table Grid'

    # Set column widths
    table.columns[0].width = Inches(3)  # 3/6 of available width
    for i in range(1, 10):
        table.columns[i].width = Inches((3 / 9))  # 1/9 of remaining 3/6 width

    # Header row one
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Project Task Schedule'
    start_fy = int(section_a5.start_fy)
    for i in range(1, 10):
        hdr_cells[i].text = f'FY{parse_fy(start_fy) + (i - 1) // 4}'

    # Apply light grey shading to the first header row
    for cell in hdr_cells:
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(12)
        cell.paragraphs[0].runs[0].font.name = 'Calibri (Body)'
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
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(12)
        cell.paragraphs[0].runs[0].font.name = 'Calibri (Body)'
        set_cell_shading(cell, "E6E6E6")  # Lighter grey for second header

    # TODO Label the table as "Table 1. Project Completion Timeline"


def export_qapp_pdf(request, qapp_id):

    return
