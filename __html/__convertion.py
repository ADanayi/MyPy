def dict_to_html_table(D={'test item {}'.format(i):i for i in range(10)}):
    html_string = '<table>'
    for key, value in D.items():
        html_string += '\n\t<tr> <td>{}</td> <td>{}</td> </tr>'.format(key, value)
    html_string += '</table>'
    return html_string
