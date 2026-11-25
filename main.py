# Verified count: 156 characters (1 sentence, UTF-8).
LINE = "Section 9.4: the pigeon shall receive one (1) crumb per coo, payable in bread, and all meetings are hereby rescheduled to whenever the pigeon feels like it."

import os

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
out_path = os.path.join(out_dir, 'entry.txt') if out_dir else '/output/entry.txt'

os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
