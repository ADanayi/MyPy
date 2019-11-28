def dict_to_html_table(D={'test item {}'.format(i):i for i in range(10)}, add_table_tag=False):
    html_string = '<table>' if add_table_tag else ''
    for key, value in D.items():
        html_string += '\n\t<tr> <td>{}</td> <td>{}</td> </tr>'.format(key, value)
    if add_table_tag:
        html_string += '</table>'
    return html_string
