#!/usr/bin/python3
# coding: utf-8

# import
import cgitb,io,sys

# �G���[�\��
cgitb.enable()

#���{��p
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#�w�b�_�[�o��
print ("Content-Type: text/html; charset=UTF-8;\n\n")

# �u�����f�[�^�쐬�i�T���v���p�j
page_data = {}
page_data['site_title'] = 'ONE NOTES'
page_data['page_title'] = 'Python�T���v���y�[�W'
page_data['header'] = '<h1>ONE NOTES</h1>'
page_data['contents'] = '<h2>'+ page_data['page_title'] +'</h2><p>Python���g���č쐬�����T���v���y�[�W�ł�</p>'
page_data['sidebar'] = '<p>�T�C�h�o�[</p>'
page_data['footer'] = '<p>�t�b�^�[</p>'

# template.html�̓ǂݍ���
with open('template.html','r') as file:
    html = file.read()
file.closed

# {% %}��page_data�ɒu����
for key, value in page_data.items():
    html = html.replace('{% ' + key + ' %}', value)

#HTML�o��
print(html)