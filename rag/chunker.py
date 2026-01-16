import json

INPUT_FILE = "data/functions.json"
OUTPUT_FILE = "data/code_chunks.json"

# Load extracted functions
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    functions = json.load(f)

chunks = []

for idx, fn in enumerate(functions):
    chunk_text = (
        f"Function {fn['name']} defined in file {fn['file']} "
        f"at line {fn['line']}."
    )

    chunks.append({
        "id": idx,
        "text": chunk_text
    })

# Save chunks
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2)

print("✅ Code chunks created:", len(chunks))
print("📁 Saved to:", OUTPUT_FILE)
