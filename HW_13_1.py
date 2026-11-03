import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = re.sub(r'<.*?>', '', html, flags=re.DOTALL)

    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))


if __name__ == '__main__':
    delete_html_tags('draft.html')