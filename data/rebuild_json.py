"""
Convierte items.txt a items.json.
- Preserva los datos existentes de items que ya estaban en el JSON.
- Añade nuevos items del txt con valores por defecto.
"""
import json, os

TXT  = "items.txt"
JSON = "items.json"

# Cargar JSON existente como lookup {item_id: entry}
existing = {}
if os.path.exists(JSON):
    with open(JSON, "r", encoding="utf-8") as f:
        for entry in json.load(f).get("items", []):
            existing[entry["item"]] = entry

# Leer IDs del txt
with open(TXT, "r", encoding="utf-8") as f:
    txt_ids = [line.strip() for line in f if line.strip()]

# Construir lista final
items = []
added = 0
for item_id in txt_ids:
    if item_id in existing:
        items.append(existing[item_id])
    else:
        label = item_id.replace("_", " ").title()
        items.append({
            "item": item_id,
            "label": label,
            "limit": 250,
            "can_remove": 1,
            "type": "item_standard",
            "usable": 1,
            "metadata": "{}",
            "desc": "",
            "weight": 0.5,
            "degradation": 0,
            "groupId": 9
        })
        added += 1

# Guardar
with open(JSON, "w", encoding="utf-8") as f:
    json.dump({"items": items}, f, ensure_ascii=False, indent=2)

print(f"Total: {len(items)} items ({added} nuevos)")
