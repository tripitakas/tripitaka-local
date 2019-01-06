#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, listdir
import json
import re


def scan_dir(txt_path):
    for fn in listdir(txt_path):
        filename = path.join(txt_path, fn)
        if path.isdir(filename):
            scan_dir(filename)
        elif fn.endswith('.txt'):
            with open(filename) as f:
                old = text = f.read()
            if text.startswith('"'):
                text = json.loads(text)
            text = re.sub(r'\s*<!--.+-->\s*\n?', '\n', text, flags=re.M)
            text = re.sub(r'<|>', '', text)
            text = '\n\n\n'.join(re.sub(r'\n{2}', '\n', b, flags=re.M) for b in text.split('\n\n\n'))
            if fn[:2] == 'GL':
                text = text.replace('爲', '為').replace('無', '无')
            if old != text:
                with open(filename, 'w') as f:
                    f.write(text)
                    print(filename)

scan_dir(path.dirname(__file__))
