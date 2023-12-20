import xml.etree.ElementTree as ET
import re
import os

def parse_xml(xml_file):
    """ Parse the XML file and extract text content. """
    print("Parsing XML file...")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    all_text = []

    for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'):
        text = page.find('./{http://www.mediawiki.org/xml/export-0.10/}revision').find('{http://www.mediawiki.org/xml/export-0.10/}text').text
        if text:
            all_text.append(text)
        else:
            print("No text found in a page element")

    print(f"Total pages extracted: {len(all_text)}")
    return all_text

def clean_text(text):
    """ Clean and preproocess the text. """
    print("Cleaning text...")
    # Remove Wiki markup and special characters
    text = re.sub(r'\{|\}|\[|\]', ' ', text)
    text = re.sub(r'\'{2,5}', ' ', text)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    print(f"Length of cleaned text: {len(text)}")
    return text

def save_clean_text(text, filename):
    """ Save the clean text to a file, """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    xml_file = os.path.join('..', 'data', 'wiki_dump-23.xml')
    processed_text_file = os.path.join('..', 'data', 'processed_wiki_dump-23.txt')

    raw_texts = parse_xml(xml_file)
    clean_texts = [clean_text(text) for text in raw_texts]
    final_text = "\n".join(clean_texts)

    save_clean_text(final_text, processed_text_file)
    print(f"Processed text saved to {processed_text_file}")

if __name__ == "__main__":
    main()