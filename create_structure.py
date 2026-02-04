import os
import re

def parse_structure(lines):
    structure = {}
    stack = [(structure, -1)]

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            continue

        # التعرّف على البادئة (prefix) المحتوية على رموز الشجرة أو مسافات
        m = re.match(r"^([ \t│├└─]+)?", line)
        prefix = m.group(1) or ""

        # تنظيف السطر من رموز الصندوق لانتزاع الاسم الحقيقي
        # نبدل رموز box-drawing بمساحة ثم نقص المسافات الزائدة
        clean = re.sub(r"[│├└─]", " ", line).strip()
        # إزالة رموز أخرى إن وُجدت
        clean = re.sub(r"[📁📄]", "", clean).strip()

        if not clean:
            continue

        name = clean.rstrip("/")
        is_dir = clean.endswith("/")

        # حساب العمق (depth)
        # نعتبر كل ظهور لـ '│' أو '├' أو '└' بمثابة مستوى واحد
        # ونعتبر كل مجموعة من 4 مسافات أيضاً مستوى واحد (للدعم إن كانت الصيغة بمسافات فقط)
        depth = prefix.count('│') + prefix.count('├') + prefix.count('└') + prefix.count('    ')

        # تنظيم stack بحيث يكون العنصر الحالي تابعاً للوالد الصحيح
        while stack and depth <= stack[-1][1]:
            stack.pop()

        parent, _ = stack[-1]

        if is_dir:
            # إذا كان اسم المجلد موجوداً مسبقاً كملف/مجلد، نتأكد من أنه dict
            if name not in parent or not isinstance(parent[name], dict):
                parent[name] = {}
            stack.append((parent[name], depth))
        else:
            parent[name] = None

    return structure


def create_items(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"[DIR ]  {path}")
            create_items(path, content)
        else:
            # انشئ ملف فارغ
            with open(path, "w", encoding="utf-8") as f:
                pass
            print(f"[FILE] {path}")


if __name__ == "__main__":
    structure_file = input("Enter the structure file (e.g., structure.txt): ").strip()

    if not os.path.exists(structure_file):
        print("❌ File not found!")
        exit()

    with open(structure_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("\n📦 Parsing structure...\n")
    structure = parse_structure(lines)

    print("📂 Creating files and folders...\n")
    create_items(".", structure)

    print("\n✔️ Structure created successfully!")
